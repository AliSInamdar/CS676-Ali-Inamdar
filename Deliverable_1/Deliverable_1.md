# Deliverable 1

## 1. Cloning and installing the tiny troupe package.

```bash
git clone https://github.com/microsoft/tinytroupe
cd tinytroupe
pip install .
```

## 2. Importing the OPENAI API Key.

```bash
export OPENAI_API_KEY="enter api key"
```

## 3. Starting python

```bash
python
```

## 4. Creating 1st persona

```python
from tinytroupe.agent import TinyPerson

ali = TinyPerson("Ali")
ali.define("age", 26)
ali.define("nationality","Indian")
ali.define("occupation","Data Science student at Pace University")
ali.define("skills",["Python","Data Science","Machine Learning","SQL","Deep Learning","JAVA"])
ali.define("quirks","Uses AI Jokes")
```

## 5. Asking Question to 1st persona


## 6. Creating 2nd Persona

```python
yiqiao = TinyPerson("Yiqiao")
yiqiao.define("age", 30)
yiqiao.define("nationality", "Chinese")
yiqiao.define("occupation", "He is a professor at Pace university.")
yiqiao.define("skills",["Python","Data Science","Machine Learning","SQL","Deep Learning","Computer Vision","Neural Networks","Cloud Computing","NLP (Natural Language Processing)"])
john.define("personality", {
    "friendly": True,
    "analytical": True,
})
```

## 7. Observing a conversation between two personas

```bash

```
 
