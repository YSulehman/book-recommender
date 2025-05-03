import pickle
from sklearn.neighbors import NearestNeighbors

class KNN:
    def __init__(self, encoded_book_query: str, data_pth: str, num_neightbours:int, metric: str='cosine'):
        self.num_neighbours = num_neightbours
        self.metric = metric
        self.data_pth = data_pth
        self.encoded_book_query = encoded_book_query

    def recommend_books(self):
        # load data 
        with open(self.data_pth, 'rb') as f:
            data = pickle.load(f)

        embedded_data = data['embeddings']
        titles = data['titles']

        # nearest neighbour model
        self.nn_model = NearestNeighbors(self.num_neighbours, metric=self.metric)

        # fit model 
        self.nn_model.fit(embedded_data)

        # Find closest neighbors
        _ , indices = self.nn_model.kneighbors(self.encoded_book_query)
        
        # Return recommended titles
        return [titles[i] for i in indices[0]]
