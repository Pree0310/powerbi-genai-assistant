import os
import streamlit as st
import pandas as pd
import numpy as np
import re

# Debugging info (optional)
# st.write("Current working directory:", os.getcwd())
# st.write("Files in current directory:", os.listdir())

# Load CSV file
csv_path = os.path.join(os.getcwd(), "healthcare.csv")
df = pd.read_csv(csv_path)

# Simulate fake embeddings (not used in free mode)
df['embedding'] = [np.random.rand(1536).tolist() for _ in range(len(df))]

# Streamlit UI
st.title("Healthcare Q&A Assistant (Free Version)")
user_question = st.text_input("Ask a question about healthcare data:")

# 🔁 Smart Matching Logic (new block)
if user_question:
    st.write("🔍 You asked:", user_question)

    keywords = user_question.lower().split()
    matched_rows = pd.DataFrame()

    # Check for numeric filters like "age > 50"
    match = re.search(r"(age|cost|amount|price|total)\s*(>|<|=)\s*(\d+)", user_question.lower())
    
    if match:
        col, op, val = match.groups()
        val = int(val)

        if col in df.columns:
            if op == ">":
                matched_rows = df[df[col] > val]
            elif op == "<":
                matched_rows = df[df[col] < val]
            elif op == "=":
                matched_rows = df[df[col] == val]
    else:
        # Keyword-based search
        mask = df.apply(lambda row: row.astype(str).str.lower().str.contains('|'.join(keywords)).any(), axis=1)
        matched_rows = df[mask]

    # Show results
    if not matched_rows.empty:
        st.subheader("📊 Matching Results:")
        st.write(matched_rows.head(5))
    else:
        st.warning("❌ No matching data found.")
