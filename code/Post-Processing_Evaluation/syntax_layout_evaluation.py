

tags = ['ACT' ,'EN-301-549' ,'EN-9.1.1.1' ,'EN-9.1.2.2' ,'EN-9.1.3.1' ,'EN-9.1.3.5',
 'EN-9.1.4.1' ,'EN-9.1.4.12' ,'EN-9.1.4.2', 'EN-9.1.4.3', 'EN-9.1.4.4',
 'EN-9.2.1.1' ,'EN-9.2.1.3' ,'EN-9.2.2.1' ,'EN-9.2.2.2', 'EN-9.2.4.1',
 'EN-9.2.4.2', 'EN-9.2.4.4' ,'EN-9.3.1.1' ,'EN-9.3.1.2', 'EN-9.3.3.2',
 'EN-9.4.1.2' ,'TT11.a' ,'TT11.b', 'TT12.a' ,'TT12.d', 'TT13.a' ,'TT13.c',
 'TT14.b', 'TT17.a' ,'TT2.a' ,'TT2.b' ,'TT4.a' ,'TT5.c', 'TT6.a' ,'TT7.a', 'TT7.b',
 'TT8.a', 'TT9.a', 'TTv5', 'best-practice' ,'cat.aria', 'cat.color' ,'cat.forms',
 'cat.keyboard', 'cat.language', 'cat.name-role-value' , 'cat.parsing',
 'cat.semantics', 'cat.sensory-and-visual-cues' ,'cat.structure',
 'cat.tables' ,'cat.text-alternatives' ,'cat.time-and-media' ,'review-item',
 'section508' ,'section508.22.a', 'section508.22.f' ,'section508.22.g',
 'section508.22.i' ,'section508.22.j' ,'section508.22.n' ,'section508.22.o',
 'wcag111' ,'wcag122' ,'wcag131' ,'wcag135' ,'wcag141' ,'wcag1412' ,'wcag142',
 'wcag143' ,'wcag144' ,'wcag146' ,'wcag211' ,'wcag213' ,'wcag21aa' ,'wcag221' ,
 'wcag222' ,'wcag224', 'wcag22aa', 'wcag241', 'wcag242', 'wcag244' , 'wcag249',
 'wcag258', 'wcag2a', 'wcag2aa' ,'wcag2aaa', 'wcag311' ,'wcag312' ,'wcag325',
 'wcag332', 'wcag412']

!pip install playwright google-colab nest_asyncio
!playwright install

import nest_asyncio
import asyncio
import pandas as pd
from playwright.async_api import async_playwright
from google.colab import data_table  # Colab-friendly table display

"""## Our Dataset"""

import nest_asyncio
import asyncio
import pandas as pd
from playwright.async_api import async_playwright
from google.colab import data_table  # Colab-friendly table display

# Apply nest_asyncio to allow nested event loops in Colab
nest_asyncio.apply()

# Mapping impact levels to numeric scores
impactScore = {
    "critical": 5,
    "serious": 4,
    "moderate": 3,
    "minor": 2,
    "cosmetic": 1,
    "accessible": 0
}

import re
def extract_ids_from_html(html_content):
    """Extract all id attributes from an HTML snippet."""
    if not isinstance(html_content, str):
        return set()
    return set(re.findall(r'id=["\'](.*?)["\']', html_content))

def extract_attributes_from_html(html_content):
    """Extract label, title, role, and alt attributes from an HTML snippet."""
    if not isinstance(html_content, str):
        return {}
    attributes = {
        "label": [val for val in re.findall(r'label=["\'](.*?)["\']', html_content) if val.strip()],
        "title": [val for val in re.findall(r'title=["\'](.*?)["\']', html_content) if val.strip()],
        "role": [val for val in re.findall(r'role=["\'](.*?)["\']', html_content) if val.strip()],
        "alt": [val for val in re.findall(r'alt=["\'](.*?)["\']', html_content) if val.strip()],
        "aria-label": [val for val in re.findall(r'aria-label=["\'](.*?)["\']', html_content) if val.strip()]
    }
    return attributes
def extract_attributes_from_html2(html_content):
    """Extract various accessibility-related attributes from an HTML snippet."""
    if not isinstance(html_content, str):
        return {}
    attributes = {
        "aria-label": [val for val in re.findall(r'aria-label=["\'](.*?)["\']', html_content) if val.strip()],
       "aria-braillelabel": [val for val in re.findall(r'aria-braillelabel=["\'](.*?)["\']', html_content) if val.strip()],
        "aria-brailleroledescription": [val for val in re.findall(r'aria-brailleroledescription=["\'](.*?)["\']', html_content) if val.strip()],
        "aria-roledescription": [val for val in re.findall(r'aria-roledescription=["\'](.*?)["\']', html_content) if val.strip()]
    }
    return attributes

