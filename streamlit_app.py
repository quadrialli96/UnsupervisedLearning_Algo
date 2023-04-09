import streamlit as st
import pandas as pd
from sklearn.cluster import KMeans
from plotly import graph_objects as go
import plotly.express

data = pd.read_csv("account_data.csv")
st.title("Medicaid Services in the United States")

with st.sidebar:
    cluster = st.select_slider(label="Number of Clusters", options=range(2, 11), value=2)
#ML ALGO
ml_algo = KMeans(n_clusters=6).fit(X = data[['LONGITUDE', 'LATITUDE']], sample_weight= data['MEDICAID PROVIDER ID'])
cluster_label = ml_algo.labels_

plot_df= data.copy()
plot_df['cluster']= cluster_label
plot_df.head()

colors = ['Blackbody','Bluered','Blues','Cividis','Earth','Electric','Greens','Greys','Hot','Jet','Picnic','Portland','Rainbow','RdBu','Reds','Viridis','YlGnBu','YlOrRd']

counter = 0
for cluster in plot_df['cluster'].unique():
    temp = plot_df[plot_df['cluster'] == cluster ]
    if counter == 0:
        fig = go.Figure(go.Densitymapbox(lat=temp['LATITUDE'], lon=temp['LONGITUDE'], radius=1, colorscale=colors[counter]))
        counter +=1
    else:
        fig.add_densitymapbox(lat=temp['LATITUDE'], lon=temp['LONGITUDE'], radius=10, colorscale=colors[counter])
        counter +=1

fig.update_layout(mapbox_style="carto-positron")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
st.plotly_chart(fig)
