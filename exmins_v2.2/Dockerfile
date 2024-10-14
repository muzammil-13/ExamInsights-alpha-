FROM pathwaycom/pathway:latest

WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y python3-opencv tesseract-ocr-eng \
    && rm -rf /var/lib/apt/lists/* /var/cache/apt/archives/*

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install -U --no-cache-dir -r requirements.txt 

# Copy application code
COPY . .

# Expose ports
EXPOSE 8000  
# Pathway app port
EXPOSE 8501  
# Streamlit port

# Set environment variables (optional)
# ENV PATHWAY_APP_URL=http://localhost:8000 

# Start both Pathway and Streamlit
CMD ["sh", "-c", "python app.py & streamlit run streamlit_app.py"]
