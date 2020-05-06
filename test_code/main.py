import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches
import warnings
import requests
import matplotlib.cm as cm
import matplotlib.colors as colors
import folium

from test_code.stops import stop_points
from test_code.routes import shape_to_gdf

#Read in all necessary data from GTFS folder
agency = pd.read_csv('/Users/matthewroosa/Documents/SAVI Python Geospatial/gtfs_mapping/notebook example/ferry_gtfs/agency.txt')
routes = pd.read_csv('/Users/matthewroosa/Documents/SAVI Python Geospatial/gtfs_mapping/notebook example/ferry_gtfs/routes.txt')
shapes = pd.read_csv('/Users/matthewroosa/Documents/SAVI Python Geospatial/gtfs_mapping/notebook example/ferry_gtfs/shapes.txt')
stops = pd.read_csv('/Users/matthewroosa/Documents/SAVI Python Geospatial/gtfs_mapping/notebook example/ferry_gtfs/stops.txt')
trips = pd.read_csv('/Users/matthewroosa/Documents/SAVI Python Geospatial/gtfs_mapping/notebook example/ferry_gtfs/trips.txt')



#stops, convert to 4326 in case it was in some other format
sjson = stop_points(stops).to_json()
rjson = shape_to_gdf(shapes, trips, routes).to_json()

# folium
m = folium.Map(
    location=[40.772, -73.9972],
    zoom_start=11,
    tiles='Stamen Terrain')
folium.GeoJson(
    sjson,
    name='geojson',
    style_function=lambda feature: {

    }
).add_to(m)
folium.GeoJson(
    rjson,
    name='geojson',
    style_function=lambda feature: {
        'color': 'black'  # rjson['route_color']
    }
).add_to(m)

m