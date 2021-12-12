import plotly.graph_objects as go
import pandas as pd
import plotly.express as px


df = pd.read_csv('my_songs_db.csv')
artpop = df[df.genre == 'k-pop']
#art_pop_artists = artpop.artists.value_counts().insex()
art_pop_artists = list(artpop.artists.value_counts().index)
art_pop_songs = list(df.artists.value_counts())

labels_art_pop = art_pop_artists
values_art_pop = art_pop_songs

fig = go.Figure(data=[go.Pie(labels=labels_art_pop, values=values_art_pop)])
fig.show()

fig.write_html('exp.html')

