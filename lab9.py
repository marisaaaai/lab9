import plotly.graph_objects as go

import pandas as pd

df = pd.read_csv('ciudades_freq.csv')
df['text'] = df['Ciudades'] + '<br>Frecuencia ' + (df['Freq']).astype(str)
limits = [(0,2),(3,10),(11,20),(21,50),(50,3000)]
colors = ["royalblue","crimson","lightseagreen","orange","lightgrey"]
cities = []
scale = 5000

fig = go.Figure()

for i in range(len(limits)):
    lim = limits[i]
    df_sub = df[lim[0]:lim[1]]
    fig.add_trace(go.Scattergeo(
        locationmode = 'USA-states',
        text = df_sub['text'],
        marker = dict(
            size = df_sub['Freq'],
            color = colors[i],
            line_color='rgb(40,40,40)',
            line_width=0.5
        )))
    print(df_sub['text'])

fig.update_layout(
        title_text = '2014 US city populations<br>(Click legend to toggle traces)',
        showlegend = True,
        geo = dict(
            scope = 'usa',
            landcolor = 'rgb(217, 217, 217)',
        )
    )

fig.show()