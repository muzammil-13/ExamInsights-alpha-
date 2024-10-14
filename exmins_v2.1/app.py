import streamlit as st
import requests

# --- Configuration ---
HOST = "localhost"
PORT = 8080
RAG_API_URL = f"http://{HOST}:{PORT}/query"

# --- Helper Function to Process PDF and Query RAG ---
def analyze_pdf_and_answer(uploaded_file, question=None):
    """
    Processes the uploaded PDF using the RAG pathway and answers the question.

    Args:
        uploaded_file: The uploaded PDF file object.
        question (str, optional): The user's question. Defaults to None.

    Returns:
        str: The answer from the RAG pathway or an error message.
    """
    if uploaded_file is not None:
        try:
            # Send the PDF content to your RAG API
            files = {"file": uploaded_file}  # Use 'files' for multipart upload
            response = requests.post(RAG_API_URL, files=files, json={"query": question})
            response.raise_for_status()

            # Get the answer from the response
            answer = response.json().get("answer", "No answer found in the response.")
            return answer

        except requests.exceptions.RequestException as e:
            return f"Error communicating with RAG API: {e}"
    else:
        return "Please upload a PDF file."

# --- Streamlit App ---
st.title("📄 Ask Your Documents")

# File Upload
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

# Analyze Button
if st.button("Analyze"):
    if uploaded_file is not None:
        with st.spinner("Analyzing document..."):
            # Process the PDF and get a general analysis (no question yet)
            general_analysis = analyze_pdf_and_answer(uploaded_file)
            st.write("**Analysis:**", general_analysis)
    else:
        st.warning("Please upload a PDF file.")

# User Question Input
user_question = st.text_input("Ask a question about the document:")

# Get Answer Button
if st.button("Get Answer"):
    if user_question and uploaded_file:
        with st.spinner("Getting your answer..."):
            answer = analyze_pdf_and_answer(uploaded_file, user_question)
            st.write("**Answer:**", answer)
    else:
        st.warning("Please upload a PDF and enter a question.")
