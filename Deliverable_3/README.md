# 📊 CS676 - URL Validity Prediction with Neural Networks

**Project 1 - Deliverable 3**  
**Author**: Ali Inamdar

This project builds a neural network model to predict the **custom rating** of web content based on the **user prompt** and **functional rating**. It combines data aggregation from multiple GitHub repositories, tokenization, model training using TensorFlow, and deployment on Hugging Face.

---

## 📁 Contents

- 🔗 Combine multiple CSV datasets from student repositories
- 🤖 Build and train a multi-input neural network model with TensorFlow
- 🧠 Use tokenized user prompts and functional ratings as inputs
- ☁️ Deploy model + tokenizer to Hugging Face Hub
- 💡 Load and infer predictions using downloaded artifacts

---

## 📦 Dependencies

Install all required packages using pip:

```bash
pip install --upgrade huggingface_hub
pip install pandas requests beautifulsoup4
pip install tensorflow matplotlib keras
```

## 📚 Data Preparation
```
- Inputs: GitHub CSV URLs with the following columns:

    user_prompt

    url_to_check

    func_rating

    custom_rating

- Process:

    Convert GitHub URLs to raw format

    Download, decode (UTF-8/Latin-1)

    Normalize and combine columns

    Convert func_rating and custom_rating to integers
```

## 🧠 Model Architecture
The neural network has two inputs:

  1. Tokenized user prompt (via Embedding + Dense layers)

  2. Functional rating (via Dense layer)

The branches are concatenated and passed through a final Dense layer with softmax activation for multi-class classification (0–5 stars).
```python
Inputs: [Text Input, Func Rating]
Embedding -> Flatten -> Dense -> ...
                         ⬇
            Dense (func rating)
                         ⬇
              Concatenate ➜ Softmax
```
## ⚙️ Training Parameters
Embedding Dim: 16

Max Length: Calculated from data

Epochs: 80

Batch Size: 2

Loss: Categorical Crossentropy

Optimizer: Adam

Output: One-hot encoded custom_rating (6 classes)

## ☁️ Hugging Face Deployment
The model and tokenizer are saved locally and then pushed to Hugging Face:

  - model.keras: Trained model

  - tokenizer.pkl: Tokenizer used during training

These artifacts are then downloaded for inference.

## 🧪 Local Inference
Test prompts like:
```python
["Best stock to buy?", "How to make safe investments?"]
```

## 🧠 Sample Output
```plaintext
Prompt: Best stock to buy?
Predicted Rating: 0.85
--------------------------------------------------
Prompt: How to make safe investments?
Predicted Rating: 0.76
--------------------------------------------------
```
