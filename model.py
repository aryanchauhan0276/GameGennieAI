import os
import numpy as np
import pandas as pd

from functools import lru_cache
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


CSV_FILE = "playstore_games_with_descriptions.csv"
EMBEDDINGS_FILE = "gameembeddings.npy"


@lru_cache(maxsize=1)
def load_model():
    return SentenceTransformer("all-MiniLM-L6-v2")


@lru_cache(maxsize=1)
def load_data():

    df = pd.read_csv(CSV_FILE)

    df.columns = df.columns.str.strip()

    drop_cols = [
        "id",
        "genre",
        "rating",
        "reviews",
        "installs",
        "content_rating",
        "size",
        "current_version",
        "requires_android",
        "cost_label",
        "updated"
    ]

    df.drop(columns=drop_cols, inplace=True, errors="ignore")

    df["NameandDecription"] = (
        df["app_name"].fillna("")
        + " : "
        + df["description"].fillna("")
    )

    return df


@lru_cache(maxsize=1)
def load_embeddings():

    df = load_data()
    model = load_model()

    if os.path.exists(EMBEDDINGS_FILE):
        embeddings = np.load(EMBEDDINGS_FILE)
    else:
        embeddings = model.encode(
            df["NameandDecription"].tolist(),
            show_progress_bar=True,
            batch_size=32
        )

        np.save(EMBEDDINGS_FILE, embeddings)

    return embeddings


def solution(query, k=5):

    df = load_data()

    embeddings = load_embeddings()

    model = load_model()

    query_embedding = model.encode([query])

    similarity = cosine_similarity(
        query_embedding,
        embeddings
    )[0]

    top_indices = similarity.argsort()[-k:][::-1]

    games = []

    for idx in top_indices:
        games.append(df.iloc[idx]["app_name"])

    return games
