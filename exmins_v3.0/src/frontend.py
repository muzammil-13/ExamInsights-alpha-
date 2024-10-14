import streamlit as st
import requests
import os
import pandas as pd
import plotly.express as px
from wordcloud import WordCloud
import matplotlib.pyplot as plt

API_URL = "http://localhost:8000"

st.set_page_config(layout="wide")
st.title("ExamInsight: Real-time Exam Analysis")

# File uploader for PDF
uploaded_file = st.file_uploader("Upload an exam paper (PDF)", type="pdf")

if uploaded_file:
    # Save the uploaded file
    save_path = os.path.join("data", uploaded_file.name)
    with open(save_path, "wb") as f:
        f.write(uploaded_file.getvalue())
    st.success(f"File {uploaded_file.name} has been uploaded and saved.")

# Query input
query = st.text_input("Ask a question about the exam papers:")

if query:
    try:
        response = requests.post(f"{API_URL}/query", json={"question": query})
        if response.status_code == 200:
            results = response.json()
            st.subheader("Insights:")
            
            # Convert results to DataFrame
            df = pd.DataFrame(results)
            
            # Display results in a table
            st.dataframe(df)
            
            # Visualizations
            col1, col2 = st.columns(2)
            
            with col1:
                # Bar chart of relevance scores
                fig = px.bar(df, x='id', y='score', title='Relevance Scores by Document')
                st.plotly_chart(fig)
            
            with col2:
                # Pie chart of document distribution
                fig = px.pie(df, names='id', values='score', title='Document Distribution')
                st.plotly_chart(fig)
            
            # Word cloud of document content
            st.subheader("Word Cloud of Relevant Documents")
            text = " ".join(df['content'].tolist())
            wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
            fig, ax = plt.subplots()
            ax.imshow(wordcloud, interpolation='bilinear')
            ax.axis('off')
            st.pyplot(fig)
            
            # Topic modeling (simplified version)
            st.subheader("Top Topics")
            topics = df['content'].str.split().explode().value_counts().head(10)
            st.bar_chart(topics)
            
            # Interactive document viewer
            st.subheader("Document Viewer")
            selected_doc = st.selectbox("Select a document to view:", df['id'])
            if selected_doc:
                doc_content = df[df['id'] == selected_doc]['content'].iloc[0]
                st.text_area("Document Content", doc_content, height=300)
            
        else:
            st.error("Failed to get insights. Please try again.")
    except requests.RequestException as e:
        st.error(f"An error occurred: {str(e)}")

# Add a sidebar with additional options
st.sidebar.header("Analysis Options")
analysis_type = st.sidebar.selectbox(
    "Choose analysis type",
    ["General", "Question Types", "Difficulty Level", "Topic Distribution"]
)

if analysis_type != "General":
    st.subheader(f"{analysis_type} Analysis")
    st.info(f"Placeholder for {analysis_type} analysis. Implement specific visualizations here.")

# Add a feedback section
st.sidebar.header("Feedback")
feedback = st.sidebar.text_area("Provide feedback or report issues:")
if st.sidebar.button("Submit Feedback"):
    # Implement feedback submission logic here
    st.sidebar.success("Thank you for your feedback!")