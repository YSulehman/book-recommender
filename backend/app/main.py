from fastapi import FastAPI
from backend.src.recommender_model import KNN
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")
knn = KNN(None, 'backend/data/clean/embedded_data.pkl', 5)


app = FastAPI()

# test run
@app.get('/') 
def health_check():
    return {'message': 'Hello World'}

@app.get('/recommend')
def recommend(book_query: str):
    # embed users book query
    embedded_book_query = model.encode([book_query])

    #set query attribute
    knn.encoded_book_query = embedded_book_query
    
    return {'recommendations': knn.recommend_books()}


