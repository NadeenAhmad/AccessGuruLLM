

!pip install huggingface_hub
!pip install langchain_community
from huggingface_hub import login
login('Hugging_face_token')
!pip install -q -U langchain transformers bitsandbytes accelerate

import torch
from transformers import BitsAndBytesConfig
from langchain import HuggingFacePipeline
from langchain import PromptTemplate, LLMChain
from langchain.memory import ConversationBufferMemory
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

# Configuration for quantization
quantization_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype=torch.float16,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_use_double_quant=True,
)

# Load the model and tokenizer
model_4bit = AutoModelForCausalLM.from_pretrained(
    "mistralai/Mistral-7B-Instruct-v0.1",
    device_map="auto",
    quantization_config=quantization_config,
)
tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-Instruct-v0.1")

# Create the pipeline
pipeline_inst = pipeline(
    "text-generation",
    model=model_4bit,
    tokenizer=tokenizer,
    use_cache=True,
    device_map="auto",
    max_length=128000,
    do_sample=True,
    top_k=5,
    num_return_sequences=1,
    eos_token_id=tokenizer.eos_token_id,
    pad_token_id=tokenizer.eos_token_id,
)
# Wrap the pipeline in LangChain's HuggingFacePipeline
llm = HuggingFacePipeline(pipeline=pipeline_inst)

"""# Generate Metacognitive Prompts"""

#extract code from response, confidence, explanation
#calculate new impact score of extracted code
#save in csv
#corrective reprompting
#extract code from response, confidence, explanation
#calculate new impact score of extracted code
#save in csv


#gpt 4

# baseline dataset
# mistral
# gpt 4

!pip install mistralai
import os
from mistralai import Mistral

#model = "mistral-large-latest"
#client = Mistral(api_key = "YOUR_API_KEY")

import json
import pandas as pd

def get_guidelines(violationType):
  guide = []
  json_file_path = '/content/mapping_dict_file.json'
  # Open and read the JSON file
  with open(json_file_path, 'r') as file:
     data = json.load(file)
  guidelineNames=data[violationType]
  guidelines= pd.read_csv('/content/WCAGGuidelines.csv')
  for x in guidelineNames:
      guide.append(str(x+":" +guidelines[guidelines['guideId'] == x]['description'].values[0]))
  return guide


#get_guidelines("image-alt-not-descriptive")
def get_category(c):
    categories = {
        "Syntax": """These occur when HTML code lacks essential structural elements or attributes required for accessibility, such as missing alt attributes or improper use of heading tags and table elements.
    To correct this type of web accessibility violation, expertise in HTML coding is required.""",
        "Layout": """These relate to design and visual organization issues, such as insufficient color contrast or poor font sizing, that reduce readability or usability for visually impaired users. Fixes must ensure accessibility without negatively affecting users without impairments.
    To correct this type of web accessibility violation, knowledge of web design principles and front-end coding is required.""",
        "Semantic": """These involve the misuse or absence of meaningful content or attributes, such as vague alt text or improper use of semantic elements like <header> or <section>.
    To correct this type of web accessibility violation, expertise in HTML semantics and coding is required.""",
    }
    return categories.get(c, "No description available for this category.")

def get_category_1(violationType):
  category = ""
  categories= pd.read_csv('/content/violation_taxonomy.csv')
    # Ensure column names are correct
  if 'violationnumberID' not in categories.columns or 'Category' not in categories.columns:
        raise ValueError("CSV file does not contain the expected columns.")

    # Search for the violation name
  category = categories.loc[categories['violationnumberID'] == violationType, 'Category']

    # Return the category if found, else return a not found message
  return category.iloc[0] if not category.empty else "Violation not found"

# Load CSV file
df = pd.read_csv("/content/Our_dataset_Final_Final.csv")

# Process each row
#for index, row in df.iterrows():
for index, row in df.head(2).iterrows():
    category = row['category']
    category_description = get_category(category)
    violationType = row['violationnumberID']
    guideline = get_guidelines(violationType)
    violationDescription = row['description']
    impact = row['impact']
    URL = row['webURL']
    HTMLElement = row['affectedHTMLElement(s)']
#baseline dataset column names
#for index, row in df.head(2).iterrows():
 #   category = get_category_1(row['id'])
  #  category_description = get_category(category)
  #  violationType = row['id']
   # guideline = get_guidelines(violationType)
   # violationDescription = row['description']
   # impact = row['impact']
   # URL = row['webURL']
   # HTMLElement = row['html']
    print(f"Category: {category}")
    print(f"Category Description: {category_description}")
    print(f"Violation Type: {violationType}")
    print(f"Guideline: {guideline}")
    print(f"Violation Description: {violationDescription}")
    print(f"Impact: {impact}")
    print(f"URL: {URL}")
    print(f"Affected HTML Element(s): {HTMLElement}")

import requests
import time

# Mistral AI API Setup
API_KEY = "YOUR_API_KEY"  # Replace with your actual API key
MISTRAL_API_URL = "https://api.mistral.ai/v1/chat/completions"

