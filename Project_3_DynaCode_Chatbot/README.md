# 🤖 Dynamic Python Code Generator Bot

This Streamlit app uses OpenAI's GPT to generate and execute Python code dynamically based on user instructions and an uploaded CSV dataset. It's ideal for quickly prototyping data science tasks like regression, classification, or visualization.

## 🧠 How It Works

1. You enter a Python task (e.g., “build a random forest classifier for diabetes”)
2. You upload a CSV dataset
3. The bot generates executable Python code using OpenAI
4. The code is auto-corrected to reference your uploaded file
5. The script is executed and results are shown live!

## 🚀 Features

- Dynamic code generation using OpenAI GPT-4o
- Smart path injection to avoid file-not-found errors
- Automatically displays execution results
- Hugging Face Spaces-compatible

## 🔐 Secrets Required

- Set your OpenAI API key as a secret on Hugging Face:
  - `OPENAI_API_KEY=your-key`

## 📂 Files

- `app.py` — Streamlit app logic
- `requirements.txt` — Dependencies list

## ✅ Requirements

```bash
streamlit
openai
pandas
scikit-learn
```

## System Design
```python
┌──────────────────────┐
│  User opens App      │
└─────────┬────────────┘
          │
          ▼
┌────────────────────────────────────────┐
│ Upload CSV file                        │
└─────────┬──────────────────────────────┘
          │
          ▼
┌────────────────────────────────────────┐
│ Enter Natural Language Prompt          │
│ (e.g.,"build random forest classifier")│
└─────────┬──────────────────────────────┘
          │
          ▼
┌────────────────────────────────────────┐
│ OpenAI API called (gpt-4o)             │
│ Generates clean executable Python code │
└─────────┬──────────────────────────────┘
          │
          ▼
┌────────────────────────────────────────┐
│ Replace Hardcoded pd.read_csv()        │
│ → Inject uploaded file reference       │
└─────────┬──────────────────────────────┘
          │
          ▼
┌────────────────────────────────────────┐
│ Execute generated code safely          │
│ - Capture stdout                       │
└─────────┬──────────────────────────────┘
          │
          ▼
┌────────────────────────────────────────┐
│ Display Execution Output to User       │
└────────────────────────────────────────┘
```

## Author
Ali Inamdar