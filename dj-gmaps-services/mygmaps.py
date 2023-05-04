import gmaps
import gmaps.datasets

# Set up gmaps
gmaps.configure(api_key="AIzaSyDuH9RKXi2ywLIXZWoqi1g6JZ9cg_vVQGI")

# Create a map
fig = gmaps.figure()

# Display the map
fig



import gmaps
import gmaps.datasets

gmaps.configure(api_key='')
earthquake_df = gmaps.datasets.load_dataset_as_df('earthquakes')
earthquake_df.head()

locations = earthquake_df[['latitude', 'longitude']]
weights = earthquake_df['magnitude']
fig = gmaps.figure()
fig.add_layer(gmaps.heatmap_layer(locations, weights=weights))
fig