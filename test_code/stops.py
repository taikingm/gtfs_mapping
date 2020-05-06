import geopandas as gpd
def stop_points(stops):
    stops_gdf = gpd.GeoDataFrame(
        stops,
        crs=4326,
        geometry=gpd.points_from_xy(stops.stop_lon, stops.stop_lat)
    )
    return stops
