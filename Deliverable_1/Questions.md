# This markdown file answers all three questions.

## Q.1)  How to install `tinytroupe` packages?

```bash
Ans: Firstly we will need to create a new repo in github.
     Then after that we will need to open a codespace on the repo.
     After that step we need to paste teh following command into the terminal of our codespace.
     "git clone https://github.com/microsoft/tinytroupe"
     After we complete this step we need to change our directory to the tiny troupe by using the following command
     "cd tinytroupe"
     After this step we need to install all packages from the cloned repo, by using the following command
     "pip install ."
     And, then we would have successfully intalled the tinytroupe packages onto our repo.
```


## Q.2) What is Turin test?In today's world with Large Language Models (LLMs), what is the definition of Turing Test?

```bash
Ans: The Turing Test was proposed by Alan Turing in 1950 as a way to evaluate a machine’s ability to exhibit intelligent  behavior equivalent to, or indistinguishable from, that of a human.
     The original test,nvolved a human judge engaging in natural language conversations with both a human and a machine.
     If the judge could not reliably distinguish between the two, the machine was said to have passed the test.

    With the rise of LLMs like ChatGPT, GPT-4, Claude, Gemini, and others, the concept of the Turing Test has evolved:

    1. Surface-Level Imitation vs. True Intelligence
        - LLMs can generate human-like responses and often fool users into thinking they are interacting with a human. 
        However, they do not possess true understanding, consciousness, or reasoning beyond pattern recognition and statistical inference.

    2. Expanded Definitions of AI Evaluation
        The traditional Turing Test is now considered insufficient as a benchmark for true intelligence. Newer benchmarks focus on:

        - AGI (Artificial General Intelligence): Ability to generalize across different domains.

        - Cognitive and Reasoning Tests: Evaluating problem-solving, logic, and planning.

        - Ethical and Contextual Understanding: Assessing bias, misinformation handling, and ethical decision-making.

    3. Modern Turing Test Variants

        - Linguistic Imitation Tests: Can an AI consistently fool an expert? (E.g., chat-based Turing tests)

        - Embodied Turing Test: Can an AI behave like a human in real-world interactions?

        - Winograd Schema Challenge: Can an AI resolve ambiguous pronoun references that require reasoning?

        - AI Safety Tests: Ensuring AI does not manipulate, deceive, or generate harmful content.

     In summary, some LLMs have fooled users in short interactions, no AI has yet passed a rigorous, long-term Turing Test consistently across multiple domains without revealing its non-human nature.    
```

## Q.3)Create a simulation of your own topic and show me the transcript. This implies define at least two personas of your own choice with conflict built in and observe their conversation. You can simply copy/paste the conversation in a .md file. Please comment on the transcript whether you think the Turing Test is passed.

```python
from tinytroupe.agent import TinyPerson

ali = TinyPerson("Ali")
ali.define("age", 26)
ali.define("nationality","Indian")
ali.define("occupation","Data Science student at Pace University")
ali.define("skills",["Python","Data Science","Machine Learning","SQL","Deep Learning","JAVA"])
ali.define("quirks","Uses AI Jokes")
```

```python
from tinytroupe.agent import TinyPerson

yiqiao = TinyPerson("Yiqiao")
yiqiao.define("age", 30)
yiqiao.define("nationality", "Chinese")
yiqiao.define("occupation", "He is a professor at Pace university.")
yiqiao.define("skills",["Python","Data Science","Machine Learning","SQL","Deep Learning","Computer Vision","Neural Networks","Cloud Computing","NLP (Natural Language Processing)"])
```

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
# Comments & Thoughts:

```bash
My thoughts: I think that this converstion between these two bots has passed the Turing Test.

Reason: 
- I think the bot has passed the Turing test because of the way the conversation flow has taken place , and also due to the ease in which the enlish language was used by it.
- I also think that this type of converstion is something that you can easily hear between a real student and a real teacher.
- Hence , I think that this bot conversation has passed the Turing Test.
```