def reset_chat_history():
    """Resets chat history, keeping only the system prompt."""
    global chat_history
    chat_history = [
        {"role": "system", "content": "You are a Web accessibility expert with a strong proficiency in HTML and a deep commitment to fixing Web accessibility violations. You are familiar with different types of disabilities and user needs. You are familiar with assistive technologies such as screen readers and understand how they interact with the Web. You specialize in analyzing Web pages, identifying issues, and providing immediate, corrected HTML code solutions that meet WCAG 2.1 standards. Your expertise includes resolving problems like missing or improper Alt text, insufficient heading structure, non-semantic elements, inaccessible forms, and color contrast issues. You are adept at transforming flawed code into compliant, clean HTML that works seamlessly with assistive technologies, ensuring that Websites are fully navigable by keyboard and readable by screen readers. You provide the corrected code necessary for immediate implementation, ensuring that Websites are not only compliant but truly inclusive for users with disabilities. Your mission is to ensure that every Website and Web application is accessible to all users by providing expertly corrected HTML, making the Web a more inclusive space. "
                                  "You reflect on your own answers, assess their accuracy, and provide corrections only when necessary."}

    ]


#def send_prompt(prompt):
#    """Send a structured prompt to the model while maintaining chat history."""

    # Append user prompt
 #   chat_history.append({"role": "user", "content": prompt})

    # Make an API request to Mistral AI
  #  response = requests.post(
   #     MISTRAL_API_URL,
    #    headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"},
     #   json={"model": "open-mistral-7b", "messages": chat_history, "max_tokens": 128000},

    #)

    # Process response
    #if response.status_code == 200:
     #   chat_response = response.json()["choices"][0]["message"]["content"]
      #  chat_history.append({"role": "assistant", "content": chat_response})
      #  return chat_response
   # else:
       # return f"Error: {response.status_code}, {response.text}"



def send_prompt(prompt, retries=3, initial_wait=10):
    """Send a structured prompt to the model while handling rate limits."""
    chat_history.append({"role": "user", "content": prompt})

    for attempt in range(retries):
        try:
            response = requests.post(
                MISTRAL_API_URL,
                headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"},
                json={"model": "open-mistral-7b", "messages": chat_history, "max_tokens": 128000},
            )

            # If successful, process and return response
            if response.status_code == 200:
                chat_response = response.json()["choices"][0]["message"]["content"]
                chat_history.append({"role": "assistant", "content": chat_response})
                return chat_response

            # Handle rate limit errors (429)
            elif response.status_code == 429:
                wait_time = initial_wait * (2 ** attempt)  # Exponential backoff
                print(f"Rate limit exceeded. Waiting {wait_time} seconds before retrying... (Attempt {attempt+1}/{retries})")
                time.sleep(wait_time)
                continue  # Retry request

            # Handle other errors
            else:
                return f"Error: {response.status_code}, {response.text}"

        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}. Retrying... (Attempt {attempt+1}/{retries})")
            time.sleep(initial_wait * (2 ** attempt))  # Exponential backoff

    return "Error: Exceeded retry attempts due to rate limiting."



# Function to perform metacognitive prompting step-by-step
def analyze_web_accessibility_violation(category, category_description, violationType, violationDescription, impact, URL, HTMLElement, guideline):
    # Initialize chat history
    reset_chat_history()
    chat_history = [
    {"role": "system", "content": "You are a Web accessibility expert with a strong proficiency in HTML and a deep commitment to fixing Web accessibility violations. You are familiar with different types of disabilities and user needs. You are familiar with assistive technologies such as screen readers and understand how they interact with the Web. You specialize in analyzing Web pages, identifying issues, and providing immediate, corrected HTML code solutions that meet WCAG 2.1 standards. Your expertise includes resolving problems like missing or improper Alt text, insufficient heading structure, non-semantic elements, inaccessible forms, and color contrast issues. You are adept at transforming flawed code into compliant, clean HTML that works seamlessly with assistive technologies, ensuring that Websites are fully navigable by keyboard and readable by screen readers. You provide the corrected code necessary for immediate implementation, ensuring that Websites are not only compliant but truly inclusive for users with disabilities. Your mission is to ensure that every Website and Web application is accessible to all users by providing expertly corrected HTML, making the Web a more inclusive space. "
                                  "You reflect on your own answers, assess their accuracy, and provide corrections only when necessary."}
]
    """Executes the metacognitive evaluation workflow for web accessibility violations."""


    # Step 1: Comprehension & Clarification
    prompt_comprehension_clarification = f"""
    Clarify your understanding of the following web accessibility violation:
    Violation type: "{violationType}",
    Violation description: "{violationDescription}",
    Impact: "{impact}" (Impact is a rating determined by the severity of the violation, indicating the extent to which it hinders user interaction with the Web content. The scale is [cosmetic, minor, moderate, serious, critical]).
    Web page URL: "{URL}"
    Affected HTML Element(s) by the Violation: "{HTMLElement}"
    """
    print("\n### Step 1: Comprehension Clarification ###")
    print(send_prompt(prompt_comprehension_clarification))

    # Step 2: Preliminary Judgment & Correction
    prompt_preliminary_judgment = f"""
    {violationType} is  {category} Web accessibility violation,  {category_description}.
    Based on your understanding, provide a preliminary correction for the web accessibility violation based on the following WCAG guideline(s): "{guideline}".
    Ensure you generate the complete corrected code, not just a snippet.
    """
    print("\n### Step 2: Preliminary Correction ###")
    print(send_prompt(prompt_preliminary_judgment))

    # Step 3: Critical Evaluation of the Correction
    prompt_critical_evaluation = """
    Critically assess your preliminary correction, make sure to correct the initial web accessibility violation without introducing new web accessibility violations. Only make corrections if the previous answer is incorrect. Return ONLY the fixed HTML code with no extra explanations.
    """
    print("\n### Step 3: Critical Evaluation ###")
    print(send_prompt(prompt_critical_evaluation))

    # Step 4: Decision Confirmation
    prompt_decision_confirmation = """
    Confirm your final decision on whether the correction is accurate or not and provide very short reasoning for your decision.
    Only suggest further corrections if the initial response contains errors. Enclose your corrected HTML code to replace the initial code with violations between these two marker strings: "###albidaya###" as first line and "###alnihaya###" as last line.
    Make sure:
    - The output is complete, valid HTML.
    - The text rendered on the Web page remains unchanged.
    - Only accessibility-related attributes and tags are modified.

    """
    print("\n### Step 4: Decision Confirmation ###")
    response = send_prompt(prompt_decision_confirmation)
    print(response)


    # Step 5: Confidence Level Evaluation
    prompt_confidence_level = """
    Evaluate your confidence (0-100%) in your correction, enclose your confidence score between these two marker strings: "###albidaya###" as first line and "###alnihaya###" as last line.
    Provide a very short explanation for this confidence level, enclose your explanation between these two marker strings: "###albidaya2###" as first line and "###alnihaya2###" as last line.
    """
    print("\n### Step 5: Confidence Level Evaluation ###")
    confidence = send_prompt(prompt_confidence_level)
    print(confidence)
    reset_chat_history()

    return response, confidence
