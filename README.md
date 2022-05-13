# Mapping GTFS Data using GeoPandas and Folium

The **purpose of this project** is to visualize transit routes by utilizing GTFS data hosted on [Transit Feed](https://transitfeeds.com/feeds) with Pandas, GeoPanas, and Folium.

---

## Executive Summary

This project was inteded to take in GTFS data to visualize the routes and stops of the transit system. 

## Background

I have always been interested in public transportation and how it's shaped by the city as well as how it shapes the city it's in. Creating a visualization of movement of the transit system allows people to estimate a lot of different aspects of the city from where the central distric is, where do people commute from, or how the region has been spreading over time. I do not have a lot of experience with GTFS data, but would like to find a standard way of displaying routes and movement as soon as reading in the GTFS file without going through the task of setting up the base map, reading the lines, gps points etc.

## Resources

#### Resources List

* [Google Transit Feed Overview](https://developers.google.com/transit/gtfs)
* [GTFS.org ](http://gtfs.org/reference/static)
* Other online examples, tutorials on how to use the data.

#### Data Sources List
The code will currently read in any gtfs data in zip format, all sample data has been downloaded from transit feed:

* [Open Mobility Data](https://transitfeeds.com/)

## Technical Requirements

#### Python Libraries
Project consists of mostly three python libraries:

* [Pandas](https://pandas.pydata.org/): Merging GTFS csv data.
* [GeoPandas](https://geopandas.org/): Geospatial analysis such as getting the centroid, converting file to GeoJSON format.
* [Folium](https://python-visualization.github.io/folium/): Displaying the map and saving as HTML.

## Example Procedure:

In order to get the main.py to work you will have to:
1. Set up "data" folder in your directory.
2. Access [Transit Feed](https://transitfeeds.com/feeds) and download any GTFS data (would not work with realtime GTFS) from the list into your "data" directory. The zip file should be "example_data_gtfs.zip" for the code to run properly with minimal edits to the code. For example, if I wanted to download [Amarillo City Transit GTFS Feed](https://transitfeeds.com/p/amarillo-city-transit/1150), I will name my zip file "Amarillo_gtfs.zip".
3. Open main.py from the code directory.
4. Change the city name within `gtfs_mapping(city_name='amarillo')` on the last line of the code to whatever name you downloaded in step 2 (you will only need to enter in the name prior to _gtfs.zip).
5. Once the code runs, you should find a unzipped GTFS folder, and a html file of your transit data in your data folder.
6. The resulting map should looke something like this: 
   ![https://github.com/taikingm/gtfs_mapping/blob/master/notebook_example/example_screenshot.png?raw=true](https://github.com/taikingm/gtfs_mapping/blob/master/notebook_example/example_screenshot.png?raw=true)
