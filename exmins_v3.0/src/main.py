import os
import pathway as pw
from pathway.stdlib.ml.index import KNNIndex
from pathway.stdlib.ml.embedders import SentenceTransformerEmbedder

# Initialize embedder
embedder = SentenceTransformerEmbedder(model_name="all-MiniLM-L6-v2")

# Define data directory
data_dir = os.path.join(os.path.dirname(__file__), "..", "data")

# Read PDF files
def read_pdfs():
    return pw.io.fs.read(data_dir, format="binary")

# Process PDFs
pdfs = read_pdfs()
documents = pdfs.select(
    content=pw.apply(lambda x: x.decode("utf-8"), pw.this.data),
    id=pw.this.filename,
)

# Create embeddings
embeddings = documents.select(
    embedding=embedder(pw.this.content),
    id=pw.this.id,
)

# Create KNN index
index = KNNIndex(embeddings, embedding_column="embedding")

# Query function
@pw.udf
def query(question: str, k: int = 5):
    query_embedding = embedder(question)
    results = index.query(query_embedding, k=k)
    return results

# API endpoint
api = pw.io.http.rest_api(query=query)

# Run the pipeline
pw.run()