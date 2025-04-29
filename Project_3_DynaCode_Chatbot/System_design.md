# System Design for DynaCode_Chatbot

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