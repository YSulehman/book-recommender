import json
from fastapi.responses import FileResponse
from fastapi import FastAPI, WebSocket
from fastapi.staticfiles import StaticFiles
from backend.src.recommender_model import KNN
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")
knn = KNN(None, 'backend/data/clean/embedded_data.pkl', 5)

app = FastAPI()

app.mount("/static", StaticFiles(directory="frontend/public/static"), name="static")

@app.get("/")
async def root():
    return FileResponse("frontend/public/index.html")

# test run
@app.get('/health') 
def health_check():
    return {'message': 'Hello World'}

@app.get('/recommend')
def recommend(book_query: str):
    # embed users book query
    embedded_book_query = model.encode([book_query])

    #set query attribute
    knn.encoded_book_query = embedded_book_query
    
    return {'recommendations': knn.recommend_books()}

# websocket endpoint 
@app.websocket('/ws')
async def websocket_endpoint(websocket: WebSocket):
    # accept WebSocket connection
    await websocket.accept()

    # wait for message from client
    while True:
        query = await websocket.receive_text()

        # embed users book query
        embedded_book_query = model.encode([query])

        #set query attribute
        knn.encoded_book_query = embedded_book_query

        recommendations = knn.recommend_books()

        await websocket.send_text(json.dumps(recommendations))





