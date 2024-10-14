FROM pathwaycom/pathway:latest

WORKDIR /app

RUN apt-get update \
    && apt-get install -y python3-opencv tesseract-ocr-eng \
    && rm -rf /var/lib/apt/lists/* /var/cache/apt/archives/*

COPY requirements.txt .
RUN pip install -U --no-cache-dir -r requirements.txt

COPY . .


# Expose the port your application listens on
EXPOSE 8000

# Start Streamlit with the appropriate address and port
CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0", "--server.port=8000"] 