# Example Usage
#analyze_web_accessibility_violation(
 #   category="Color Contrast",
  #  category_description="The text does not have sufficient contrast against its background.",
  #  violationType="Low Contrast",
  #  violationDescription="The color contrast ratio between text and background is below the minimum threshold required by WCAG 2.1.",
   # impact="serious",
   # URL="https://example.com",
   # HTMLElement="<p style='color:lightgray;'>Low contrast text</p>",
   # guideline="WCAG 2.1 - 1.4.3 Contrast (Minimum)"
#)


#for index, row in df.iterrows():
#for index, row in df.head(2).iterrows():
 #   category = row['category']
  #  category_description = get_category(category)
   # violationType = row['violationnumberID']
   # guideline = get_guidelines(violationType)
   # violationDescription = row['description']
   # impact = row['impact']
   # URL = row['webURL']
   # HTMLElement = row['affectedHTMLElement(s)']

  #  analyze_web_accessibility_violation(category, category_description, violationType, violationDescription, impact, URL, HTMLElement, guideline)

# Add new columns to store responses if they do not exist
if "MetaCognitive_Response" not in df.columns:
    df["MetaCognitive_Response"] = ""
if "Confidence_Score" not in df.columns:
    df["Confidence_Score_Explanation"] = ""


for index, row in df.head(2).iterrows():
#for index, row in df.iterrows():
    category = get_category_1(row['violationnumberID'])
    category_description = get_category(category)
    violationType = row['violationnumberID']
    guideline = get_guidelines(violationType)
    violationDescription = row['description']
    impact = row['impact']
    URL = row['webURL']
    HTMLElement = row['affectedHTMLElement(s)']
    response, confidence = analyze_web_accessibility_violation(
        category, category_description, violationType, violationDescription, impact, URL, HTMLElement, guideline
    )

    df.at[index, "MetaCognitive_Response"] = response
    df.at[index, "Confidence_Score_Explanation"] = confidence


    # Save to CSV after each iteration to prevent data loss in case of runtime disconnection
    df.to_csv("/content/our_dataset_MetaCognitive_Response_mistral.csv", index=False)

"""1 hour --> baseline dataset"""

import requests
import time

# Mistral AI API Setup
API_KEY = "YOUR_API_KEY"  # Replace with your actual API key
MISTRAL_API_URL = "https://api.mistral.ai/v1/chat/completions"

def reset_chat_history():
    """Resets chat history, keeping only the system prompt."""
    global chat_history
    chat_history = [
        {"role": "system", "content": "You are a Web accessibility expert with a strong proficiency in HTML and a deep commitment to fixing Web accessibility violations. You are familiar with different types of disabilities and user needs. You are familiar with assistive technologies such as screen readers and understand how they interact with the Web. You specialize in analyzing Web pages, identifying issues, and providing immediate, corrected HTML code solutions that meet WCAG 2.1 standards. Your expertise includes resolving problems like missing or improper Alt text, insufficient heading structure, non-semantic elements, inaccessible forms, and color contrast issues. You are adept at transforming flawed code into compliant, clean HTML that works seamlessly with assistive technologies, ensuring that Websites are fully navigable by keyboard and readable by screen readers. You provide the corrected code necessary for immediate implementation, ensuring that Websites are not only compliant but truly inclusive for users with disabilities. Your mission is to ensure that every Website and Web application is accessible to all users by providing expertly corrected HTML, making the Web a more inclusive space. "
                                  "You reflect on your own answers, assess their accuracy, and provide corrections only when necessary."}

    ]


#def send_prompt(prompt):
#    """Send a structured prompt to the model while maintaining chat history."""

    # Append user prompt
 #   chat_history.append({"role": "user", "content": prompt})

    # Make an API request to Mistral AI
  #  response = requests.post(
   #     MISTRAL_API_URL,
    #    headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"},
     #   json={"model": "open-mistral-7b", "messages": chat_history, "max_tokens": 128000},

    #)

    # Process response
    #if response.status_code == 200:
     #   chat_response = response.json()["choices"][0]["message"]["content"]
      #  chat_history.append({"role": "assistant", "content": chat_response})
      #  return chat_response
   # else:
       # return f"Error: {response.status_code}, {response.text}"



