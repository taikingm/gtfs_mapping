import geopandas as gpd
import pandas as pd


def shape_to_gdf(shapes, trips, routes):
    shapes_gdf = gpd.GeoDataFrame(
        shapes,
        geometry=gpd.points_from_xy(shapes.shape_pt_lon, shapes.shape_pt_lat)
    )
    shapes_gdf2 = shapes_gdf.groupby(['shape_id'])['geometry'].apply(lambda x: LineString(x.tolist()))
    shapes_gdf = gpd.GeoDataFrame(shapes_gdf2, geometry='geometry')
    # keeping trips infor only for each trips to take out trip_id
    trips_drop = trips.drop_duplicates(subset=['shape_id'])
    # merging trip_id on to shapes in order to merge into route.txt
    shape_merge = shapes_gdf.merge(trips_drop, left_on='shape_id', right_on='shape_id', how='outer')
    # dropping duplicate shapes to simplify route for this test
    shape_merge = shape_merge.drop_duplicates(subset=['route_id'])
    # Route lines merged with name, routes.txt
    shape_routes = shape_merge.merge(routes, left_on='route_id', right_on='route_id', how='inner')
    shape_routes.crs = {'init': 'epsg:4326'}
    return shape_routes