# Violations that require manual ID comparison
id_check_violations = {"duplicate-id", "duplicate-id-active", "duplicate-id-aria"}
id_check_violations2 = { "landmark-unique" , "accesskeys" , "frame-title-unique", "image-redundant-alt" }
id_check_violations3 = { "landmark-complementary-is-top-level","landmark-contentinfo-is-top-level",
                        "landmark-main-is-top-level" ,"heading-order"}
violation_aliases = {
    "area-alt": "img-alt",
    "aria-roles": "aria-deprecated-role",
    "aria-prohibited-attr": ["aria-valid-attr-value", "aria-allowed-attr"],
    "aria-hidden-body": "aria-hidden-focus"
}




async def check_accessibility_from_html(html_content):
    """Launch Playwright and check accessibility violations for a given HTML snippet."""
    try:
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()

            await page.set_content(html_content)  # Set page content to the provided HTML
            await page.add_script_tag(url="https://cdn.jsdelivr.net/npm/axe-core@4.4.1/axe.min.js")  # Inject axe-core

            # Evaluate accessibility using axe-core
            results = await page.evaluate("""
            async () => {
                return await axe.run(document, {
                    runOnly: {
                        type: 'tag',
                        values: ['ACT' ,'EN-301-549' ,'EN-9.1.1.1' ,'EN-9.1.2.2' ,'EN-9.1.3.1' ,'EN-9.1.3.5',
 'EN-9.1.4.1' ,'EN-9.1.4.12' ,'EN-9.1.4.2', 'EN-9.1.4.3', 'EN-9.1.4.4',
 'EN-9.2.1.1' ,'EN-9.2.1.3' ,'EN-9.2.2.1' ,'EN-9.2.2.2', 'EN-9.2.4.1',
 'EN-9.2.4.2', 'EN-9.2.4.4' ,'EN-9.3.1.1' ,'EN-9.3.1.2', 'EN-9.3.3.2',
 'EN-9.4.1.2' ,'TT11.a' ,'TT11.b', 'TT12.a' ,'TT12.d', 'TT13.a' ,'TT13.c',
 'TT14.b', 'TT17.a' ,'TT2.a' ,'TT2.b' ,'TT4.a' ,'TT5.c', 'TT6.a' ,'TT7.a', 'TT7.b',
 'TT8.a', 'TT9.a', 'TTv5', 'best-practice' ,'cat.aria', 'cat.color' ,'cat.forms',
 'cat.keyboard', 'cat.language', 'cat.name-role-value' , 'cat.parsing',
 'cat.semantics', 'cat.sensory-and-visual-cues' ,'cat.structure',
 'cat.tables' ,'cat.text-alternatives' ,'cat.time-and-media' ,'review-item',
 'section508' ,'section508.22.a', 'section508.22.f' ,'section508.22.g',
 'section508.22.i' ,'section508.22.j' ,'section508.22.n' ,'section508.22.o',
 'wcag111' ,'wcag122' ,'wcag131' ,'wcag135' ,'wcag141' ,'wcag1412' ,'wcag142',
 'wcag143' ,'wcag144' ,'wcag146' ,'wcag211' ,'wcag213' ,'wcag21aa' ,'wcag221' ,
 'wcag222' ,'wcag224', 'wcag22aa', 'wcag241', 'wcag242', 'wcag244' , 'wcag249',
 'wcag258', 'wcag2a', 'wcag2aa' ,'wcag2aaa', 'wcag311' ,'wcag312' ,'wcag325',
 'wcag332', 'wcag412']

 }
                });
            }
            """)

            await browser.close()  # Close browser
            return results  # Return the accessibility results
    except Exception as e:
        return {"error": str(e)}  # Handle errors gracefully

