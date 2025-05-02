import os
import argparse
import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer


def normalise_numeric_values(data_frame: pd.DataFrame, column: str) -> np.ndarray :
    """
    normalise numerical columns in the dataframe, e.g. book ratings, and convert to numpy
    array
    """
    # first convert to numeric 
    data_frame[column] = pd.to_numeric(data_frame[column], errors='coerce')

    # fill NaN with mean 
    mean_val = data_frame[column].mean()
    data_frame[column] = data_frame[column].fillna(mean_val)

    np_array = data_frame[column].to_numpy(dtype=float)

    # now normalise 
    np_array = (np_array - np.min(np_array)) / (np.max(np_array) - np.min(np_array))

    # reshape two dimensional
    np_array = np_array.reshape(-1,1)

    return np_array

def preprocess(file: str, columns: list) -> pd.DataFrame:

    # check file exists 
    if os.path.exists(file):
        df = pd.read_csv(file)
    else:
        raise FileNotFoundError
    
    # remove any leading spaces 
    df.columns = df.columns.str.strip()
    
    # get subset of data we're interested in but check specified columns are there 
    missing_columns = [col for col in columns if col not in df.columns]
    if missing_columns:
        raise KeyError(f"Missing required columns: {missing_columns}")
    
    else:
        df_subset = df[[columns]]

    return df_subset

def run_embed_data(args) -> None:
    """
    creates vector embedding of the dataset
    """

    # initial preprocess of dataframe 
    df = preprocess(args.input_file, ['title', 'authors', 'publisher', 'language_code', 'average_rating', 'num_pages'])

    # instantiate model
    model = SentenceTransformer("all-MiniLM-L6-v2")

    authors = df['authors'].astype(str).tolist()
    publishers = df['publisher'].astype(str).tolist()
    languages = df['language_code'].astype(str).tolist()

    author_embeddings = model.encode(authors)
    publisher_embeddings = model.encode(publishers)
    language_embeddings = model.encode(languages)

    # now handle numerical columns 
    normalised_ratings = normalise_numeric_values(df, 'average_rating')
    normalised_page_count = normalise_numeric_values(df, 'num_pages')

    # concatenate all data into single arrray horizontally 
    embedded_data = np.concatenate([author_embeddings, publisher_embeddings, language_embeddings, normalised_ratings, normalised_page_count], 
                            axis=1)
    
    # save embedded data
    np.save(args.save_file, embedded_data)

if __name__=="__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--input_file", type=str, required=True, help='path to raw csv data')
    parser.add_argument("--save_file", type=str, required=True, help='destination file of embedded data')

    args= parser.parse_args()

    # run embedding 
    run_embed_data(args)
