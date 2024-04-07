import pandas as pd
import re
from gensim import corpora, models, similarities
from gensim.utils import tokenize


def custom_tokenize(text):
    tokens = re.findall(r"\b\w+\b|\S*\d+", text)
    return tokens


def tokenize_in_df(str_in):
    try:
        return list(
            custom_tokenize(
                str_in,
            )
        )
    except:
        return ""


df = pd.read_csv("base.csv", sep=",", names=["names", "link", "text"])[
    ["names", "link", "text"]
]
df_1 = pd.read_csv("to_search_for.csv", sep=",", names=["text"])["text"]

df["tokens"] = df["text"].apply(tokenize_in_df)
df = df[df["tokens"].apply(len) > 0]

dictionary = corpora.Dictionary(df["tokens"])
feature_cnt = len(dictionary.token2id)
corpus = [dictionary.doc2bow(text) for text in df["tokens"]]
tfidf = models.TfidfModel(corpus, smartirs="lpn")
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
    print(df.head(20)[["names", "link", df_1["text"][i]]].to_string(header=False))

    # print("\nActual source:\n" + df_1["source"][i])
