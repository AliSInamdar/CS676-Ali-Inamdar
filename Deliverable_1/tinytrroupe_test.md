# Test run for Tiny Troupe.

## Step 1: Installing the tinytroupe package:
'''bash
git clone https://github.com/microsoft/tinytroupe
'''
cd tinytroupe
pip install .

## 2. Importing the OPENAI API Key.
export OPENAI_API_KEY="enter api key"

## 3. Starting python
python

## 3.1. Importing the persona of Lisa the data scientist from tiny troupe
from tinytroupe.examples import create_lisa_the_data_scientist

## 3.2. Assigning a variable to the imported tny persona
lisa_ds = create_lisa_the_data_scientist()

## 3.3. Checking the persona
lisa_ds
TinyPerson(name='Lisa Carter')

## 3.4. Calling the listen & act function of the persona. And asking her a question.


lisa_ds.listen_and_act("Tell me about your life.")
USER --> Lisa Carter: [CONVERSATION] 
          > Tell me about your life.
Lisa Carter acts: [THINK] 
                 > I need to think about how to summarize my life in a way that reflects my
                 > experiences and interests. I should mention my background, education, career, and
                 > personal interests.
Lisa Carter acts: [TALK] 
                 > Sure! I grew up in Vancouver, Canada, in a tech-savvy family. I pursued a
                 > Master's in Data Science at the University of Toronto, where I focused on
                 > improving search relevance using context-aware models. Now, I work as a Data
                 > Scientist at Microsoft in the M365 Search team, analyzing user behavior to
                 > enhance search results. I love learning about AI and machine learning, and in my
                 > free time, I enjoy cooking, playing the piano, and watching movies. How about
                 > you?
Lisa Carter acts: [DONE]


# tinytroupe-test2

## Step 1: Install Packages

Open a terminal from Codespace on Github. In the terminal, run the following command to clone the repository:

```bash
git clone https://github.com/microsoft/tinytroupe
```

Change directory into the `tinytroupe` folder:

```bash
cd tinytroupe
```

Install the package:

```bash
pip install .
```

## Step 2: Setup API Key

In the terminal that you just installed packages, use the following command to setup API Key:

```bash
export OPENAI_API_KEY="xxxx"
```

## Step 3: Experiments (Simulation)

### Talk to an existing persona

```python
from tinytroupe.examples import create_lisa_the_data_scientist
lisa_ds = create_lisa_the_data_scientist() # instantiate a Lisa from the example builder
lisa_ds.listen_and_act("Tell me about your life.")
```


```bash
lisa_ds.listen_and_act("Tell me about your life.")
USER --> Lisa Carter: [CONVERSATION] 
          > Tell me about your life.
Lisa Carter acts: [THINK] 
                 > I need to think about how to summarize my life in a way that reflects my
                 > experiences and interests. I should mention my background, education, career, and
                 > personal interests.
Lisa Carter acts: [TALK] 
                 > Sure! I grew up in Vancouver, Canada, in a tech-savvy family. I pursued a
                 > Master's in Data Science at the University of Toronto, where I focused on
                 > improving search relevance using context-aware models. Now, I work as a Data
                 > Scientist at Microsoft in the M365 Search team, analyzing user behavior to
                 > enhance search results. I love learning about AI and machine learning, and in my
                 > free time, I enjoy cooking, playing the piano, and watching movies. How about
                 > you?
Lisa Carter acts: [DONE]
```