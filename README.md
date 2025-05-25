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

If Docker is not installed, you can do so by the following the instructions [here](https://docs.docker.com/get-started/get-docker/).

Build the docker file locally:

```
docker build -t your_image_name:tag .
```
Then push the image to an online registry, such as [Docker Hub](https://hub.docker.com/). The application was deployed via AWS EC2, instructions for setting up an instance can be found [here](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html).

After you ssh into your EC2 account pull the image:
```
docker pull your_image_name:tag
```
Finally, run the container exposing the appropriate port:
```
docker run -d -p host_port:container_port --name your_container_name your_image_name:tag
```