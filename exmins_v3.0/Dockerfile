FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000 8501

CMD ["sh", "-c", "python src/main.py & streamlit run src/frontend.py"]