import streamlit as st
import requests  # For making requests to the Pathway app
import os
from pymupdf import fitz  # For PDF processing

# --- Configuration ---
PATHWAY_APP_URL = os.environ.get("PATHWAY_APP_URL", "http://localhost:8000")


# --- Streamlit UI ---
st.title("ExamInsight: Unlock Exam Paper Insights")

uploaded_file = st.file_uploader("Upload an Exam Paper (PDF)", type=["pdf"])

if uploaded_file is not None:
    # --- PDF Processing Example ---
    with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
        text = ""
        for page in doc:
            text += page.get_text()

    # TODO (Future Enhancement):
    # 1. Save the extracted 'text' to a file in your 'data/' folder.
    # 2. Trigger the Pathway app to re-index (potentially using Celery).

    # --- Querying the Pathway App ---
    st.header("Ask a Question about the Exam Paper:")
    user_question = st.text_input("Your Question:")

    if st.button("Get Insights"):
        if user_question:
            response = requests.post(
                f"{PATHWAY_APP_URL}/v1/pw_ai_answer",
                json={"prompt": user_question},
            )

            if response.status_code == 200:
                insights = response.json()
                st.subheader("Insights:")
                st.write(insights)  # Display the insights
            else:
                st.error("Error communicating with the Pathway app.")
        else:
            st.warning("Please enter a question.")
