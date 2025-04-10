# 🔎 URL Validity Rating System

This project evaluates the **validity and trustworthiness of a given URL** based on a user-provided query. It combines natural language processing, sentiment analysis, and external data sources (like fact-checking and citations) to compute a comprehensive **validity score**.

---

## 🚀 Features

| Feature                 | Description                                                                 |
|-------------------------|-----------------------------------------------------------------------------|
| 🔗 Domain Trust         | Estimates trustworthiness of the domain (placeholder logic for MOZ API).    |
| 🧠 Content Relevance    | Uses semantic similarity (Sentence Transformers) to match content to query. |
| ✅ Fact-Checking         | Queries Google Fact Check API to verify facts in the page text.             |
| ⚖️ Bias Detection        | Applies sentiment analysis using a RoBERTa-based model.                     |
| 📚 Citation Scoring      | Checks if the URL is cited via Google Scholar using SerpAPI.                |
| 📊 Final Validity Score | A weighted composite score based on all the above metrics.                  |

---

## 🧱 Tech Stack

- **Python 3.8+**
- `sentence-transformers`
- `transformers` (HuggingFace)
- `textstat`
- `validators`
- `requests`
- `beautifulsoup4`

---

## 📁 Install Dependencies
```python
pip install -U sentence-transformers
pip install validators
pip install textstat
pip install beautifulsoup4
pip install transformers
```

## 🧪 Sample Usage
```bash
user_prompt = "Nvidia Stock price"
url_to_check = "https://leapscholar.com"

result = rate_url_validity(user_prompt, url_to_check)
print(result)
```
## Output:
```bash
{
  "Domain Trust": 60,
  "Content Relevance": 32.14,
  "Fact-Check Score": 50,
  "Bias Score": 100,
  "Citation Score": 0,
  "Final Validity Score": 53.84
}
```
## 🧑‍💻 Author
Ali Inamdar



