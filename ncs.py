import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors


class CodeSearchEngine:
    def __init__(
        self,
        n_neighbors=1,
        ngram_range=(1, 2),
        min_df=1,
        max_df=1,
        token_pattern=r"\b\w+\b|\S*\d+",
    ):
        """n_neighbors must be less than or equal to number of documents in the database"""
        self.n_neighbors = n_neighbors
        self.vectorizer = TfidfVectorizer(
            ngram_range=ngram_range,
            min_df=min_df,
            max_df=max_df,
            token_pattern=token_pattern,
        )
        self.neigh = NearestNeighbors(n_neighbors=n_neighbors, n_jobs=-1)

    def fit(self, X):
        """Build an index from an array of texts X to find neighbors late"""
        tfidf_index = self.vectorizer.fit_transform(X)
        self.neigh.fit(tfidf_index)

    def query(self, samples, n_results=1):
        """n_results must be less than n_neighbors"""
        tfidf = self.vectorizer.transform(samples)
        return self.neigh.kneighbors(tfidf, n_neighbors=n_results)


def print_results(df, res):
    for link, dist in zip(df["link"][res[1][0]], res[0][0]):
        print(f"{link} -> {dist}")


def main():
    database_path = "data/base.csv"
    queries_path = "data/to_search_for.csv"
    df = pd.read_csv(database_path, sep=",", names=["names", "link", "text"])[
        ["names", "link", "text"]
    ]
    samples = pd.read_csv(queries_path, sep=",", names=["text"])["text"].values

    neighbors_num = 10
    search_engine = CodeSearchEngine(neighbors_num)
    search_engine.fit(df["text"])
    res = search_engine.query(samples, neighbors_num)

    print_results(df, res)


if __name__ == "__main__":
    main()
