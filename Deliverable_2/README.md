# 🔐 URL Validity Scorer

Deliverable 2

This project provides a **production-ready, multi-factor URL credibility evaluator** that uses natural language processing, fact-checking APIs, and sentiment analysis to assess the trustworthiness of a webpage in the context of a user's query.

---

## 🚀 Overview

The `URLValidator` class evaluates web content based on:
- **Domain Trust** (via fake news detection models)
- **Content Relevance** (semantic similarity with user query)
- **Fact-Checking** (using Google Fact Check API)
- **Bias Detection** (via sentiment analysis)

It returns:
- A final **credibility score (0–100)**
- A **1–5 star rating**
- A human-readable **explanation** of credibility factors

---

## 🔧 Tech Stack

| Tool/Library | Purpose |
|--------------|---------|
| `transformers` (HuggingFace) | Text classification pipelines |
| `sentence-transformers` | Semantic similarity |
| `BeautifulSoup` | HTML parsing |
| `requests` | HTTP requests |
| `huggingface_hub` | Hugging Face authentication |
| `Google Fact Check API` | Verifying factual accuracy |
| `SerpAPI` *(optional)* | Citation info (commented in code) |

---

## 📁 Install dependencies
```python
pip install requests
pip install beautifulsoup4
pip install -U sentence-transformers
pip install transformers
pip install huggingface_hub
```
## 🧪 Example Usage
```python
validator = URLValidator()

user_prompt = "how to make safe investments"
url_to_check = "https://www.sec.gov/investor/pubs/tenthingstoconsider.htm"

result = validator.rate_url_validity(user_prompt, url_to_check)

import json
print(json.dumps(result, indent=2))
```

## ✅ Sample Output:
```python
{
  "raw_score": {
    "Domain Trust": 100,
    "Content Relevance": 82,
    "Fact-Check Score": 90,
    "Final Validity Score": 93.5
  },
  "stars": {
    "score": 5,
    "icon": "⭐⭐⭐⭐⭐"
  },
  "explanation": "This source is highly credible and relevant."
}
```



