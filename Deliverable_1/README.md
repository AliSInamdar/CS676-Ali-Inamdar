# 🧠 AI Persona Debate using Microsoft TinyTroupe

This project explores the use of **Microsoft's TinyTroupe model** to simulate an engaging, dynamic **debate between two AI-generated personas**. Each persona is uniquely defined by goals, beliefs, and personality traits. The system showcases interactive conversation modeling with realistic character-driven dialogue.

---

## 🎯 Objective

Create two distinct TinyPerson personas and simulate a structured **debate or dialogue** on a given topic, allowing:
- Personality-driven argumentation
- Contrasting viewpoints
- Role-play dynamics between agents

---

## 🛠️ Tech Stack

| Tool/Library | Purpose |
|--------------|---------|
| [TinyTroupe (Microsoft)](https://huggingface.co/microsoft/TinyTroupe) | Multi-agent dialogue modeling |
| Python       | Core scripting |
| VS Code / Colab | Development environment |
| JSON / YAML  | Persona configuration |
|

---

## 👤 Personas

Each persona is defined by:
- **Name**
- **Age**
- **Nationality**
- **Occupation**
- **Knowledge Skills**

Example:
```python
{
  "name": "Ali",
  "Age": ["26"],
  "occupation": ["Student"],
  "skills":["Python","Data Science","Machine Learning","SQL","Deep Learning","JAVA"]"
}
```
## 🧪 Sample Debate Setup
```python
>>> from tinytroupe.environment import TinyWorld
>>> world = TinyWorld("Classroom", [yiqiao, ali])
>>> world.make_everyone_accessible()
>>> yiqiao.listen("I want to extend my deadline on the project assigned.")
```

## 🧾 Output Example
```bash
Yiqiao acts: [THINK] 
            > The person wants to extend their project deadline. I need to consider how to respond
            > to this request and whether it's reasonable or not.
Yiqiao acts: [TALK] 
            > Could you please provide more details about why you need to extend the deadline? It
            > would help me understand your situation better.
Yiqiao acts: [DONE]
```

## 📌 Project Structure
```bash
📦 tinytroupe-debate/
├── personas/               # JSON/YAML persona files
├── README.md               # Project overview
└── results/                # Saved transcripts or logs
```

## 🙌 Acknowledgments
Built using Microsoft TinyTroupe, inspired by human-like AI conversations and roleplay systems.

