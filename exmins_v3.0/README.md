
# ExamInsight: Real-time Exam Analysis with Pathway

## Overview

ExamInsight is a web application that leverages the power of Retrieval Augmented Generation (RAG) with Pathway to provide real-time insights from exam papers (PDFs). It allows users to upload exam papers and ask questions about them, receiving relevant information and analysis in return.

## Features

- **PDF Upload:** Easily upload exam papers in PDF format.
- **Semantic Search:** Ask questions about the exam papers using natural language.
- **Relevance Ranking:** View the most relevant exam paper sections based on your query.
- **Document Distribution:** Visualize how relevant information is spread across different documents.
- **Word Cloud:** Identify key terms and concepts within the relevant content.
- **Topic Modeling (Simplified):** Get a quick overview of potential topics covered in the exam.
- **Document Viewer:** Read the full content of selected exam paper sections.
- **Future Analysis Options:** The application is designed to incorporate additional analysis types like question type classification, difficulty level assessment, and more detailed topic distribution.

## How it Works

1. **Data Ingestion:** Uploaded PDF exam papers are processed by Pathway, extracting text content and storing each paper as a separate document.
2. **Embeddings:** Pathway uses a pre-trained Sentence Transformer model to generate semantic embeddings for each document, capturing the meaning of the text.
3. **Index Creation:** A KNN (k-Nearest Neighbors) index is built using the document embeddings, enabling efficient similarity search.
4. **Query Processing:** When a user asks a question, it's converted into an embedding, and the KNN index is queried to find the most semantically similar exam paper sections.
5. **Insights Generation:** The frontend (Streamlit) presents the relevant documents and extracts additional insights like relevance scores, document distribution, and potential topics.

## Installation and Running

1. **Prerequisites:**

   - Python 3.7 or higher
   - pip
   - Docker (optional, for containerized deployment)
2. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/examInsights_app_3.0.git
   cd examInsights_app_3.0
   ```


3. **Create a Virtual Environment (Recommended):**
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
4. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
5. **Run the Application:**
   ```bash
   # Start the Pathway backend
   python src/main.py

   # In a separate terminal, start the Streamlit frontend
   streamlit run src/frontend.py
   ```
6. **Access the Application:** Open your web browser and go to `http://localhost:8000`.

## Contributing

Contributions are welcome! Please feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT License.