def send_prompt(prompt, retries=3, initial_wait=10):
    """Send a structured prompt to the model while handling rate limits."""
    chat_history.append({"role": "user", "content": prompt})

    for attempt in range(retries):
        try:
            response = requests.post(
                MISTRAL_API_URL,
                headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"},
                json={"model": "open-mistral-7b", "messages": chat_history, "max_tokens": 128000},
            )

            # If successful, process and return response
            if response.status_code == 200:
                chat_response = response.json()["choices"][0]["message"]["content"]
                chat_history.append({"role": "assistant", "content": chat_response})
                return chat_response

            # Handle rate limit errors (429)
            elif response.status_code == 429:
                wait_time = initial_wait * (2 ** attempt)  # Exponential backoff
                print(f"Rate limit exceeded. Waiting {wait_time} seconds before retrying... (Attempt {attempt+1}/{retries})")
                time.sleep(wait_time)
                continue  # Retry request

            # Handle other errors
            else:
                return f"Error: {response.status_code}, {response.text}"

        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}. Retrying... (Attempt {attempt+1}/{retries})")
            time.sleep(initial_wait * (2 ** attempt))  # Exponential backoff

    return "Error: Exceeded retry attempts due to rate limiting."



# Function to perform metacognitive prompting step-by-step
def analyze_web_accessibility_violation(category, category_description, violationType, violationDescription, impact, URL, HTMLElement, guideline):
    # Initialize chat history
    reset_chat_history()
    chat_history = [
    {"role": "system", "content": "You are a Web accessibility expert with a strong proficiency in HTML and a deep commitment to fixing Web accessibility violations. You are familiar with different types of disabilities and user needs. You are familiar with assistive technologies such as screen readers and understand how they interact with the Web. You specialize in analyzing Web pages, identifying issues, and providing immediate, corrected HTML code solutions that meet WCAG 2.1 standards. Your expertise includes resolving problems like missing or improper Alt text, insufficient heading structure, non-semantic elements, inaccessible forms, and color contrast issues. You are adept at transforming flawed code into compliant, clean HTML that works seamlessly with assistive technologies, ensuring that Websites are fully navigable by keyboard and readable by screen readers. You provide the corrected code necessary for immediate implementation, ensuring that Websites are not only compliant but truly inclusive for users with disabilities. Your mission is to ensure that every Website and Web application is accessible to all users by providing expertly corrected HTML, making the Web a more inclusive space. "
                                  "You reflect on your own answers, assess their accuracy, and provide corrections only when necessary."}
]
    """Executes the metacognitive evaluation workflow for web accessibility violations."""


    # Step 1: Comprehension & Clarification
    prompt_comprehension_clarification = f"""
    Clarify your understanding of the following web accessibility violation:
    Violation type: "{violationType}",
    Violation description: "{violationDescription}",
    Impact: "{impact}" (Impact is a rating determined by the severity of the violation, indicating the extent to which it hinders user interaction with the Web content. The scale is [cosmetic, minor, moderate, serious, critical]).
    Web page URL: "{URL}"
    Affected HTML Element(s) by the Violation: "{HTMLElement}"
    """
    print("\n### Step 1: Comprehension Clarification ###")
    print(send_prompt(prompt_comprehension_clarification))

    # Step 2: Preliminary Judgment & Correction
    prompt_preliminary_judgment = f"""
    {violationType} is  {category} Web accessibility violation,  {category_description}.
    Based on your understanding, provide a preliminary correction for the web accessibility violation based on the following WCAG guideline(s): "{guideline}".
    Ensure you generate the complete corrected code, not just a snippet.
    """
    print("\n### Step 2: Preliminary Correction ###")
    print(send_prompt(prompt_preliminary_judgment))

    # Step 3: Critical Evaluation of the Correction
    prompt_critical_evaluation = """
    Critically assess your preliminary correction, make sure to correct the initial web accessibility violation without introducing new web accessibility violations. Only make corrections if the previous answer is incorrect. Return ONLY the fixed HTML code with no extra explanations.
    """
    print("\n### Step 3: Critical Evaluation ###")
    print(send_prompt(prompt_critical_evaluation))

    # Step 4: Decision Confirmation
    prompt_decision_confirmation = """
    Confirm your final decision on whether the correction is accurate or not and provide very short reasoning for your decision.
    Only suggest further corrections if the initial response contains errors. Enclose your corrected HTML code to replace the initial code with violations between these two marker strings: "###albidaya###" as first line and "###alnihaya###" as last line.
    Make sure:
    - The output is complete, valid HTML.
    - The text rendered on the Web page remains unchanged.
    - Only accessibility-related attributes and tags are modified.

    """
    print("\n### Step 4: Decision Confirmation ###")
    response = send_prompt(prompt_decision_confirmation)
    print(response)


    # Step 5: Confidence Level Evaluation
    prompt_confidence_level = """
    Evaluate your confidence (0-100%) in your correction, enclose your confidence score between these two marker strings: "###albidaya###" as first line and "###alnihaya###" as last line.
    Provide a very short explanation for this confidence level, enclose your explanation between these two marker strings: "###albidaya2###" as first line and "###alnihaya2###" as last line.
    """
    print("\n### Step 5: Confidence Level Evaluation ###")
    confidence = send_prompt(prompt_confidence_level)
    print(confidence)
    reset_chat_history()

    return response, confidence
