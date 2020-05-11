import pandas as pd
import geopandas as gpd
import folium
import zipfile
from shapely.geometry import  LineString

# Read in all necessary data from GTFS folder
# Read in all necessary data from GTFS folder
city_name = 'ferry'
z = zipfile.ZipFile(f"{city_name}_gtfs.zip")
z.extractall(f"{city_name}_gtfs")

agency = pd.read_csv(f"{city_name}_gtfs/agency.txt")
routes = pd.read_csv(f"{city_name}_gtfs/routes.txt")
shapes = pd.read_csv(f"{city_name}_gtfs/shapes.txt")
stops = pd.read_csv(f"{city_name}_gtfs/stops.txt")
trips = pd.read_csv(f"{city_name}_gtfs/trips.txt")
# Taking agency name to save html file at the end.
html_name = agency['agency_name'][0]

# read in stops as gdf
stops_gdf = gpd.GeoDataFrame(
    stops,
    crs=4326,
    geometry=gpd.points_from_xy(stops.stop_lon, stops.stop_lat))

# Create GeoDataFrame from Shapes.txt
shapes_gdf = gpd.GeoDataFrame(
    shapes,
    crs=4326,
    geometry=gpd.points_from_xy(shapes.shape_pt_lon, shapes.shape_pt_lat)
)

# Create Linestring out of shape_id and shape_pt_sequence
shapes_gdf = shapes_gdf.groupby(['shape_id'])['geometry'].apply(lambda x: LineString(x.tolist()))
shapes_gdf = gpd.GeoDataFrame(shapes_gdf, geometry='geometry')

# keeping trips info only for each trips to take out trip_id
trips_drop = trips.drop_duplicates(subset=['shape_id'])

# merging trip_id on to shapes in order to merge into route.txt
shape_merge = shapes_gdf.merge(trips_drop, left_on='shape_id', right_on='shape_id', how='outer')

# dropping duplicate shapes to simplify route for this test
shape_merge = shape_merge.drop_duplicates(subset=['route_id'])

# Route lines merged with name, routes.txt
shape_routes = shape_merge.merge(routes, left_on='route_id', right_on='route_id', how='inner')
shape_routes.crs = {'init': 'epsg:4326'}

# stops, convert to 4326 in case it was in some other format
sjson = stops_gdf.to_json()

# routes converted to GeoJson
rjson = shape_routes.to_json()


# Function identifying centroid of routes to display original location of map
def get_feature_centroid(gdf):
    gdf['dissolve'] = 1
    center = gdf.dissolve(by='dissolve').centroid
    return center.x, center.y


# Getting Sentriod to display original coordinates for map.
x, y = get_feature_centroid(shape_routes)

# Setting up Basemap
m = folium.Map(
    location=[y, x],
    zoom_start=10,
    tiles='cartodbpositron')


# Function to return route color with # in front to display properly for leaflet style_function
def style_geojson(features):
    return {'color': f"#{features['properties']['route_color']}"}


# Display GeoJson of Routes
folium.GeoJson(
    rjson,
    name='Routes',
    style_function=style_geojson,
).add_to(m)

# Creating and displaying folium.Marker for every stop
for index, row in stops_gdf.iterrows():
    x, y = row['geometry'].centroid.x, row['geometry'].centroid.y
    folium.Circle(
        location=[y, x],
        radius=45,
        popup=" Station Name:" + row['stop_name'] + "Routes Served:",
        color='black',
        fill=True,
        fill_opacity=500,
    ).add_to(m)

m.save(f"{html_name}.html")
