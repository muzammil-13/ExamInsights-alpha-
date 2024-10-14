# ExamInsight: Real-time Exam Analysis with Pathway RAG

## Introduction

ExamInsight is a powerful application that leverages the capabilities of Real-time Augmented Generation (RAG) to provide dynamic insights from exam papers. Powered by Pathway, ExamInsight ingests data from PDF documents stored in its data folder, making it an invaluable tool for both students and educators.

What sets ExamInsight apart is its ability to adapt to changes in real-time. Built with Pathway and Docker, it operates within a containerized environment, ensuring seamless deployment and management. Pathway's in-memory scalable vector store allows ExamInsight to instantly reflect any modifications made to the source PDFs, ensuring users always have access to the most up-to-date analysis. The Streamlit frontend provides an intuitive and user-friendly way to interact with the application.

## Table of Contents

- [Introduction](#introduction)
- [What Problem It Solves](#what-problem-it-solves)
- [Architecture Overview](#architecture-overview)
- [Getting Started](#getting-started)
- [Demo](#demo)
- [Contributing](#contributing)
- [Contact Information](#contact-information)

## What Problem It Solves

ExamInsight addresses the challenge of extracting meaningful insights from static exam papers. Traditionally, analyzing these documents was a time-consuming and manual process. ExamInsight changes this by automatically processing and analyzing PDF exam papers, providing real-time insights into question patterns, topics, and difficulty levels.

Currently, ExamInsight ingests data from PDFs stored within its data folder. However, it can be easily extended to connect with live, dynamic data sources like Google Drive, offering real-time updates as collaborators make changes. This opens up a world of possibilities for collaborative exam analysis and ensures everyone has access to the latest information. Explore over 300+ data connectors here: [https://github.com/pathwaycom/llm-app?tab=readme-ov-file#llm-app](https://github.com/pathwaycom/llm-app?tab=readme-ov-file#llm-app) and [https://pathway.com/app-templates](https://pathway.com/app-templates).

## Architecture Overview

ExamInsight is built upon a robust and scalable architecture:

- **Pathway:** The core of ExamInsight, Pathway is a production-ready RAG framework that enables real-time updates and powers the live Gen AI capabilities.
- **Docker:** Docker provides containerization, making ExamInsight easily deployable and manageable across different environments.
- **Local Data Folder for Data Ingestion:** ExamInsight ingests PDF documents stored in its local data folder. This approach can be extended to connect with external data sources like Google Drive for dynamic updates.
- **Streamlit:** Streamlit provides the user interface for interacting with ExamInsight, making it easy to ask questions and get insights from the exam papers.

## Getting Started

To run ExamInsight locally, follow these steps:

**Prerequisites:**

- Docker: Install Docker Desktop for your operating system from [https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/)
- Pathway: Install Pathway using pip: `pip install pathway-ai`

**Instructions:**

1. **Clone the Repository:** `git clone https://github.com/your-username/ExamInsight.git`
2. **Navigate to the Project Directory:** `cd ExamInsight`
3. **Build the Docker Image:** `docker build -t exam-insight .`
4. **Run the Docker Container:** `docker run -p 8000:8000 -p 8501:8501 exam-insight`

**Adding PDFs and Connecting Google Drive:**

- **Add PDFs:** Place your exam paper PDFs in the designated `data` folder within the project directory.
- **Connect Google Drive (Future Enhancement):**  Instructions on connecting Google Drive for live updates will be added in a future release.

## Demo

[Include a demo video or GIF showcasing ExamInsight's features and functionality here.]

## Contributing

We welcome contributions from the community! If you'd like to contribute to ExamInsight, please follow these guidelines:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with descriptive messages.
4. Push your changes to your forked repository.
5. Submit a pull request to the main repository.

## Contact Information

For any questions, suggestions, or collaboration opportunities, please contact [muzammilibrahim13@gmail.com](muzammilibrahim13@gmail.com)
