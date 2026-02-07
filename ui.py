import streamlit as st
from main import run_agent

st.set_page_config(page_title="AI Agent Dashboard", page_icon="🤖", layout="wide")
st.title("🤖 Multi-Agent AI Dashboard")

user_input = st.text_input("Ask your AI agent anything:")

if st.button("Run"):
    with st.spinner("AI is thinking..."):
        result = run_agent(user_input)
        st.subheader("📘 Research Output")
        st.write(result["research"])
        st.subheader("📊 Analysis Output")
        st.write(result["analysis"])
        st.subheader("✅ Final Response")
        st.write(result["final"])
