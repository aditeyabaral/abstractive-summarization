import os
from pathlib import Path
import pandas as pd

articles_bbc = list()
summaries_bbc = list()
articles_allnews = list()
summaries_allnews = list()

df_bbc = pd.DataFrame()
df_allnews = pd.DataFrame()

for root, dirs, files in os.walk("."):
    for name in files:
        full_path = os.path.join(root, name)
        if "BBC News Summary" in full_path:
            if full_path.endswith(".txt"):
                if "Summaries" in full_path:
                    with open(full_path) as f:
                        content = f.read().strip()
                        summaries_bbc.append(content)
                elif "News Articles" in full_path:
                    with open(full_path) as f:
                        content = f.read().strip()
                        articles_bbc.append(content)
        else:
            if full_path.endswith(".csv"):
                temp_df = pd.read_csv(full_path)
                try:
                    summary = temp_df["SUMMARY"].values.tolist()
                    article = temp_df["TEXT"].values.tolist()
                    summaries_allnews.extend(summary)
                    articles_allnews.extend(article)
                except:
                    pass

print(len(articles_bbc), len(summaries_bbc))
print(len(articles_allnews), len(summaries_allnews))

df_bbc["TEXT"] = articles_bbc
df_bbc["SUMMARY"] = summaries_bbc

df_allnews["TEXT"] = articles_allnews
df_allnews["SUMMARY"] = summaries_allnews

df_bbc.to_csv("bbc_news.csv")
df_allnews.to_csv("all_news.csv")