# Example Usage
#analyze_web_accessibility_violation(
 #   category="Color Contrast",
  #  category_description="The text does not have sufficient contrast against its background.",
  #  violationType="Low Contrast",
  #  violationDescription="The color contrast ratio between text and background is below the minimum threshold required by WCAG 2.1.",
   # impact="serious",
   # URL="https://example.com",
   # HTMLElement="<p style='color:lightgray;'>Low contrast text</p>",
   # guideline="WCAG 2.1 - 1.4.3 Contrast (Minimum)"
#)


#for index, row in df.iterrows():
#for index, row in df.head(2).iterrows():
 #   category = row['category']
  #  category_description = get_category(category)
   # violationType = row['violationnumberID']
   # guideline = get_guidelines(violationType)
   # violationDescription = row['description']
   # impact = row['impact']
   # URL = row['webURL']
   # HTMLElement = row['affectedHTMLElement(s)']

  #  analyze_web_accessibility_violation(category, category_description, violationType, violationDescription, impact, URL, HTMLElement, guideline)

# Add new columns to store responses if they do not exist
if "MetaCognitive_Response" not in df.columns:
    df["MetaCognitive_Response"] = ""
if "Confidence_Score" not in df.columns:
    df["Confidence_Score_Explanation"] = ""


#for index, row in df.head(2).iterrows():
for index, row in df.iterrows():
    category = get_category_1(row['violationnumberID'])
    category_description = get_category(category)
    violationType = row['violationnumberID']
    guideline = get_guidelines(violationType)
    violationDescription = row['description']
    impact = row['impact']
    URL = row['webURL']
    HTMLElement = row['affectedHTMLElement(s)']
    response, confidence = analyze_web_accessibility_violation(
        category, category_description, violationType, violationDescription, impact, URL, HTMLElement, guideline
    )

    df.at[index, "MetaCognitive_Response"] = response
    df.at[index, "Confidence_Score_Explanation"] = confidence


    # Save to CSV after each iteration to prevent data loss in case of runtime disconnection
    df.to_csv("/content/our_dataset_MetaCognitive_Response_mistral.csv", index=False)

import requests
import time

# Mistral AI API Setup
API_KEY = "YOUR_API_KEY"  # Replace with your actual API key
MISTRAL_API_URL = "https://api.mistral.ai/v1/chat/completions"

def reset_chat_history():
    """Resets chat history, keeping only the system prompt."""
    global chat_history
    chat_history = [
        {"role": "system", "content": "You are a Web accessibility expert with a strong proficiency in HTML and a deep commitment to fixing Web accessibility violations. You are familiar with different types of disabilities and user needs. You are familiar with assistive technologies such as screen readers and understand how they interact with the Web. You specialize in analyzing Web pages, identifying issues, and providing immediate, corrected HTML code solutions that meet WCAG 2.1 standards. Your expertise includes resolving problems like missing or improper Alt text, insufficient heading structure, non-semantic elements, inaccessible forms, and color contrast issues. You are adept at transforming flawed code into compliant, clean HTML that works seamlessly with assistive technologies, ensuring that Websites are fully navigable by keyboard and readable by screen readers. You provide the corrected code necessary for immediate implementation, ensuring that Websites are not only compliant but truly inclusive for users with disabilities. Your mission is to ensure that every Website and Web application is accessible to all users by providing expertly corrected HTML, making the Web a more inclusive space. "
                                  "You reflect on your own answers, assess their accuracy, and provide corrections only when necessary."}

    ]


#def send_prompt(prompt):
#    """Send a structured prompt to the model while maintaining chat history."""

    # Append user prompt
 #   chat_history.append({"role": "user", "content": prompt})

    # Make an API request to Mistral AI
  #  response = requests.post(
   #     MISTRAL_API_URL,
    #    headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"},
     #   json={"model": "open-mistral-7b", "messages": chat_history, "max_tokens": 128000},

    #)

    # Process response
    #if response.status_code == 200:
     #   chat_response = response.json()["choices"][0]["message"]["content"]
      #  chat_history.append({"role": "assistant", "content": chat_response})
      #  return chat_response
   # else:
       # return f"Error: {response.status_code}, {response.text}"



def send_prompt(prompt, retries=3, initial_wait=10):
    """Send a structured prompt to the model while handling rate limits."""
    chat_history.append({"role": "user", "content": prompt})

    for attempt in range(retries):
        try:
            response = requests.post(
                MISTRAL_API_URL,
                headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"},
                json={"model": "open-mistral-7b", "messages": chat_history, "max_tokens": 128000},
            )

            # If successful, process and return response
            if response.status_code == 200:
                chat_response = response.json()["choices"][0]["message"]["content"]
                chat_history.append({"role": "assistant", "content": chat_response})
                return chat_response

            # Handle rate limit errors (429)
            elif response.status_code == 429:
                wait_time = initial_wait * (2 ** attempt)  # Exponential backoff
                print(f"Rate limit exceeded. Waiting {wait_time} seconds before retrying... (Attempt {attempt+1}/{retries})")
                time.sleep(wait_time)
                continue  # Retry request

            # Handle other errors
            else:
                return f"Error: {response.status_code}, {response.text}"

        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}. Retrying... (Attempt {attempt+1}/{retries})")
            time.sleep(initial_wait * (2 ** attempt))  # Exponential backoff

    return "Error: Exceeded retry attempts due to rate limiting."



