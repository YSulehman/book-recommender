import pickle
from sklearn.neighbors import NearestNeighbors

class KNN:
    """
    unsupervised knn for recommender
    """
    def __init__(self, encoded_book_query: str, data_pth: str, num_neightbours:int, metric: str='cosine'):
        self.num_neighbours = num_neightbours
        self.metric = metric
        self.data_pth = data_pth
        self.encoded_book_query = encoded_book_query

         # nearest neighbour model
        self.nn_model = NearestNeighbors(n_neighbors=self.num_neighbours, metric=self.metric)

        # load data once?
        with open(self.data_pth, 'rb') as f:
            self.data = pickle.load(f)

    def recommend_books(self):

        embedded_data = self.data['embeddings']
        titles = self.data['titles']

        # fit model 
        self.nn_model.fit(embedded_data)

        # Find closest neighbors
        indices = self.nn_model.kneighbors(self.encoded_book_query, return_distance=False)
        
        # Return recommended titles
        return [titles[i] for i in indices[0]]
