# -*- coding: utf-8 -*-
"""Deliverable_2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Pa6iPz9DCm9GOxQft7bJ9HLQtXHrp0V0

## Algorithms for Data Science - CS 676
## Project 1 - Deliverable 2
## Ali Inamdar

1. Importing all the libraries required for this deliverable.
"""

#Importing all librariers for this deliverable
import requests
from bs4 import BeautifulSoup
from sentence_transformers import SentenceTransformer, util
from transformers import AutoTokenizer,AutoModelForSequenceClassification
from transformers import pipeline
from huggingface_hub import login

"""2. Importing Serp API & Hugging Face tokens."""

#Hugging Face Access Token
login(token="Hugging FAce Token ")

#Serp API Key
from google.colab import userdata
Ali_serp_api = userdata.get('Ali_Serp_API')

#Google fact check API Key
Ali_google_api = userdata.get('Ali_google_api')

"""3. Creating the Class function."""

class URLValidator:
    """
    A production-ready URL validation class that evaluates the credibility of a webpage
    using multiple factors: domain trust, content relevance, fact-checking, bias detection, and citations.
    """

    def __init__(self):
        # SerpAPI Key
        # This api key is acquired from SerpAPI website.
        self.serpapi_key = Ali_serp_api

        # Load models once to avoid redundant API calls
        self.similarity_model = SentenceTransformer('sentence-transformers/all-mpnet-base-v2')
        self.fake_news_classifier_new = pipeline("text-classification", model="mrm8488/bert-tiny-finetuned-fake-news-detection")
        self.sentiment_analyzer = pipeline("text-classification", model="cardiffnlp/twitter-roberta-base-sentiment")
        self.pipe = pipeline("text-classification", model="mrm8488/distilroberta-finetuned-financial-news-sentiment-analysis")

    def fetch_page_content(self, url: str) -> str:
        """ Fetches and extracts text content from the given URL. """
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")
            return " ".join([p.text for p in soup.find_all("p")])  # Extract paragraph text
        except requests.RequestException:
            return ""  # Fail gracefully by returning an empty string

    def get_domain_trust(self, url: str, content: str) -> int:
      """Computes the domain trust score based on available data sources."""
      trust_scores = []

      # Hugging Face Fake News Detector
      if content:
        try:
            score = self.get_domain_trust_huggingface(content)
            trust_scores.append(score)
        except Exception as e:
            print(f"Error in Hugging Face Trust Calculation: {e}")

      # Compute final score (average of available scores) safely
      return int(sum(trust_scores) / len(trust_scores)) if trust_scores else 50  # Default score is 50 if no data

    def get_domain_trust_huggingface(self, content: str) -> int:
        """ Uses a Hugging Face fake news detection model to assess credibility. """
        if not content:
            return 50  # Default score if no content available
        result = self.fake_news_classifier_new(content[:1200])[0]  # Process only first 1200 characters
        return 100 if result["label"] == "REAL" else 40 if result["label"] == "FAKE" else 50

    def compute_similarity_score(self, user_query: str, content: str) -> int:
        """ Computes semantic similarity between user query and page content. """
        if not content:
            return 0
        return int(util.pytorch_cos_sim(self.similarity_model.encode(user_query), self.similarity_model.encode(content)).item() * 100)

    def check_facts(self, content: str) -> int:
        """ Cross-checks extracted content with Google Fact Check API. """
        if not content:
            return 50
        api_url = f"https://factchecktools.googleapis.com/v1alpha1/claims:search?query={content[:1000]}"
        try:
            response = requests.get(api_url)
            data = response.json()
            return 90 if "claims" in data and data["claims"] else 40
        except:
            return 50  # Default uncertainty score


    def detect_bias(self, content: str) -> int:
        """ Uses NLP sentiment analysis to detect potential bias in content. """
        if not content:
            return 50
        sentiment_result = self.sentiment_analyzer(content[:1000])[0]
        return 100 if sentiment_result["label"] == "POSITIVE" else 50 if sentiment_result["label"] == "NEUTRAL" else 35

    def get_star_rating(self, score: float) -> tuple:
        """ Converts a score (0-100) into a 1-5 star rating. """
        stars = max(1, min(5, round(score / 20)))  # Normalize 100-scale to 5-star scale
        return stars, "⭐" * stars

    def generate_explanation(self, domain_trust, similarity_score, fact_check_score, bias_score,  final_score) -> str:
        """ Generates a human-readable explanation for the score. """
        reasons = []
        if domain_trust < 50:
            reasons.append("The source has low domain authority.")
        if similarity_score < 50:
            reasons.append("The content is not highly relevant to your query.")
        if fact_check_score < 50:
            reasons.append("Limited fact-checking verification found.")
        if bias_score < 50:
            reasons.append("Potential bias detected in the content.")
        #if citation_score < 30:
            #reasons.append("Few citations found for this content.")

        return " ".join(reasons) if reasons else "This source is highly credible and relevant."

    def rate_url_validity(self, user_query: str, url: str) -> dict:
        """ Main function to evaluate the validity of a webpage. """
        content = self.fetch_page_content(url)

        domain_trust = self.get_domain_trust(url, content)
        similarity_score = self.compute_similarity_score(user_query, content)
        fact_check_score = self.check_facts(content)
        bias_score = self.detect_bias(content)
        #citation_score = self.check_google_scholar(url)

        final_score = (
            (0.50 * domain_trust) +
            (0.30 * similarity_score) +
            (0.25 * fact_check_score) +
            (0.30 * bias_score)
            )

        stars, icon = self.get_star_rating(final_score)
        explanation = self.generate_explanation(domain_trust, similarity_score, fact_check_score, bias_score, final_score)

        return {
            "raw_score": {
                "Domain Trust": domain_trust,
                "Content Relevance": similarity_score,
                "Fact-Check Score": fact_check_score,
                "Final Validity Score": final_score
            },
            "stars": {
                "score": stars,
                "icon": icon
            },
            "explanation": explanation
        }

"""4. Running the Class"""

# Instantiate the URLValidator class
validator = URLValidator()

# Define user prompt and URL
user_prompt = "how to make safe investments"
url_to_check = "https://www.sec.gov/investor/pubs/tenthingstoconsider.htm"

# Run the validation
result = validator.rate_url_validity(user_prompt, url_to_check)

# Print the results
import json
print(json.dumps(result, indent=2))