# Function to perform metacognitive prompting step-by-step
def analyze_web_accessibility_violation(category, category_description, violationType, violationDescription, impact, URL, HTMLElement, guideline):
    # Initialize chat history
    reset_chat_history()
    chat_history = [
    {"role": "system", "content": "You are a Web accessibility expert with a strong proficiency in HTML and a deep commitment to fixing Web accessibility violations. You are familiar with different types of disabilities and user needs. You are familiar with assistive technologies such as screen readers and understand how they interact with the Web. You specialize in analyzing Web pages, identifying issues, and providing immediate, corrected HTML code solutions that meet WCAG 2.1 standards. Your expertise includes resolving problems like missing or improper Alt text, insufficient heading structure, non-semantic elements, inaccessible forms, and color contrast issues. You are adept at transforming flawed code into compliant, clean HTML that works seamlessly with assistive technologies, ensuring that Websites are fully navigable by keyboard and readable by screen readers. You provide the corrected code necessary for immediate implementation, ensuring that Websites are not only compliant but truly inclusive for users with disabilities. Your mission is to ensure that every Website and Web application is accessible to all users by providing expertly corrected HTML, making the Web a more inclusive space. "
                                  "You reflect on your own answers, assess their accuracy, and provide corrections only when necessary."}
]
    """Executes the metacognitive evaluation workflow for web accessibility violations."""


    # Step 1: Comprehension & Clarification
    prompt_comprehension_clarification = f"""
    Clarify your understanding of the following web accessibility violation:
    Violation type: "{violationType}",
    Violation description: "{violationDescription}",
    Impact: "{impact}" (Impact is a rating determined by the severity of the violation, indicating the extent to which it hinders user interaction with the Web content. The scale is [cosmetic, minor, moderate, serious, critical]).
    Web page URL: "{URL}"
    Affected HTML Element(s) by the Violation: "{HTMLElement}"
    """
    print("\n### Step 1: Comprehension Clarification ###")
    print(send_prompt(prompt_comprehension_clarification))

    # Step 2: Preliminary Judgment & Correction
    prompt_preliminary_judgment = f"""
    {violationType} is  {category} Web accessibility violation,  {category_description}.
    Based on your understanding, provide a preliminary correction for the web accessibility violation based on the following WCAG guideline(s): "{guideline}".
    Ensure you generate the complete corrected code, not just a snippet.
    """
    print("\n### Step 2: Preliminary Correction ###")
    print(send_prompt(prompt_preliminary_judgment))

    # Step 3: Critical Evaluation of the Correction
    prompt_critical_evaluation = """
    Critically assess your preliminary correction, make sure to correct the initial web accessibility violation without introducing new web accessibility violations. Only make corrections if the previous answer is incorrect. Return ONLY the fixed HTML code with no extra explanations.
    """
    print("\n### Step 3: Critical Evaluation ###")
    print(send_prompt(prompt_critical_evaluation))

    # Step 4: Decision Confirmation
    prompt_decision_confirmation = """
    Confirm your final decision on whether the correction is accurate or not and provide very short reasoning for your decision.
    Only suggest further corrections if the initial response contains errors. Enclose your corrected HTML code to replace the initial code with violations between these two marker strings: "###albidaya###" as first line and "###alnihaya###" as last line.
    Make sure:
    - The output is complete, valid HTML.
    - The text rendered on the Web page remains unchanged.
    - Only accessibility-related attributes and tags are modified.

    """
    print("\n### Step 4: Decision Confirmation ###")
    response = send_prompt(prompt_decision_confirmation)
    print(response)


    # Step 5: Confidence Level Evaluation
    prompt_confidence_level = """
    Evaluate your confidence (0-100%) in your correction, enclose your confidence score between these two marker strings: "###albidaya###" as first line and "###alnihaya###" as last line.
    Provide a very short explanation for this confidence level, enclose your explanation between these two marker strings: "###albidaya2###" as first line and "###alnihaya2###" as last line.
    """
    print("\n### Step 5: Confidence Level Evaluation ###")
    confidence = send_prompt(prompt_confidence_level)
    print(confidence)
    reset_chat_history()

    return response, confidence
# Example Usage
#analyze_web_accessibility_violation(
 #   category="Color Contrast",
  #  category_description="The text does not have sufficient contrast against its background.",
  #  violationType="Low Contrast",
  #  violationDescription="The color contrast ratio between text and background is below the minimum threshold required by WCAG 2.1.",
   # impact="serious",
   # URL="https://example.com",
   # HTMLElement="<p style='color:lightgray;'>Low contrast text</p>",
   # guideline="WCAG 2.1 - 1.4.3 Contrast (Minimum)"
#)


#for index, row in df.iterrows():
#for index, row in df.head(2).iterrows():
 #   category = row['category']
  #  category_description = get_category(category)
   # violationType = row['violationnumberID']
   # guideline = get_guidelines(violationType)
   # violationDescription = row['description']
   # impact = row['impact']
   # URL = row['webURL']
   # HTMLElement = row['affectedHTMLElement(s)']

  #  analyze_web_accessibility_violation(category, category_description, violationType, violationDescription, impact, URL, HTMLElement, guideline)

