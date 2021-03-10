import youtube_dl
import pickle
import pandas as pd

pd.options.display.max_rows = 20
pd.options.display.max_columns = 10

with open('data/golfDB.pkl', 'rb') as f:
    data = pickle.load(f)

non_slow = data.loc[data["id"] % 2 == 0]
print(non_slow['id'])

youtube_path = "https://www.youtube.com/watch?v="

for id in non_slow['youtube_id']:
    url = youtube_path + id

    ydl_opts = {
        "outtmpl": f"data/{id}.mp4"
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])



