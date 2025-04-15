# Book Recommender
The aim of this project is to incorporate a back-end book recommender with a front-end web app that allows users to find book recommendations based on book titles, genre or 
other keywords.

Could use this kaggle dataset: [Books Dataset](https://www.kaggle.com/datasets/elvinrustam/books-dataset?select=BooksDataset.csv). This will act as 
knowledge base that the system uses when users enter a prompt. 
Should be able to use free tier of AWS. 

- AWS ECS to run lightweight containers,
- AWS S3 free tier.

Questions:
- distinction between dataset location for local development vs deploying on cloud database?

Approach (backend):

1. Create vector embeddings for books in dataset.
2. user give prompt -> embed -> perform k-nn 
3. return results along with metadata, etc. 

Frontend:

1. receives user input
2. send request to backend API
3. display recommendations.