# Add new columns to store responses if they do not exist
if "MetaCognitive_Response" not in df.columns:
    df["MetaCognitive_Response"] = ""
if "Confidence_Score" not in df.columns:
    df["Confidence_Score_Explanation"] = ""


# Define the starting row index
start_index = 195  # Change this to the desired starting row

# Iterate over the dataset starting from the specified index
for index, row in df.iloc[start_index:].iterrows():
    category = get_category_1(row['violationnumberID'])
    category_description = get_category(category)
    violationType = row['violationnumberID']
    guideline = get_guidelines(violationType)
    violationDescription = row['description']
    impact = row['impact']
    URL = row['webURL']
    HTMLElement = row['affectedHTMLElement(s)']
    response, confidence = analyze_web_accessibility_violation(
        category, category_description, violationType, violationDescription, impact, URL, HTMLElement, guideline
    )

    df.at[index, "MetaCognitive_Response"] = response
    df.at[index, "Confidence_Score_Explanation"] = confidence


    # Save to CSV after each iteration to prevent data loss in case of runtime disconnection
    df.to_csv("/content/our_dataset_MetaCognitive_Response_mistral.csv", index=False)

print("hello")

"""## Utils"""

!pip install playwright google-colab nest_asyncio
!playwright install

import asyncio
import pandas as pd
from playwright.async_api import async_playwright
from google.colab import data_table

async def check_accessibility_from_html(html_content):
    """Launch Playwright and check accessibility violations for the given HTML snippet."""
    try:
        async with async_playwright() as p:
            # Launch browser in headless mode
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()

            # Set HTML content directly instead of using temp files
            await page.set_content(html_content)

            # Inject axe-core for accessibility testing
            await page.add_script_tag(url="https://cdn.jsdelivr.net/npm/axe-core@4.4.1/axe.min.js")

            # Run axe accessibility checks
            results = await page.evaluate("""
            async () => {
                return await axe.run(document, {
                    runOnly: {
                        type: 'tag',
                        values: ['wcag2a', 'cat.sensory-and-visual-cues', 'wcag2aa', 'wcag144', 'ACT']
                    }
                });
            }
            """)

            # Close the browser
            await browser.close()

            return results
    except Exception as e:
        return {"error": str(e)}

async def process_csv(file_path):
    """Process the CSV file and calculate violation scores."""
    df = pd.read_csv(file_path)

    if "affectedElement(s)" not in df.columns or "violationid" not in df.columns:
        print("Error: Required columns not found in the CSV file.")
        return

    results = []

    for index, row in df.iterrows():
        element_html = row["affectedElement(s)"]
        violation_id = row["violationnumberID"]
        oldscore= row["initialImpactScore"]

        if pd.isna(element_html):
            results.append((violation_id, element_html,oldscore, "N/A"))
            continue

        violations = await check_accessibility_from_html(element_html)

        if "error" in violations:
            score = "Error"
        else:
            score = len(violations.get('violations', []))  # Count number of violations

        results.append(( violation_id, element_html,oldscore, score))

    # Convert to DataFrame
    result_df = pd.DataFrame(results, columns=["violationnumberID","affectedElement(s)", "initialImpactScore","Violation Score"])

    # Display results in Colab
    data_table.DataTable(result_df)  # Display interactive table

    return result_df

# Replace with actual CSV file path in Colab
csv_file_path = "/content/Our_dataset.csv"

# Get the current event loop if it exists, otherwise create a new one
#try:
    #loop = asyncio.get_running_loop()
#except RuntimeError:
    #loop = asyncio.new_event_loop()
#asyncio.set_event_loop(loop)

# Use asyncio.run to execute the coroutine safely in Colab
asyncio.run(process_csv(csv_file_path)) # Instead of `loop.run_until_complete`, which might conflict with Colab's existing loop

import nest_asyncio
import asyncio
import pandas as pd
from playwright.async_api import async_playwright
from google.colab import data_table  # Colab-friendly table display

# Apply nest_asyncio to allow nested event loops in Colab
nest_asyncio.apply()

async def check_accessibility_from_html(html_content):
    """Launch Playwright and check accessibility violations for a given HTML snippet."""
    try:
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)  # Headless mode for Colab
            page = await browser.new_page()

            # Set HTML content directly
            await page.set_content(html_content)

            # Inject axe-core for accessibility testing
            await page.add_script_tag(url="https://cdn.jsdelivr.net/npm/axe-core@4.4.1/axe.min.js")

            # Run axe accessibility checks
            results = await page.evaluate("""
            async () => {
                return await axe.run(document, {
                    runOnly: {
                        type: 'tag',
                        values: ['wcag2a', 'cat.sensory-and-visual-cues', 'wcag2aa', 'wcag144', 'ACT']
                    }
                });
            }
            """)

            # Close the browser
            await browser.close()

            return results
    except Exception as e:
        return {"error": str(e)}

