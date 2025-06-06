import os
import pandas as pd
import numpy as np
import streamlit as st

# Debugging info: check current working directory and files
st.write("Current working directory:", os.getcwd())
st.write("Files in current directory:", os.listdir())

# Safely load your CSV file using absolute path
csv_path = os.path.join(os.getcwd(), "healthcare.csv")
df = pd.read_csv(csv_path)

# Simulate fake embeddings (random vectors)
df['embedding'] = [np.random.rand(1536).tolist() for _ in range(len(df))]

# Streamlit UI
st.title("GenAI Q&A Assistant for Power BI CSV")
question = st.text_input("Ask a question about your data:")

if question:
    st.write("🔍 You asked:", question)
    
    # Simulate similarity scoring (random row for demo)
    top_result = df.sample(1)
    
    st.subheader("📊 Closest Matching Row:")
    st.write(top_result)
