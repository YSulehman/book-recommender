# Book Recommender
A web app book recommender. 

## Dataset
The dataset used here is a Kaggle dataset, publicly available here: [goodreads dataset](https://www.kaggle.com/datasets/jealousleopard/goodreadsbooks?resource=download)

To pre-process the data, run the following command:

```
python backend/src/preprocess_data.py --input_file path_to_raw_data --save_file dest_path_clean_data
```

## Backend 
The application uses [Sentence Transformers](https://huggingface.co/sentence-transformers) to create vector embeddings of the data. Unsupervised KNN is used to generate the book 
recommendations. 

## Installation and deploylment

*Instructions to be added*

<!-- Should be able to use free tier of AWS. 

- AWS ECS to run lightweight containers,
- AWS S3 free tier.

## Questions:
1. embedded query features must match embedded data... what if embedded data has more than titles?
2. how to set up model as rest api? what is uvicorn? different ports?
3. html and javascript basics: how to take user search input as argument for js function? (PROGRESS).
4. follow up from 3.; look into WebSockets
5. distinction between dataset location for local development vs deploying on cloud database?

To Dos:
1. create vector embedding of data. (DONE),
2. implement knn (unsupervised), (DONE)
3. set up rest api via fastapi, (Done ish... how to display results in a list format? Could be frontend task.) (DONE)
4. write front-end interface code (test locally) (DONE)
5. read up more on websockets (javascript client and python backend) + how to improve frontend UI (have centred + some colour)?
6. create AWS free tier account, 
7. containerise model via docker ? 
8. set up aws endpoint etc.,...deploy!


## Approach (backend):

1. Create vector embeddings for books in dataset.
2. user give prompt -> embed -> perform k-nn 
3. return results along with metadata, etc. 

## Frontend:

1. receives user input
2. send request to backend API
3. display recommendations. -->