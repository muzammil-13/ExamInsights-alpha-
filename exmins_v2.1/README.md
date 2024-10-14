# 📄 ExamInsight - A RAG-Powered Question Answering App

This project demonstrates a simple Question Answering application built with Streamlit and powered by a Retrieval Augmented Generation (RAG) pathway.

## Features

* **PDF Upload:** Easily upload PDF documents to the app.
* **Document Analysis:** The app uses a RAG pipeline to analyze the content of your uploaded PDFs.
* **Question Answering:** Ask questions about the document, and the app will provide relevant answers based on the analyzed content.

## How it Works

1. **Frontend (Streamlit):**
   - The user interface is built with Streamlit, allowing users to upload PDFs and ask questions.
2. **Backend (RAG API):**
   - A separate API (example provided using Flask) handles the RAG processing:
     - Receives the uploaded PDF from the Streamlit app.
     - Extracts text from the PDF.
     - Passes the text through a RAG pipeline (embedding, vector search, LLM response generation).
     - Returns the generated answer to the Streamlit app.

## Getting Started

### Prerequisites

- Python 3.7+
- Install the required packages: `pip install -r requirements.txt`

### Running the Application

1. **Start the RAG API:**
   - Navigate to the API directory.
   - Run: `python api.py` (replace `api.py` with your API script name).
2. **Start the Streamlit App:**
   - Navigate to the Streamlit app directory.
   - Run: `streamlit run app.py`

Now you can access the app in your web browser at `http://localhost:8000` (or the port specified by Streamlit).

## Configuration

- **API Endpoint:** The Streamlit app is configured to communicate with the RAG API at `http://localhost:8080/query`. Adjust the `HOST` and `PORT` variables in `app.py` if necessary.

## Future Improvements

- **Enhanced UI:** Improve the user interface with more interactive elements and visualizations.
- **Document Chunking:** Implement chunking for handling large PDF documents more efficiently.
- **Asynchronous Processing:** Use asynchronous tasks to prevent the app from blocking during long-running RAG processes.
- **Error Handling:** Add more robust error handling to provide informative messages to the user.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have any suggestions or improvements.
