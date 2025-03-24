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

```python
ali.listen_and_act("Tell me about your life.")
USER --> Ali: [CONVERSATION] 
          > Tell me about your life.
Ali acts: [THINK] 
         > I need to think about how to describe my life. I should mention my studies, interests,
         > and maybe a bit about my personality.
Ali acts: [TALK] 
         > Well, I'm currently a Data Science student at Pace University. I'm 26 years old and I
         > have a strong interest in Python, Machine Learning, and Deep Learning. I enjoy working
         > with data and finding insights that can help solve problems. I also have a quirky side
         > where I like to use AI jokes!
Ali acts: [DONE] 
```

## 6. Creating 2nd Persona

```python
from tinytroupe.agent import TinyPerson

yiqiao = TinyPerson("Yiqiao")
yiqiao.define("age", 30)
yiqiao.define("nationality", "Chinese")
yiqiao.define("occupation", "He is a professor at Pace university.")
yiqiao.define("skills",["Python","Data Science","Machine Learning","SQL","Deep Learning","Computer Vision","Neural Networks","Cloud Computing","NLP (Natural Language Processing)"])
```

## 7. Observing a conversation between two personas

```bash

>>> from tinytroupe.environment import TinyWorld
>>> world = TinyWorld("Classroom", [yiqiao, ali])
>>> world.make_everyone_accessible()
>>> yiqiao.listen("I want to extend my deadline on the project assigned.")


USER --> Yiqiao: [CONVERSATION] 
          > I want to extend my deadline on the project assigned.
TinyPerson(name='Yiqiao')
>>> world.run(3)
──────────────────────────────────────────────────────────────── Classroom step 1 of 3 ────────────────────────────────────────────────────────────────
Yiqiao acts: [THINK] 
            > The person wants to extend their project deadline. I need to consider how to respond
            > to this request and whether it's reasonable or not.
Yiqiao acts: [TALK] 
            > Could you please provide more details about why you need to extend the deadline? It
            > would help me understand your situation better.
Yiqiao acts: [DONE] 

Yiqiao --> Ali: [CONVERSATION] 
            > Could you please provide more details about why you need to extend the deadline? It
            > would help me understand your situation better.
Ali acts: [THINK] 
         > Yiqiao is asking for more details about the deadline extension. I need to explain my
         > reasons clearly and concisely to help them understand my situation better.
Ali acts: [TALK] 
         > I appreciate your willingness to understand my situation better. The reason I need to
         > extend the deadline is that I've encountered some unexpected challenges with my project
         > that have set me back. I want to ensure that I can deliver quality work, and a little
         > more time would really help me achieve that.
Ali acts: [DONE] 

Ali --> Yiqiao: [CONVERSATION] 
         > I appreciate your willingness to understand my situation better. The reason I need to
         > extend the deadline is that I've encountered some unexpected challenges with my project
         > that have set me back. I want to ensure that I can deliver quality work, and a little
         > more time would really help me achieve that.
──────────────────────────────────────────────────────────────── Classroom step 2 of 3 ────────────────────────────────────────────────────────────────
Yiqiao acts: [THINK] 
            > Ali has encountered unexpected challenges and needs more time to ensure quality work.
            > This is a reasonable request, and I should consider granting the extension.
Yiqiao acts: [TALK] 
            > Thank you for explaining your situation, Ali. I understand that unexpected challenges
            > can arise. How much additional time do you think you would need to complete the
            > project?
Yiqiao acts: [DONE] 

Yiqiao --> Ali: [CONVERSATION] 
            > Thank you for explaining your situation, Ali. I understand that unexpected challenges
            > can arise. How much additional time do you think you would need to complete the
            > project?
Ali acts: [THINK] 
         > Yiqiao is understanding about my situation, which is good. I need to consider how much
         > additional time I would realistically need to complete the project. I think an extra week
         > should be sufficient to address the challenges I faced and ensure the quality of my work.
Ali acts: [TALK] 
         > Thank you for your understanding, Yiqiao. I believe that an additional week would be
         > sufficient for me to complete the project. This will give me the time I need to address
         > the challenges I've encountered and ensure that I deliver quality work.
Ali acts: [DONE] 

Ali --> Yiqiao: [CONVERSATION] 
         > Thank you for your understanding, Yiqiao. I believe that an additional week would be
         > sufficient for me to complete the project. This will give me the time I need to address
         > the challenges I've encountered and ensure that I deliver quality work.
──────────────────────────────────────────────────────────────── Classroom step 3 of 3 ────────────────────────────────────────────────────────────────
Yiqiao acts: [THINK] 
            > Ali believes that an additional week will be sufficient to complete the project. This
            > seems reasonable, and I should consider granting the extension.
Yiqiao acts: [TALK] 
            > I can grant you the additional week for the project. I appreciate your commitment to
            > delivering quality work. Please let me know if you need any further assistance during
            > this time.
Yiqiao acts: [DONE] 

Yiqiao --> Ali: [CONVERSATION] 
            > I can grant you the additional week for the project. I appreciate your commitment to
            > delivering quality work. Please let me know if you need any further assistance during
            > this time.
Ali acts: [THINK] 
         > Yiqiao has granted me the additional week for the project, which is a relief. I should
         > express my gratitude and also consider if I need any assistance during this time.
Ali acts: [TALK] 
         > Thank you so much for granting me the additional week, Yiqiao. I really appreciate your
         > understanding and support. I will definitely reach out if I need any further assistance
         > during this time.
Ali acts: [DONE] 

Ali --> Yiqiao: [CONVERSATION] 
         > Thank you so much for granting me the additional week, Yiqiao. I really appreciate your
         > understanding and support. I will definitely reach out if I need any further assistance
         > during this time.
>>> 

```
 
## 8. Turing Test

```bash
My thoughts: I think that this converstion between these two bots has passed the Turing Test.

Reason: 
- I think the bot has passed the Turing test because of the way the conversation flow has taken place , and also due to the ease in which the enlish language was used by it.
- I also think that this type of converstion is something that you can easily hear between a real student and a real teacher.
- Hence , I think that this bot conversation has passed the Turing Test.