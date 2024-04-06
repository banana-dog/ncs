import pandas as pd
import re
from gensim import corpora, models, similarities
from gensim.utils import tokenize


def tokenize_in_df(strin):
    try:
        return list(
            tokenize(
                strin,
            )
        )
    except:
        return ""


df = pd.read_csv("base.csv", sep=",", names=["names", "text"])[["names", "text"]]
df_1 = pd.read_csv("to_search_for.csv", sep=",", names=["names", "source", "text"])[
    ["names", "source", "text"]
]

df["tokens"] = df["text"].apply(tokenize_in_df)

dictionary = corpora.Dictionary(df["tokens"])
feature_cnt = len(dictionary.token2id)
corpus = [dictionary.doc2bow(text) for text in df["tokens"]]
tfidf = models.TfidfModel(corpus)
index = similarities.SparseMatrixSimilarity(tfidf[corpus], num_features=feature_cnt)

for text in df_1["text"]:
    kw_vector = dictionary.doc2bow(tokenize(text))
    df[text] = index[tfidf[kw_vector]]
for i in range(df_1.shape[0]):
    df = df.sort_values(by=df_1["text"][i], ascending=False)
    print(
        "\nThe "
        + df_1["names"][i]
        + " function is probably contained in one of these files:\n"
    )
    print(df.head(3)["names"].to_string(index=False))

    print("\nActual source:\n" + df_1["source"][i])
