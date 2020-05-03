
# Assignment 04

# Project Proposal

![http://www.pratt.edu/tiny_mce/plugins/imagemanager/files/Light_brown_blue22.jpg](http://www.pratt.edu/tiny_mce/plugins/imagemanager/files/Light_brown_blue22.jpg)

The **purpose of this project** is to have some **well-written** and **well-documented code** in a GitHub repository that illustrates you can write some Python code. This project is for **your** Portfolio, so pick something you are **interested in** or that's **useful** (either in some professional work or automating some task). [Learn how the project is evaluated (rubric)](https://github.com/pratt-savi-810/pratt-savi-810-2020-03-project).


#### Project Routes

There's a couple of routes you can go;

1. **Creating a Tool to Automate a Task** - usually for some task automation, less an analysis, more data engineering. 
2. **Performing Data Analysis to Answer a Research Question** - this type of project requires plots and data insights. 

Since writing the code is the challenging part. Do not think about this in scope of a normal project. **Keep your scope focused!** Keep it limited in functionality and if you finish early, you can add more features. I've seen students go down some pretty deep rabbit holes and emerge with some very disorganized projects. You could have only 30 lines of code or so, and still have a great project so long as the code is well written and the doc's are informative and it has some functionality that's useful in some capacity. Most likely someone such as a hiring manager will only glance at your Repository, so you want it to be organized and clean and very clear as to its purpose. 

## Assignment 04 Submission
You will **Fork** and **Clone this Repo** and **edit this README.md Markdown file**. This is your submission, just the link to your forked Repo and edited README.md file. This project should be the edited version of this README.md (**Markdown**) file. 

#### Learn more about [Markdown](https://www.markdownguide.org/). 

Most code editors allow editing of Markdown files, some recommended editors are;

* [Atom](https://atom.io/)
* [MacDown](https://macdown.uranusjr.com/)
* [Visual Studio Code (VS Code)](https://code.visualstudio.com/)
* [StackEdit (edit in-browser)](https://stackedit.io/)
* [Dillinger (edit in-browser)](https://dillinger.io/)
* You can even edit inside of [GitHub](https://github.com/). 

Your Assignment 04 Deliverables are listed below:

# Deliverables

You should edit the following items in-line and substitute any of the provided text with your response below for your README.md Assignment 04 submission. 


---

## Executive Summary

I would like to automate the task of producing a transit route map out of GTFS files. My initial goal will be to write a set a code that will read in the routes, stops, and timetable for each GTFS feed available. Eventually, I would like to try to be able to calculate on time rates of each transit, potentially a timel

- **Why** are you doing this project? 
- **How** do you imagine you'll accomplish this project? 
- Is this a project **Creating a Tool to Automate a Task** or **Performing Data Analysis to Answer a Research Questio**? 

I would like to automate the task of producing a transit route map out of GTFS files. My initial goal will be to write a set a code that will read in the routes, stops, and timetable for each GTFS feed available. Eventually, I would like to try to be able to calculate on time rates of each transit, potentially a timeline map of the day of moving points showing the movement of the vehicles. I am woking on this project to better understand the structure of transis feed data, learning how to create and interactive map of a transit system without having to try to find transit maps for each city.

## Background

I have always been interested in public transportation and how it's shaped by the city as well as how it shapes the city it's in. Creating an visualization of movement of the transit system allows people to estimate a lot of different aspects of the city from where the central distric is, where do people commute from, or how the region has been spreading over time. I do not have a lot of experience with GTFS data, but would like to find an standard way of displaying routes and movement as soon as reading in the GTFS file without going through the task of setting up the base map, reading the lines, gps points etc.

## Resources
List any possible articles, resources or analysis or anything useful and include links and perhaps annotate a sentence as to the key findings of this resource. Or if you cannot find any resources please mention. 

#### Resources List

* [Google Transit Feed Overview](https://developers.google.com/transit/gtfs)
* [GTFS.org ](http://gtfs.org/reference/static)
* Other online examples, tutorials on how to use the data.
 
## Input Data 

#### Data Sources List 
List any possible data including links with any input data sources you'll be using. 

* [Open Mobility Data](https://transitfeeds.com/)
* [MTA Data Downloads](http://web.mta.info/developers/download.html) 
  

## Technical Requirements

#### Python Libraries
List any Python libraries you think you may need. Desribe what you may use them for. 

* [GTFS Kit](https://mrcagney.github.io/gtfs_kit_docs/index.html#examples) Read in GTFS Data, conveting them into Geo DataFrames.
* [GTFS Realtime Bindings](https://github.com/MobilityData/gtfs-realtime-bindings/tree/master/python): To be able to read in real time transit feed.


#### Library Wish List
Also note any libraries or functionality that you may need that you're not sure exists. Try your best to articulate this in words. This will be helpful if I can provide any libraries to suggest for use in the project. 

* Interactive mapping library that will allow overlays of points, and lines, but also be able to display info on top.
* Library that will be able to display points movement by time.
  

## Measuring Success: 

- How will you measure your project's sucess?

My initial goal will be to display an map of transit routes for any datafeed that is entered into the script.
Secondary goal will be to produce point movement (if data exists) for each day of GTFS data produced. <br>
When those goals area achieved, I would like to try to create an more interactive map where a viewer can click on a certain route and receive more information of the route such as time tables that are contained in the data.

## Project Execution Plan Outline
Please include a short outline describing the steps you'd imagine going through. 

Could be as simple as;

```
- Research on data structure and example uses on the web
- Trying out displaying data on simple plots, getting a grasp on how the data will work
- Look into libraries that will best fit the list of features
- Produce one static map
- Create a function that will run just by entering data source
- Start adding in additional features