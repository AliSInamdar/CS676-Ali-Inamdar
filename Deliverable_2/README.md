# 🤖 Mistral-Powered ChatBot with Code Generation & Execution

**CS 676 - Algorithms for Data Science**  
**Project 2 - Deliverable 2**  
**Author**: Ali Inamdar

This project leverages the [Mistral AI](https://docs.mistral.ai) API to build an interactive Python-based chatbot that can understand user prompts, generate responses, **write Python scripts**, and even **execute them locally** — all in a conversational loop.

---

## 🚀 Key Features

| Feature                             | Description |
|-------------------------------------|-------------|
| 🧠 Chat with Mistral AI             | Interact with a natural language AI agent |
| 🧾 Save Python Scripts              | Automatically detect and extract code blocks from AI responses |
| ⚙️ Execute Scripts Locally         | Run generated Python code and view the output |
| 📜 Maintain Conversation History    | Keeps track of chat context between human and agent |
| 🔒 Secure API & Agent ID Handling   | Uses `api_key` and `agent_id` securely within the class |

---

## 🛠️ Technologies Used

- **Python 3.10+**
- [Mistral AI SDK](https://pypi.org/project/mistralai/)
- `subprocess` for local script execution
- `re` for code block detection
- `IPython` (optional display functionality)

---

## 📁 Install dependencies
```bash
pip install mistralai
```

## Run the chatbot
```bash
python ali_inamdar_proejct2_deliverable2.py
```

## Start chatting You'll be prompted like this:
```bash
🧑 Human: write a python function to reverse a string
🤖 Bot: Here is a Python script...
💻 What name do you want to save for this script? reverse_string
💻 Do you want to execute this script? Enter 'Y' or 'N'.
```
## 💬 How It Works
- When a prompt is entered, the chatbot sends it to Mistral's API using the provided agent ID.

- If the AI responds with a Python code block (python ... ), the code is extracted and saved as a .py file.

- The user can choose to execute the script locally, and the output will be printed in the terminal.

## 🧠 Example Use Case
```bash
🧑 Human: write a python program to calculate factorial
🤖 Bot: Sure! Here's a Python script...

💻 What name do you want to save for this script? factorial
💻 Do you want to execute this script? Y

Script executed successfully.
🤖 Bot Output:
Enter a number: 5
Factorial is: 120
```

## 🙌 Acknowledgments
Thanks to Mistral AI for the API, and the CS 676 course instructors for guidance and project design.

