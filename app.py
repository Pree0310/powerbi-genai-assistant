import pandas as pd
import numpy as np
import streamlit as st

# Load your CSV file
df = pd.read_csv("healthcare.csv")  # Change to your actual file name

# Simulate fake embeddings (just random vectors for now)

df['embedding'] = [np.random.rand(1536).tolist() for _ in range(len(df))]
# Streamlit UI
st.title("GenAI Q&A Assistant for Power BI CSV")
question = st.text_input("Ask a question about your data:")

if question:
    st.write("🔍 You asked:", question)
    
    # Simulate similarity scoring (random results)
    top_result = df.sample(1)
    
    st.subheader("📊 Closest Matching Row:")
    st.write(top_result)
