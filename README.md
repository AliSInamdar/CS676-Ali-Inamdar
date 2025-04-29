# Algorithms for Data Science - CS 676
## Final Project - Deliverable.

# 🚀 Project 3: AI-Powered Streamlit Applications

Welcome to **Project 3**, a collection of interactive, AI-enhanced Streamlit applications deployed on Hugging Face Spaces. This repository includes:

- 🧠 A dynamic Python code generation chatbot powered by OpenAI
- 📈 A linear regression model builder with dataset upload and metric evaluation

---

## 📁 Repository Structure

```
Project_3/
│
├── Project_3_DynaCode_Chatbot/       # Dynamic Code Generator Bot using OpenAI
│   ├── app.py                        # Streamlit chatbot interface
│   ├── requirements.txt              # Dependencies for Hugging Face
│
├── Project_3_Linear_regression/     # Linear Regression Trainer App
│   ├── app.py                        # Streamlit regression app
│   ├── requirements.txt              # Dependencies for Hugging Face
│
└── README.md                         # Combined project documentation
```

---

## 🤖 Project: Dynamic Python Code Generator Chatbot

An AI-powered Streamlit app that dynamically generates and executes Python code based on user instructions and an uploaded CSV file. Built using OpenAI’s GPT-4o model.

### ✨ Features

- Accepts natural language prompts (e.g., “build a random forest classifier”)
- Upload any dataset (CSV)
- Auto-generates executable Python code using OpenAI API
- Injects uploaded dataset and executes in real-time
- Displays output or errors cleanly

### 🔗 Try it on Hugging Face

👉 [Launch App](https://huggingface.co/spaces/AliInamdar/DynaCode-Chatbot)

---

## 📈 Project: Interactive Linear Regression App

This Streamlit application allows users to upload a CSV dataset, select the target and features, and train a linear regression model with real-time metric evaluation.

### ✨ Features

- Upload your dataset
- Dynamically select target and features
- Trains a `LinearRegression` model from scikit-learn
- Displays:
  - Mean Squared Error (MSE)
  - Mean Absolute Error (MAE)
  - R-squared Score (R²)

### 🔗 Try it on Hugging Face

👉 [Launch App](https://huggingface.co/spaces/AliInamdar/Housing-Price-Predictor)

---

## 🛠 Setup Instructions (Local)

To run either project locally:

```bash
# Navigate into the project folder
cd Project_3_DynaCode_Chatbot  # or Project_3_Linear_regression

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

---

## 🔐 Environment Variables

For the dynamic code bot, set your OpenAI API key:

```bash
export OPENAI_API_KEY=your-key
```

In Hugging Face Spaces, add it in the **“Secrets”** tab as:

- `OPENAI_API_KEY = your-key`

---

## 📜 License

This project is licensed under the MIT License.  
Feel free to use, modify, and share!

---

## 🙌 Author

Made with ❤️ by **Ali Inamdar**  
[GitHub](https://github.com/AliInamdar)
