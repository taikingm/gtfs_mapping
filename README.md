# Mapping GTFS Data using GeoPandas and Folium

The **purpose of this project** is to visualize transit routes by utilizing GTFS data hosted on [Transit Feed](https://transitfeeds.com/feeds) with Pandas, GeoPanas, and Folium.

---

## Executive Summary

I would like to automate the task of producing a transit route map out of GTFS files. My initial goal will be to write a set a code that will read in the routes, stops, and timetable for each GTFS feed available. Eventually, I would like to try to be able to calculate on time rates of each transit, potentially a timeline map of the day of moving points showing the movement of the vehicles. I am woking on this project to better understand the structure of transis feed data, learning how to create and interactive map of a transit system without having to try to find transit maps for each city.

## Background

I have always been interested in public transportation and how it's shaped by the city as well as how it shapes the city it's in. Creating an visualization of movement of the transit system allows people to estimate a lot of different aspects of the city from where the central distric is, where do people commute from, or how the region has been spreading over time. I do not have a lot of experience with GTFS data, but would like to find an standard way of displaying routes and movement as soon as reading in the GTFS file without going through the task of setting up the base map, reading the lines, gps points etc.

## Resources
List any possible articles, resources or analysis or anything useful and include links and perhaps annotate a sentence as to the key findings of this resource. Or if you cannot find any resources please mention.

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

* Pandas: Merging GTFS csv data
* GeoPandas: Geospatial analysis such as getting the centroid, converting file to GeoJSON format 
* Folium: Displaying the map and saving as HTML


#### Library Wish List
Also note any libraries or functionality that you may need that you're not sure exists. Try your best to articulate this in words. This will be helpful if I can provide any libraries to suggest for use in the project.

## Example:
