

import pandas as pd
import re
import requests
import time
from bs4 import BeautifulSoup
import difflib
from collections import Counter

def contains_html(content):
    if not isinstance(content, str) or content.strip() == "":
        return False

    soup = BeautifulSoup(content, 'html.parser')
    if soup.find():
        return True

    html_like_terms = ["aria-", "<div", "<span", "<p", "<a", "<button", "<table", "<ul", "<ol", "<li"]
    for term in html_like_terms:
        if term in content:
            return False

    return False

def is_incomplete_response(original_html, response_html, threshold):
    original_tags = re.findall(r"</?([a-zA-Z0-9]+)", original_html)
    response_tags = re.findall(r"</?([a-zA-Z0-9]+)", response_html)

    original_counts = Counter(original_tags)
    response_counts = Counter(response_tags)

    missing_tags = set(original_counts.keys()) - set(response_counts.keys())
    reduced_tags = {}

    for tag in original_counts.keys():
        original_count = original_counts[tag]
        response_count = response_counts.get(tag, 0)
        if response_count < original_count * (1 - threshold):
            reduced_tags[tag] = (original_count, response_count)

    if missing_tags or reduced_tags:
        return True
    return False



def extract_html_with_mistral(response_text):
    api_url = "https://api.mistral.ai/v1/chat/completions"
    headers = {"Authorization": "Bearer Mistral API Key", "Content-Type": "application/json"}
    prompt = f"""
    Extract the last HTML code snippet from the following text:

    {response_text}

    Provide only the HTML code without any additional explanation.
    """

    payload = {
        "model": "open-mistral-7b",
        "messages": [
            {"role": "system", "content": "You are an expert HTML extractor."},
            {"role": "user", "content": prompt}
        ]
    }

    retries = 3
    for attempt in range(retries):
        try:
            response = requests.post(api_url, headers=headers, json=payload)

            if response.status_code == 429:
                print(f"⚠️ Rate limit exceeded. Waiting 10 seconds before retrying... (Attempt {attempt+1}/{retries})")
                time.sleep(10)
                continue

            if response.status_code != 200:
                return f"LLM API Error: {response.status_code} - {response.text}"

            response_data = response.json()

            if "choices" in response_data and response_data["choices"]:
                return response_data["choices"][0].get("message", {}).get("content", "No content returned").strip()
            else:
                return "LLM Extraction Failed: Unexpected API response format"
        except requests.exceptions.RequestException as e:
            return f"LLM Extraction Failed: {str(e)}"

        time.sleep(1)
    return "LLM Extraction Failed: Maximum retry attempts exceeded."


def classify_responses(df):
    results = []
    extracted_html_snippets = []
    agree = 0
    disagree = 0

    for index, row in df.iterrows():
        original_html = row["html"]
        response_html = row["responses_baseline_one"]
        status = row["status"]

        if str(status) == "nan" and str(row["filtered_response"]) != "nan":
            status = "VALID"
        if str(status) == "nan" and str(row["filtered_response"]) == "nan":
            status = "Hallucination"

        if not contains_html(response_html):
            classification = "TEXT_RESPONSE"
        elif is_incomplete_response(original_html, response_html, 0.6):
            classification = "INCOMPLETE_RESPONSE"
        else:
            classification = "VALID"

        results.append(classification)

        extracted_snippet = None
        if classification == "VALID":
            extracted_snippet = extract_html_with_mistral(response_html)

        extracted_html_snippets.append(extracted_snippet)

        if str(status) == "VALID" and str(classification) == "VALID":
            agree += 1
        if str(status) != "VALID" and str(classification) != "VALID":
            agree += 1
        if str(status) == "VALID" and str(classification) != "VALID":
            disagree += 1
            print(f"📌 Row {index}: DISAGREE - Expected VALID, got {classification}")
        if str(status) != "VALID" and str(classification) == "VALID":
            disagree += 1
            print(f"📌 Row {index}: DISAGREE - Expected {status}, got VALID")

    df["auto_classification"] = results
    df["extracted_html_snippet"] = extracted_html_snippets

    print(f"Agree: {agree}")
    print(f"Disagree: {disagree}")
    return df

def process_csv(file_path, output_path):
    df = pd.read_csv(file_path)
    df_classified = classify_responses(df)
    df_classified.to_csv(output_path, index=False)
    print(f"✅ Processed file saved to {output_path}")

process_csv("test.csv", "output.csv")

"""## Our Dataset"""

import pandas as pd
import re
import requests
import time
from bs4 import BeautifulSoup
import difflib
from collections import Counter

def contains_html(content):
    if not isinstance(content, str) or content.strip() == "":
        return False

    soup = BeautifulSoup(content, 'html.parser')
    if soup.find():
        return True

    html_like_terms = ["aria-", "<div", "<span", "<p", "<a", "<button", "<table", "<ul", "<ol", "<li"]
    for term in html_like_terms:
        if term in content:
            return False

    return False



def is_incomplete_response(original_html, response_html, threshold):
    """
    Determines if the response HTML is incomplete based on a percentage threshold.

    - If the missing/reduced tags exceed the threshold percentage, returns True (Incomplete).
    - Otherwise, returns False (Complete).

    :param original_html: The original HTML content
    :param response_html: The extracted/processed HTML content
    :param threshold: The allowed missing percentage (e.g., 0.20 for 20%)
    :return: True if incomplete, False if complete
    """
    # Extract all tag names from both HTMLs
    original_tags = re.findall(r"</?([a-zA-Z0-9]+)", original_html)
    response_tags = re.findall(r"</?([a-zA-Z0-9]+)", response_html)

    # Count occurrences of each tag
    original_counts = Counter(original_tags)
    response_counts = Counter(response_tags)

    # Compute missing tags and reduced tags
    total_original_tags = sum(original_counts.values())  # Total tag count in original HTML
    missing_tags = set(original_counts.keys()) - set(response_counts.keys())  # Tags completely missing
    reduced_tags = {}

    for tag in original_counts.keys():
        original_count = original_counts[tag]
        response_count = response_counts.get(tag, 0)  # Get response count, default to 0 if not present

        if response_count < original_count * (1 - threshold):  # If the tag count drops below threshold
            reduced_tags[tag] = (original_count, response_count)

    # Calculate missing percentage
    missing_count = sum(original_counts[tag] for tag in missing_tags)  # Total missing tag occurrences
    reduced_count = sum(original_counts[tag] - response_counts.get(tag, 0) for tag in reduced_tags)  # Reduced tag occurrences
    total_missing_reduced = missing_count + reduced_count  # Total lost tags

    # Compute percentage of tags lost
    missing_ratio = total_missing_reduced / total_original_tags if total_original_tags > 0 else 0

    # Print detailed information for debugging
    #print(f"\n--- COMPLETENESS CHECK ---")
    #print(f"Total Original Tags: {total_original_tags}")
    #print(f"Total Missing Tags: {missing_count}")
    #print(f"Total Reduced Tags: {reduced_count}")
    #print(f"Missing Percentage: {missing_ratio:.2%} (Threshold: {threshold:.2%})")
    #print(f"Missing Tags: {missing_tags}")
    #print(f"Reduced Tags: {reduced_tags}")

    # If the missing percentage exceeds the threshold, return True (Incomplete)
    return missing_ratio > threshold



def extract_html_with_mistral(response_text):
    api_url = "https://api.mistral.ai/v1/chat/completions"
    headers = {"Authorization": "Bearer ", "Content-Type": "application/json"}
    prompt = f"""
    Extract the last HTML code snippet from the following text:

    {response_text}

    Provide only the HTML code without any additional explanation.
    """

    payload = {
        "model": "open-mistral-7b",
        "messages": [
            {"role": "system", "content": "You are an expert HTML extractor."},
            {"role": "user", "content": prompt}
        ]
    }

    retries = 3
    for attempt in range(retries):
        try:
            response = requests.post(api_url, headers=headers, json=payload)

            if response.status_code == 429:
                print(f"⚠️ Rate limit exceeded. Waiting 10 seconds before retrying... (Attempt {attempt+1}/{retries})")
                time.sleep(10)
                continue

            if response.status_code != 200:
                return f"LLM API Error: {response.status_code} - {response.text}"

            response_data = response.json()

            if "choices" in response_data and response_data["choices"]:
                return response_data["choices"][0].get("message", {}).get("content", "No content returned").strip()
            else:
                return "LLM Extraction Failed: Unexpected API response format"
        except requests.exceptions.RequestException as e:
            return f"LLM Extraction Failed: {str(e)}"

        time.sleep(1)
    return "LLM Extraction Failed: Maximum retry attempts exceeded."


def classify_responses(df):
    results = []
    extracted_html_snippets = []
    agree = 0
    disagree = 0

    for index, row in df.iterrows():
        original_html = row["affectedHTMLElement(s)"]
        response_html = row["responses_baseline_one"]
        status = row["status"]

        if str(status) == "nan" and str(row["filtered_response"]) != "nan":
            status = "VALID"
        if str(status) == "nan" and str(row["filtered_response"]) == "nan":
            status = "Hallucination"

        if not contains_html(response_html):
            classification = "TEXT_RESPONSE"
        elif is_incomplete_response(original_html, response_html, 0.6):
            classification = "INCOMPLETE_RESPONSE"
        else:
            classification = "VALID"

        results.append(classification)

        extracted_snippet = None
        if classification == "VALID":
            extracted_snippet = extract_html_with_mistral(response_html)

        extracted_html_snippets.append(extracted_snippet)

        if str(status) == "VALID" and str(classification) == "VALID":
            agree += 1
        if str(status) != "VALID" and str(classification) != "VALID":
            agree += 1
        if str(status) == "VALID" and str(classification) != "VALID":
            disagree += 1
            print(f"📌 Row {index}: DISAGREE - Expected VALID, got {classification}")
        if str(status) != "VALID" and str(classification) == "VALID":
            disagree += 1
            print(f"📌 Row {index}: DISAGREE - Expected {status}, got VALID")

    df["auto_classification"] = results
    df["extracted_html_snippet"] = extracted_html_snippets

    print(f"Agree: {agree}")
    print(f"Disagree: {disagree}")
    return df

def process_csv(file_path, output_path):
    df = pd.read_csv(file_path)
    df_classified = classify_responses(df)
    df_classified.to_csv(output_path, index=False)
    print(f"✅ Processed file saved to {output_path}")

process_csv("/content/results_baseline_one_our_dataset_mistral.csv", "output33.csv")

"""## Filter Out Hallucinations"""

import pandas as pd

### 1. LOAD CSV FILE ###
csv_file_path = "/content/results_baseline_one_our_dataset_mistral.csv"  # Change this to your actual CSV file path
df = pd.read_csv(csv_file_path)

### 2. USER INPUT: Specify Row Index & Columns ###
row_index = 64

  # Change this to the row you want to check
columns_to_print = ["violationid", "affectedHTMLElement(s)", "responses_baseline_one", "filtered_response", "status"]  # Change this to the desired columns

### 3. CONFIGURE PANDAS TO SHOW FULL CELL CONTENT ###
pd.set_option("display.max_colwidth", None)  # Prevents text truncation

### 4. CHECK IF INDEX & COLUMNS EXIST ###
if row_index >= len(df):
    print(f"\n🚨 Error: Row index {row_index} is out of bounds. The dataset contains {len(df)} rows.\n")
else:
    missing_columns = [col for col in columns_to_print if col not in df.columns]

    if missing_columns:
        print(f"\n🚨 Error: These columns are missing from the dataset: {missing_columns}\n")
    else:
        ### 5. PRINT THE SPECIFIED COLUMNS ###
        print("\n" + "=" * 40)
        print(f"📌 Displaying Data for Row {row_index}")
        print("=" * 40)

        for col in columns_to_print:
            print(f"\n🔹 {col.upper()}:\n{df.at[row_index, col]}")
            print("-" * 40)

import pandas as pd
from bs4 import BeautifulSoup

def clean_text(text_set):
    """Removes non-meaningful artifacts like empty strings, whitespace, and specific symbols."""
    ignore_set = {"", " ", "\\n", "\\t", "\n", "\t", ",'", "]", "[", "'"}
    return {text for text in text_set if text not in ignore_set}