async def process_csv(file_path):
    """Process the CSV file and calculate new violation scores."""
    df = pd.read_csv(file_path)  # Read the CSV file into a DataFrame

    # Check if required columns exist in the CSV
    if "affectedHTMLElement(s)" not in df.columns or "violationnumberID" not in df.columns or "filtered_response" not in df.columns:
        print("Error: Required columns not found in the CSV file.")
        return

    results = []  # Initialize results list
    count_hall = 0
    for index, row in df.iterrows():
    #for index, row in df.head(25).iterrows():

        element_html = row["affectedHTMLElement(s)"]  # Extract affected elements HTML
        violation_id = row["violationnumberID"]  # Extract violation ID
        oldscore = row["initialImpactScore"]  # Extract original impact score
        category = row["category"]
        case_descriptions = ""
        print(str(index)+ " "+ str(violation_id))
        if category != "Semantic":
                    # Get old violations using Playwright
                old_violations_results = await check_accessibility_from_html(element_html)
                old_violations = {v["id"] for v in old_violations_results.get("violations", [])}

                if violation_id in violation_aliases:
                  if violation_id != "aria-prohibited-attr":
                    violation_id = violation_aliases[violation_id]
                  else:
                    if "aria-valid-attr-value" in old_violations:
                      violation_id = "aria-valid-attr-value"
                    else:
                      violation_id = "aria-allowed-attr"

                # Debugging: Check extracted old violations
                #print(f"Extracted Old Violations for Row {index}: {old_violations}")

                    # If violation ID is not in old violations, require manual check


                        # Check if filtered_response is empty
                if pd.isna(row["filtered_response"]) or row["filtered_response"].strip() == "":
                            new_score = oldscore  # Retain old score if no new response
                        #Debugging
                            #print("Filtered Response is empty")
                            case_descriptions = "LLM Hallucination"
                            #print(case_descriptions)
                            print("LLM Hallucination")
                            count_hall+=1
                else:

                      if violation_id not in old_violations:
                              print("CHECK Manual")
                              new_violations_results = await check_accessibility_from_html(row["filtered_response"])
                              new_violations = {v["id"]: v["impact"] for v in new_violations_results.get("violations", [])}

                              introduced_violations = set(new_violations.keys()) - old_violations
                              if introduced_violations:
                                  impact_sum = sum(impactScore.get(new_violations[v], 0) for v in introduced_violations)
                                  #new_score = f"CHECK MANUALLY + {impact_sum}"
                                  new_score = impact_sum
                                  case_descriptions = "CHECKS,  New violations were introduced"
                              else:
                                  #new_score = "CHECK MANUALLY"
                                  new_score = 0
                              case_descriptions = "CHECKS, Violation ID not found in old violations"
                              #       new_score =  "CHECK MANUALLY, Old violations: " + str(old_violations)
                              if violation_id in id_check_violations:
                                  if not extract_ids_from_html(str(element_html)).isdisjoint(extract_ids_from_html(str(row["filtered_response"]))):
                                    new_score += oldscore
                              if violation_id in id_check_violations2:
                                  if {item for sublist in extract_attributes_from_html(str(element_html)).values() for item in sublist} & {item for sublist in extract_attributes_from_html(str(row["filtered_response"])).values() for item in sublist}:  # If there is a common element
                                    new_score += oldscore
                              if violation_id == "link-in-text-block":
                                  if not bool(re.search(r'text-decoration:\s*underline', str(row["filtered_response"])) or
                                          re.search(r'border-bottom:\s*1px solid', str(row["filtered_response"])) or
                                          re.search(r'<u.*?</u>', str(row["filtered_response"]), re.IGNORECASE)
                                      ):
                                    new_score += oldscore

                              if violation_id == "link-name":
                                new_attributes = extract_attributes_from_html(str(row["filtered_response"]))
                                if not any(new_attributes[attr] for attr in ["alt", "title", "aria-label"] if new_attributes.get(attr) and any(val.strip() for val in new_attributes[attr])):
                                  new_score += oldscore
                              if violation_id == "no-autoplay-audio":
                                if "autoplay" in str(row["filtered_response"]).lower():
                                  new_score += oldscore
                              if violation_id == "role-img-alt":
                                new_attributes = extract_attributes_from_html(str(row["filtered_response"]))
                                if not any(new_attributes[attr] for attr in ["alt"] if new_attributes.get(attr) and any(val.strip() for val in new_attributes[attr])):
                                  new_score += oldscore
                              if violation_id == "scrollable-region-focusable":
                                if 'tabindex="0"' or 'scroll' not in str(row["filtered_response"]).lower():
                                  new_score += oldscore
                              if violation_id == "summary-name":
                                has_summary_text = bool(re.search(r'<summary>\s*([^<\s][^<]*?)\s*</summary>', str(row["filtered_response"]), re.IGNORECASE))
                                has_alternative_attrs = bool(re.search(r'aria-labelledby=["\']([^"\']\S+)["\']', str(row["filtered_response"])) or
                                        re.search(r'title=["\']([^"\']\S+)["\']', str(row["filtered_response"])))
                                if  not has_summary_text or has_alternative_attrs:
                                  new_score += oldscore

                              if violation_id == "target-size":
                                sizes = [int(size) for size in re.findall(r'(\d+)px',str(row["filtered_response"])) if size.isdigit()]
                                if not all(size >= 24 for size in sizes):
                                  new_score += oldscore
                              if violation_id == "aria-braille-equivalent":
                                attributes = extract_attributes_from_html2(str(row["filtered_response"]))
                                if not bool(attributes["aria-brailleroledescription"] or  attributes["aria-roledescription"] or attributes["aria-braillelabel"] or attributes["aria-label"]) :
                                  new_score += oldscore
                              if violation_id == "aria-conditional-attr" or violation_id == "th-has-data-cells" or violation_id == "form-field-multiple-labels":
                                old_violations_results = await check_accessibility_from_html(element_html)
                                old_violations = {v["id"] for v in old_violations_results.get("violations", [])}
                                new_violations_results = await check_accessibility_from_html(row["filtered_response"])
                                new_violations = {v["id"]: v["impact"] for v in new_violations_results.get("violations", [])}
                                introduced_violations = set(new_violations.keys()) - old_violations
                                if introduced_violations:
                                          impact_sum = sum(impactScore.get(new_violations[v], 0) for v in introduced_violations)
                                                        #new_score = f"CHECK MANUALLY + {impact_sum}"
                                          new_score = str(impact_sum) + " CHECK MANUALLY"
                                          case_descriptions = "CHECKS,  New violations were introduced"
                                else:
                                                        #new_score = "CHECK MANUALLY"
                                          new_score = str(0) + " CHECK MANUALLY"
                                          case_descriptions = "CHECKS, Violation ID not found in old violations"

                              if violation_id == "video-caption":
                                      if "track" not in str(row["filtered_response"]).lower():
                                        if "caption" not in str(row["filtered_response"]).lower():
                                              new_score+= oldscore
                              if violation_id == "landmark-no-duplicate-banner":
                                  if "banner" in str(row["filtered_response"]).lower():
                                      new_score += oldscore
                              if violation_id == "landmark-no-duplicate-contentinfo":
                                  if "contentinfo" in str(row["filtered_response"]).lower():
                                    new_score += oldscore
                              if violation_id == "landmark-no-duplicate-main":
                                  if "main" in str(row["filtered_response"]).lower():
                                      new_score += oldscore
                              if violation_id == "frame-focusable-content":
                                if "tabindex=-1" in str(row["filtered_response"]):
                                  new_score += oldscore
                              if violation_id == "frame-title":
                                if 'title=""' in str(row["filtered_response"]) or 'title' not in str(row["filtered_response"]):
                                  new_score+= oldscore
                              if violation_id =="bypass":
                                if "main" not in str(row["filtered_response"]):
                                  new_score += oldscore
                              if violation_id in id_check_violations3:
                                old_violations.add(violation_id)



                              # cases not handeled




                      else:
                                  # Get new violations using Playwright on the filtered response
                                  new_violations_results = await check_accessibility_from_html(row["filtered_response"])
                                  new_violations = {v["id"]: v["impact"] for v in new_violations_results.get("violations", [])}
                                          # Debugging: Check extracted new violations
                                  #print(f"Extracted New Violations for Row {index}: {new_violations}")
                                  if violation_id not in new_violations:  # If original violation was fixed
                                      new_score = 0  # No new violations, set to 0
                                      introduced_violations = set(new_violations.keys()) - old_violations  # Find new violations introduced
                                      if introduced_violations:
                                        for new_violation in introduced_violations:
                                            impact = impactScore.get(new_violations[new_violation], 0)  # Get impact score from Playwright results
                                            #print("nado2    "+ str(impact))
                                            new_score += impact  # Add impact score to new score
                                        print("Original Violations was fixed, New violations were introduced")
                                        case_descriptions= "Original Violations was fixed, New violations were introduced"
                                        #print(case_descriptions)
                                        print(f"New Violations Introduced for Row {index}: {introduced_violations}")
                                      else:
                                        print("Original Violations was fixed, No new violations were introduced")
                                        case_descriptions = "Original Violations was fixed, No new violations were introduced"
                                        #print(case_descriptions)
                                  else:
                                      new_score = oldscore  # Retain old score
                                      #print("nado      "+ str(new_score))
                                      #Debugging
                                      #print("Original violation was not fixed")
                                      introduced_violations = set(new_violations.keys()) - old_violations  # Find new violations introduced
                                      for new_violation in introduced_violations:
                                          impact = impactScore.get(new_violations[new_violation], 0)  # Get impact score from Playwright results
                                          #print("nado    "+ str(impact))
                                          new_score += impact  # Add impact score to new score
                                      #Debugging
                                      #print("New impact Score "+ str(new_score))
                                      if introduced_violations:
                                          print("Original violation was not fixed, New violations were introduced")
                                          case_descriptions = "Original violation was not fixed, New violations were introduced"
                                          #print(case_descriptions)
                                          #print(f"New Violations Introduced for Row {index}: {introduced_violations}")
                                      else:
                                          print("Original violation was not fixed, No new violations introduced")
                                          case_descriptions = "Original violation was not fixed, No new violations introduced"
                                          #print(case_descriptions)
        else:
          print("Semantic Violation Requires Manual Inspection")
          old_violations_results = await check_accessibility_from_html(element_html)
          old_violations = {v["id"] for v in old_violations_results.get("violations", [])}
          new_violations_results = await check_accessibility_from_html(row["filtered_response"])
          new_violations = {v["id"]: v["impact"] for v in new_violations_results.get("violations", [])}
          introduced_violations = set(new_violations.keys()) - old_violations
          if introduced_violations:
                    impact_sum = sum(impactScore.get(new_violations[v], 0) for v in introduced_violations)
                                  #new_score = f"CHECK MANUALLY + {impact_sum}"
                    new_score = str(impact_sum) + " CHECK MANUALLY"
                    case_descriptions = "CHECKS,  New violations were introduced"
          else:
                                  #new_score = "CHECK MANUALLY"
                    new_score = str(0) + " CHECK MANUALLY"
                    case_descriptions = "CHECKS, Violation ID not found in old violations"


        #print("-------------------------------------------------------------------")
        #print()
        results.append((violation_id, oldscore, case_descriptions, new_score))  # Append results

    # Convert results to DataFrame
    result_df = pd.DataFrame(results, columns=["violationid", "initialImpactScore", "Case", "newImpactScore"])

    # Save results to CSV
    result_csv_path = "/content/accessibility_results_updated.csv"
    result_df.to_csv(result_csv_path, index=False)
    print(f"Updated results saved to: {result_csv_path}")
    print("LLM Hallucination Count: " + str(count_hall))

    #return data_table.DataTable(result_df)


csv_file_path = "/content/results_baseline_one_our_dataset_mistral.csv"

# Run asyncio in a Colab-friendly way
task = asyncio.ensure_future(process_csv(csv_file_path))
await task  # This avoids `asyncio.run()` errors in Colab

import csv

def count_entries(csv_file):
    with open(csv_file, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader, None)  # Skip header row if present
        return sum(1 for row in reader)

# Example usage:
csv_filename = '/content/results_baseline_one_our_dataset_mistral.csv'  # Replace with your actual file
entry_count = count_entries(csv_filename)
print(f'Total entries: {entry_count}')

"""## Baseline Dataset"""

# prompt: mount drive

from google.colab import drive
drive.mount('/content/drive')

import nest_asyncio
import asyncio
import pandas as pd
from playwright.async_api import async_playwright
from google.colab import data_table  # Colab-friendly table display

# Apply nest_asyncio to allow nested event loops in Colab
nest_asyncio.apply()

# Mapping impact levels to numeric scores
impactScore = {
    "critical": 5,
    "serious": 4,
    "moderate": 3,
    "minor": 2,
    "cosmetic": 1,
    "accessible": 0
}

import re
def extract_ids_from_html(html_content):
    """Extract all id attributes from an HTML snippet."""
    if not isinstance(html_content, str):
        return set()
    return set(re.findall(r'id=["\'](.*?)["\']', html_content))

def extract_attributes_from_html(html_content):
    """Extract label, title, role, and alt attributes from an HTML snippet."""
    if not isinstance(html_content, str):
        return {}
    attributes = {
        "label": [val for val in re.findall(r'label=["\'](.*?)["\']', html_content) if val.strip()],
        "title": [val for val in re.findall(r'title=["\'](.*?)["\']', html_content) if val.strip()],
        "role": [val for val in re.findall(r'role=["\'](.*?)["\']', html_content) if val.strip()],
        "alt": [val for val in re.findall(r'alt=["\'](.*?)["\']', html_content) if val.strip()],
        "aria-label": [val for val in re.findall(r'aria-label=["\'](.*?)["\']', html_content) if val.strip()]
    }
    return attributes
def extract_attributes_from_html2(html_content):
    """Extract various accessibility-related attributes from an HTML snippet."""
    if not isinstance(html_content, str):
        return {}
    attributes = {
        "aria-label": [val for val in re.findall(r'aria-label=["\'](.*?)["\']', html_content) if val.strip()],
       "aria-braillelabel": [val for val in re.findall(r'aria-braillelabel=["\'](.*?)["\']', html_content) if val.strip()],
        "aria-brailleroledescription": [val for val in re.findall(r'aria-brailleroledescription=["\'](.*?)["\']', html_content) if val.strip()],
        "aria-roledescription": [val for val in re.findall(r'aria-roledescription=["\'](.*?)["\']', html_content) if val.strip()]
    }
    return attributes

# Violations that require manual ID comparison
id_check_violations = {"duplicate-id", "duplicate-id-active", "duplicate-id-aria"}
id_check_violations2 = { "landmark-unique" , "accesskeys" , "frame-title-unique", "image-redundant-alt" }
id_check_violations3 = { "landmark-complementary-is-top-level","landmark-contentinfo-is-top-level",
                        "landmark-main-is-top-level" ,"heading-order"}
violation_aliases = {
    "area-alt": "img-alt",
    "aria-roles": "aria-deprecated-role",
    "aria-prohibited-attr": ["aria-valid-attr-value", "aria-allowed-attr"],
    "aria-hidden-body": "aria-hidden-focus"
}




async def check_accessibility_from_html(html_content):
    """Launch Playwright and check accessibility violations for a given HTML snippet."""
    try:
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()

            await page.set_content(html_content)  # Set page content to the provided HTML
            await page.add_script_tag(url="https://cdn.jsdelivr.net/npm/axe-core@4.4.1/axe.min.js")  # Inject axe-core

            # Evaluate accessibility using axe-core
            results = await page.evaluate("""
            async () => {
                return await axe.run(document, {
                    runOnly: {
                        type: 'tag',
                        values: ['ACT' ,'EN-301-549' ,'EN-9.1.1.1' ,'EN-9.1.2.2' ,'EN-9.1.3.1' ,'EN-9.1.3.5',
 'EN-9.1.4.1' ,'EN-9.1.4.12' ,'EN-9.1.4.2', 'EN-9.1.4.3', 'EN-9.1.4.4',
 'EN-9.2.1.1' ,'EN-9.2.1.3' ,'EN-9.2.2.1' ,'EN-9.2.2.2', 'EN-9.2.4.1',
 'EN-9.2.4.2', 'EN-9.2.4.4' ,'EN-9.3.1.1' ,'EN-9.3.1.2', 'EN-9.3.3.2',
 'EN-9.4.1.2' ,'TT11.a' ,'TT11.b', 'TT12.a' ,'TT12.d', 'TT13.a' ,'TT13.c',
 'TT14.b', 'TT17.a' ,'TT2.a' ,'TT2.b' ,'TT4.a' ,'TT5.c', 'TT6.a' ,'TT7.a', 'TT7.b',
 'TT8.a', 'TT9.a', 'TTv5', 'best-practice' ,'cat.aria', 'cat.color' ,'cat.forms',
 'cat.keyboard', 'cat.language', 'cat.name-role-value' , 'cat.parsing',
 'cat.semantics', 'cat.sensory-and-visual-cues' ,'cat.structure',
 'cat.tables' ,'cat.text-alternatives' ,'cat.time-and-media' ,'review-item',
 'section508' ,'section508.22.a', 'section508.22.f' ,'section508.22.g',
 'section508.22.i' ,'section508.22.j' ,'section508.22.n' ,'section508.22.o',
 'wcag111' ,'wcag122' ,'wcag131' ,'wcag135' ,'wcag141' ,'wcag1412' ,'wcag142',
 'wcag143' ,'wcag144' ,'wcag146' ,'wcag211' ,'wcag213' ,'wcag21aa' ,'wcag221' ,
 'wcag222' ,'wcag224', 'wcag22aa', 'wcag241', 'wcag242', 'wcag244' , 'wcag249',
 'wcag258', 'wcag2a', 'wcag2aa' ,'wcag2aaa', 'wcag311' ,'wcag312' ,'wcag325',
 'wcag332', 'wcag412']

 }
                });
            }
            """)

            await browser.close()  # Close browser
            return results  # Return the accessibility results
    except Exception as e:
        return {"error": str(e)}  # Handle errors gracefully

async def process_csv(file_path):
    """Process the CSV file and calculate new violation scores."""
    df = pd.read_csv(file_path)  # Read the CSV file into a DataFrame

    # Check if required columns exist in the CSV
    if "html" not in df.columns or "id" not in df.columns or "filtered_response" not in df.columns:
        print("Error: Required columns not found in the CSV file.")
        return

    results = []  # Initialize results list
    count_hall = 0
    for index, row in df.iterrows():
    #for index, row in df.head(25).iterrows():

        element_html = row["html"]  # Extract affected elements HTML
        violation_id = row["id"]  # Extract violation ID
        oldscore = impactScore.get(row["impact"],0) # Extract original impact score
        case_descriptions = ""
        print(str(index)+ " "+ str(violation_id))
            # Get old violations using Playwright
        old_violations_results = await check_accessibility_from_html(element_html)
        old_violations = {v["id"] for v in old_violations_results.get("violations", [])}

        if violation_id in violation_aliases:
          if violation_id != "aria-prohibited-attr":
            violation_id = violation_aliases[violation_id]
          else:
            if "aria-valid-attr-value" in old_violations:
              violation_id = "aria-valid-attr-value"
            else:
              violation_id = "aria-allowed-attr"

        # Debugging: Check extracted old violations
        #print(f"Extracted Old Violations for Row {index}: {old_violations}")

            # If violation ID is not in old violations, require manual check


                # Check if filtered_response is empty
        if pd.isna(row["filtered_response"]) or row["filtered_response"].strip() == "":
                    new_score = oldscore  # Retain old score if no new response
                #Debugging
                    #print("Filtered Response is empty")
                    case_descriptions = "LLM Hallucination"
                    #print(case_descriptions)
                    print("LLM Hallucination")
                    count_hall+=1
        else:

              if violation_id not in old_violations:
                      print("CHECK Manual")
                      new_violations_results = await check_accessibility_from_html(row["filtered_response"])
                      new_violations = {v["id"]: v["impact"] for v in new_violations_results.get("violations", [])}

                      introduced_violations = set(new_violations.keys()) - old_violations
                      if introduced_violations:
                          impact_sum = sum(impactScore.get(new_violations[v], 0) for v in introduced_violations)
                          #new_score = f"CHECK MANUALLY + {impact_sum}"
                          new_score = impact_sum
                          case_descriptions = "CHECKS,  New violations were introduced"
                      else:
                          #new_score = "CHECK MANUALLY"
                          new_score = 0
                      case_descriptions = "CHECKS, Violation ID not found in old violations"
                       #       new_score =  "CHECK MANUALLY, Old violations: " + str(old_violations)
                      #Baseline Dataset extraction method doesn't include color information therefore it's always not fixed
                      if violation_id == "color-contrast":
                        new_score += oldscore
                      if violation_id in id_check_violations:
                          if not extract_ids_from_html(str(element_html)).isdisjoint(extract_ids_from_html(str(row["filtered_response"]))):
                            new_score += oldscore
                      if violation_id in id_check_violations2:
                          if {item for sublist in extract_attributes_from_html(str(element_html)).values() for item in sublist} & {item for sublist in extract_attributes_from_html(str(row["filtered_response"])).values() for item in sublist}:  # If there is a common element
                            new_score += oldscore
                      if violation_id == "link-in-text-block":
                          if not bool(re.search(r'text-decoration:\s*underline', str(row["filtered_response"])) or
                                  re.search(r'border-bottom:\s*1px solid', str(row["filtered_response"])) or
                                  re.search(r'<u.*?</u>', str(row["filtered_response"]), re.IGNORECASE)
                              ):
                            new_score += oldscore

                      if violation_id == "link-name":
                        new_attributes = extract_attributes_from_html(str(row["filtered_response"]))
                        if not any(new_attributes[attr] for attr in ["alt", "title", "aria-label"] if new_attributes.get(attr) and any(val.strip() for val in new_attributes[attr])):
                          new_score += oldscore
                      if violation_id == "no-autoplay-audio":
                        if "autoplay" in str(row["filtered_response"]).lower():
                          new_score += oldscore
                      if violation_id == "role-img-alt":
                        new_attributes = extract_attributes_from_html(str(row["filtered_response"]))
                        if not any(new_attributes[attr] for attr in ["alt"] if new_attributes.get(attr) and any(val.strip() for val in new_attributes[attr])):
                          new_score += oldscore
                      if violation_id == "scrollable-region-focusable":
                        if 'tabindex="0"' or 'scroll' not in str(row["filtered_response"]).lower():
                          new_score += oldscore
                      if violation_id == "summary-name":
                        has_summary_text = bool(re.search(r'<summary>\s*([^<\s][^<]*?)\s*</summary>', str(row["filtered_response"]), re.IGNORECASE))
                        has_alternative_attrs = bool(re.search(r'aria-labelledby=["\']([^"\']\S+)["\']', str(row["filtered_response"])) or
                                 re.search(r'title=["\']([^"\']\S+)["\']', str(row["filtered_response"])))
                        if  not has_summary_text or has_alternative_attrs:
                          new_score += oldscore

                      if violation_id == "target-size":
                        sizes = [int(size) for size in re.findall(r'(\d+)px',str(row["filtered_response"])) if size.isdigit()]
                        if not all(size >= 24 for size in sizes):
                          new_score += oldscore
                      if violation_id == "aria-braille-equivalent":
                        attributes = extract_attributes_from_html2(str(row["filtered_response"]))
                        if not bool(attributes["aria-brailleroledescription"] or  attributes["aria-roledescription"] or attributes["aria-braillelabel"] or attributes["aria-label"]) :
                          new_score += oldscore
                      if violation_id == "aria-conditional-attr" or violation_id == "th-has-data-cells" or violation_id == "form-field-multiple-labels":
                                old_violations_results = await check_accessibility_from_html(element_html)
                                old_violations = {v["id"] for v in old_violations_results.get("violations", [])}
                                new_violations_results = await check_accessibility_from_html(row["filtered_response"])
                                new_violations = {v["id"]: v["impact"] for v in new_violations_results.get("violations", [])}
                                introduced_violations = set(new_violations.keys()) - old_violations
                                if introduced_violations:
                                          impact_sum = sum(impactScore.get(new_violations[v], 0) for v in introduced_violations)
                                                        #new_score = f"CHECK MANUALLY + {impact_sum}"
                                          new_score = str(impact_sum) + " CHECK MANUALLY"
                                          case_descriptions = "CHECKS,  New violations were introduced"
                                else:
                                                        #new_score = "CHECK MANUALLY"
                                          new_score = str(0) + " CHECK MANUALLY"
                                          case_descriptions = "CHECKS, Violation ID not found in old violations"
                      if violation_id == "video-caption":
                              if "track" not in str(row["filtered_response"]).lower():
                                if "caption" not in str(row["filtered_response"]).lower():
                                      new_score+= oldscore
                      if violation_id == "landmark-no-duplicate-banner":
                          if "banner" in str(row["filtered_response"]).lower():
                              new_score += oldscore
                      if violation_id == "landmark-no-duplicate-contentinfo":
                          if "contentinfo" in str(row["filtered_response"]).lower():
                             new_score += oldscore
                      if violation_id == "landmark-no-duplicate-main":
                          if "main" in str(row["filtered_response"]).lower():
                              new_score += oldscore
                      if violation_id == "frame-focusable-content":
                        if "tabindex=-1" in str(row["filtered_response"]):
                          new_score += oldscore
                      if violation_id == "frame-title":
                        if 'title=""' in str(row["filtered_response"]) or 'title' not in str(row["filtered_response"]):
                          new_score+= oldscore
                      if violation_id =="bypass":
                        if "main" not in str(row["filtered_response"]):
                          new_score += oldscore
                      if violation_id in id_check_violations3:
                        old_violations.add(violation_id)



                      # cases not handeled




              else:
                          # Get new violations using Playwright on the filtered response
                          new_violations_results = await check_accessibility_from_html(row["filtered_response"])
                          new_violations = {v["id"]: v["impact"] for v in new_violations_results.get("violations", [])}
                                  # Debugging: Check extracted new violations
                          #print(f"Extracted New Violations for Row {index}: {new_violations}")
                          if violation_id not in new_violations:  # If original violation was fixed
                              new_score = 0  # No new violations, set to 0
                              introduced_violations = set(new_violations.keys()) - old_violations  # Find new violations introduced
                              if introduced_violations:
                                for new_violation in introduced_violations:
                                    impact = impactScore.get(new_violations[new_violation], 0)  # Get impact score from Playwright results
                                    #print("nado2    "+ str(impact))
                                    new_score += impact  # Add impact score to new score
                                print("Original Violations was fixed, New violations were introduced")
                                case_descriptions= "Original Violations was fixed, New violations were introduced"
                                #print(case_descriptions)
                                print(f"New Violations Introduced for Row {index}: {introduced_violations}")
                              else:
                                print("Original Violations was fixed, No new violations were introduced")
                                case_descriptions = "Original Violations was fixed, No new violations were introduced"
                                #print(case_descriptions)
                          else:
                              new_score = oldscore  # Retain old score
                              #print("nado      "+ str(new_score))
                              #Debugging
                              #print("Original violation was not fixed")
                              introduced_violations = set(new_violations.keys()) - old_violations  # Find new violations introduced
                              for new_violation in introduced_violations:
                                  impact = impactScore.get(new_violations[new_violation], 0)  # Get impact score from Playwright results
                                  #print("nado    "+ str(impact))
                                  new_score += impact  # Add impact score to new score
                              #Debugging
                              #print("New impact Score "+ str(new_score))
                              if introduced_violations:
                                  print("Original violation was not fixed, New violations were introduced")
                                  case_descriptions = "Original violation was not fixed, New violations were introduced"
                                  #print(case_descriptions)
                                  #print(f"New Violations Introduced for Row {index}: {introduced_violations}")
                              else:
                                  print("Original violation was not fixed, No new violations introduced")
                                  case_descriptions = "Original violation was not fixed, No new violations introduced"
                                  #print(case_descriptions)


        #print("-------------------------------------------------------------------")
        #print()
        results.append((violation_id, oldscore, case_descriptions, new_score))  # Append results

    # Convert results to DataFrame
    result_df = pd.DataFrame(results, columns=["violationid", "impact", "Case", "newImpactScore"])

    # Save results to CSV
    result_csv_path = "/content/baseline_two_baseline2_dataset_mistral_accessibility_results_updated.csv"
    result_df.to_csv(result_csv_path, index=False)
    print(f"Updated results saved to: {result_csv_path}")
    print("LLM Hallucination Count: " + str(count_hall))

    #return data_table.DataTable(result_df)


csv_file_path = "/content/results_baseline_two_baseline2_dataset_mistral.csv"

# Run asyncio in a Colab-friendly way
task = asyncio.ensure_future(process_csv(csv_file_path))
await task  # This avoids `asyncio.run()` errors in Colab