async def process_csv(file_path):
    """Process the CSV file and calculate violation scores."""
    df = pd.read_csv(file_path)

    if "affectedHTMLElement(s)" not in df.columns or "violationnumberID" not in df.columns:
        print("Error: Required columns not found in the CSV file.")
        return

    results = []

    for index, row in df.iterrows():
        element_html = row["affectedHTMLElement(s)"]
        violation_id = row["violationnumberID"]
        oldscore = row["initialImpactScore"]

        if pd.isna(element_html):
            results.append((element_html, violation_id, oldscore, "N/A"))
            continue

        violations = await check_accessibility_from_html(element_html)

        if "error" in violations:
            score = "Error"
        else:
            violation_list = violations.get('violations', [])
            num_violations = len(violation_list)
            details = []

            for violation in violation_list:
                description = violation.get("description", "No description")
                impact = violation.get("impact", "Unknown impact")
                details.append(f"{description} (Impact: {impact})")

            score = f"Violations: {num_violations}\n" + "\n".join(details)

        results.append((element_html, violation_id, oldscore, score))

    # Convert to DataFrame
    result_df = pd.DataFrame(results, columns=["affectedElement(s)", "violationid", "initialImpactScore", "Violation Score"])

    # Save results to CSV
    result_csv_path = "/content/accessibility_results.csv"
    result_df.to_csv(result_csv_path, index=False)
    print(f"Results saved to: {result_csv_path}")

    # Display results interactively in Colab
    return data_table.DataTable(result_df)

# Replace with actual CSV file path in Colab
csv_file_path = "/content/Our_dataset.csv"

# Run asyncio in a Colab-friendly way
task = asyncio.ensure_future(process_csv(csv_file_path))
await task  # This avoids `asyncio.run()` errors in Colab

# Load the CSV file into a DataFrame
df = pd.read_csv('/content/Our_dataset_Final_Final.csv')

# Check if 'violationid' column exists
if "violationnumberID" in df.columns:
    # Get unique violation IDs
    unique_violation_ids = df["violationnumberID"].unique()

    # Print unique violation IDs
    print("Unique violation IDs:")
    for violation_id in unique_violation_ids:
        print(violation_id)
else:
    print("Error: 'violationid' column not found in the CSV file.")

import json

# Load the JSON file
with open("/content/mapping_dict_file.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Extract unique keys
unique_keys = set(data.keys())

# Print unique keys
print("Unique Keys in the JSON file:")
for key in sorted(unique_keys):
    print(key)

print(type(unique_keys))
print(type(set(unique_violation_ids )))

set(unique_violation_ids ) - unique_keys

unique_keys - set(unique_violation_ids )

import pandas as pd

# Load the CSV file
file_path = "/content/baseline_dataset.csv"  # Change this to your CSV file path
df = pd.read_csv(file_path)

# Specify the column name
column_name = "id"  # Change this to your column name

# Print unique values in the specified column
if column_name in df.columns:
    unique_values = df[column_name].unique()
    print(f"Unique values in '{column_name}':")
    print(unique_values)
else:
    print(f"Column '{column_name}' not found in the CSV file.")

!pip install openai

import requests

API_KEY = "YOUR_API_KEY"
URL = "https://openrouter.ai/api/v1/chat/completions"

# Initialize conversation history
messages = [
    {"role": "system", "content": "You are a helpful assistant."}
]

def ask_question(question):
    """Send a question to the model and return the response."""
    messages.append({"role": "user", "content": question})

    payload = {
        "model": "qwen/qwen-2.5-coder-32b-instruct:free",
        "messages": messages,
        "temperature": 0.7,
        "max_tokens": 512
    }

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.post(URL, json=payload, headers=headers)

    if response.status_code == 200:
        reply = response.json()["choices"][0]["message"]["content"]
        messages.append({"role": "assistant", "content": reply})
        return reply
    else:
        return f"Error: {response.status_code}, {response.text}"

# First question
q1 = "Name 3 American singers."
answer1 = ask_question(q1)
print("\nQ1:", q1)
print("A1:", answer1)

# Extract singers from response (simple logic, can be improved)
singers = answer1.split("\n")[:3]  # Take the first 3 lines if in list format

# Second question depends on the first answer
if singers:
    q2 = f"Name 5 songs for each of these singers: {', '.join(singers)}"
else:
    q2 = "Name 5 songs for each of the singers you just mentioned."

answer2 = ask_question(q2)
print("\nQ2:", q2)
print("A2:", answer2)



import requests  # Library for making API calls

# OpenRouter API Key (Replace with your actual key)
API_KEY = "YOUR_API_KEY"

# OpenRouter API URL
URL = "https://openrouter.ai/api/v1/chat/completions"

# Define a fixed prompt
FIXED_PROMPT = "Name 3 American singers."

# Function to send the fixed prompt to the AI model
def ask_model():
    """
    Sends a fixed prompt to the AI model and returns the response.

    Returns:
        str: The model's response.
    """
    # Define message format
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": FIXED_PROMPT}
    ]

    # Define API request payload
    payload = {
        "model": "qwen/qwen-2-7b-instruct:free",  # Model name
        "messages": messages,  # Fixed prompt
        "temperature": 0.7,  # Adjusts randomness
        "max_tokens": 128000  # Limits response length
    }

    # Set request headers
    headers = {
        "Authorization": f"Bearer {API_KEY}",  # Authentication
        "Content-Type": "application/json"  # JSON format
    }

    try:
        # Make the API request
        response = requests.post(URL, json=payload, headers=headers)
        response.raise_for_status()  # Raise an error for HTTP issues

        # Parse and return AI's response
        return response.json()["choices"][0]["message"]["content"]

    except requests.exceptions.RequestException as e:
        return f"Error: {e}"  # Return error message if API call fails

# Run the script
if __name__ == "__main__":
    print("Fixed Prompt:", FIXED_PROMPT)
    response = ask_model()  # Send request to AI
    print("AI Response:", response)  # Print AI's answer

