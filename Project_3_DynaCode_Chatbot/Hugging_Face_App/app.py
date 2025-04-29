import streamlit as st
import openai
import pandas as pd
import subprocess
import os
import io
import contextlib
import re

# Setup OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="🧠 Build Any Model", layout="centered")
st.title("🤖 Dynamic Code Generator Chatbot")

prompt = st.text_input("🧠 Tell me what you want to build:")
uploaded_file = st.file_uploader("📂 Upload your dataset (CSV)", type=["csv"])

def replace_dataset_paths(code: str) -> str:
    """Replace all pd.read_csv(...) with in-memory file reference 'uploaded_file'."""
    return re.sub(r"pd\.read_csv\(['\"](.*?)['\"]\)", "pd.read_csv(uploaded_file)", code)

if st.button("🚀 Generate and Run"):
    if prompt and uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.success("✅ File loaded successfully.")
        
        # Call OpenAI to generate code
        system_prompt = "You are a Python code generator. Only output clean, executable Python code inside one code block. No explanation."
        client = openai.OpenAI()
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
        )
        code = response.choices[0].message.content
        if "```python" in code:
            code = code.split("```python")[-1].split("```")[0].strip()

        # 🔁 Replace any pd.read_csv(...) with the uploaded_file reference
        code = replace_dataset_paths(code)
        
        st.code(code, language="python")

        # 🔄 Inject uploaded_file as a runtime variable
        output_buffer = io.StringIO()
        try:
            with contextlib.redirect_stdout(output_buffer):
                uploaded_file.seek(0)
                exec(code, {"uploaded_file": uploaded_file})
            st.success("✅ Code executed successfully.")
            st.text(output_buffer.getvalue())
        except Exception as e:
            st.error(f"❌ Error during execution: {e}")
    else:
        st.warning("⚠️ Please upload a dataset and enter a prompt.")