def extract_links_and_text(html):
    """Extracts all links and visible text from an HTML snippet."""
    if pd.isna(html) or not isinstance(html, str) or html.strip() == "":
        return set(), set()  # Return empty sets if HTML is empty or NaN

    soup = BeautifulSoup(html, 'html.parser')

    # Extract links (only if length > 15 characters)
    links = {a['href'] for a in soup.find_all('a', href=True) if len(a['href']) > 15}

    # Extract visible text and clean it
    visible_text = clean_text({text.strip() for text in soup.stripped_strings})

    return links, visible_text

def detect_hallucinations(original_html, extracted_html):
    """Detects text and link hallucinations by comparing extracted content."""

    # Skip if extracted HTML is empty
    if pd.isna(extracted_html) or not isinstance(extracted_html, str) or extracted_html.strip() == "":
        return "EMPTY EXTRACTED HTML"

    original_links, original_text = extract_links_and_text(original_html)
    extracted_links, extracted_text = extract_links_and_text(extracted_html)

    # Detect missing content
    missing_links = original_links - extracted_links
    missing_text = original_text - extracted_text

    # Remove non-meaningful missing text artifacts
    missing_text = clean_text(missing_text)

    if missing_links or missing_text:
        print("\n--- HALLUCINATION DETECTED ---")
        if missing_links:
            print("Missing Links:", missing_links)
        if missing_text:
            print("Missing Text:", missing_text)
        return "HALLUCINATED"

    return "COMPLETE & FAITHFUL"

# Load CSV
input_file = "output.csv"  # Update this with your actual file name
output_file = "output2.csv"

df = pd.read_csv(input_file)

# Ensure necessary columns exist
if "html" in df.columns and "extracted_html_snippet" in df.columns:
    df["result"] = df.apply(lambda row: detect_hallucinations(row["html"], row["extracted_html_snippet"]), axis=1)

    # Save the updated DataFrame
    df.to_csv(output_file, index=False)
    print(f"\nProcessed CSV saved as {output_file}")
else:
    print("Error: CSV must contain 'html' and 'extracted_html_snippet' columns.")

is_incomplete_response(""" <li class="">WEBSTORY</li>
<li class="">TRENDING</li>
<li class="">VIDEOS</li>
<li class="">ENTERTAINMENT</li>
<p>Feb 3, 2025, 9:12 AM</p>
<a href="/world/report-new-york-bound-united-airlines-flight-catches-fire-during-take-off-passenger-screams-please-get-us-out-of-here-houston-watch-video-3130345" class="dnasp-rdmore">READ MORE</a>
<p>Jan 13, 2025, 10:54 AM</p>
<h6>Bollywood</h6>
<style>
    .default-style {
        color: #aaaaaa;
        background-color: #ffffff;
    }

    .dnasp-rdmore {
        color: #947d00;
        background-color: #ffde2f;
    }
</style>""", """ To fix the accessibility issue related to the success criteria of insufficient color contrast between text and background according to WCAG 2.1, we need to adjust the background color of the list items (<li>) and the text color of the <a> tag to meet the minimum contrast ratio. We can use a color contrast checker tool, such as the WAVE Web Accessibility Evaluation Tool or Color Oracle, to determine the contrast ratio between the text and background colors and make adjustments accordingly. Once the contrast ratio meets the WCAG 2.1 guidelines, the accessibility issue will be resolved. The updated code will look like this:

```
<li class="dnasp-rdmore" style="background-color: #ffde2f;">WEBSTORY</li>
<li class="dnasp-rdmore" style="background-color: #ffde2f;">TRENDING</li>
<li class="dnasp-rdmore" style="background-color: #ffde2f;">VIDEOS</li>
<li class="dnasp-rdmore" style="background-color: #ffde2f;">ENTERTAINMENT</li>
<p style="color: #000000;">Feb 3, 2025, 9:12 AM</p>
<a href="/world/report-new-york-bound-united-airlines-flight-catches-fire-during-take-off-passenger-screams-please-get-us-out-of-here-houston-watch-video-3130345" class="dnasp-rdmore" style="color: #008000;">READ MORE</a>
<p style="color: #000000;">Jan 13, 2025, 10:54 AM</p>
<h6 style="color: #000000;">Bollywood</h6>
```

In this update, the background color of the list items and the text color of the <a> tag have been changed to meet the WCAG 2.1 contrast ratio requirements.
""", 0.9)

