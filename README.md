# Book Recommender
The aim of this project is to incorporate a back-end book recommender with a front-end web app that allows users to find book recommendations based on book titles, genre or 
other keywords.

Could use this kaggle dataset: [Books Dataset](https://www.kaggle.com/datasets/elvinrustam/books-dataset?select=BooksDataset.csv). This will act as 
knowledge base that the system uses when users enter a prompt. 
Have opted for this [goodreads scraped dataset](https://www.kaggle.com/datasets/jealousleopard/goodreadsbooks?resource=download)
Should be able to use free tier of AWS. 

- AWS ECS to run lightweight containers,
- AWS S3 free tier.

## Questions:
- embedded query features must match embedded data... what if embedded data has more than titles?
- how to set up model as rest api? what is uvicorn? different ports?
- distinction between dataset location for local development vs deploying on cloud database?

To Dos:
1. create vector embedding of data. (DONE),
2. implement knn (unsupervised), (DONE)
3. set up rest api via fastapi,
4. write front-end interface code (test locally)
5. create AWS free tier account, 
6. containerise model via docker ? 
7. set up aws endpoint etc.,...deploy!


## Approach (backend):

1. Create vector embeddings for books in dataset.
2. user give prompt -> embed -> perform k-nn 
3. return results along with metadata, etc. 

## Frontend:

1. receives user input
2. send request to backend API
3. display recommendations.