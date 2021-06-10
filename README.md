# web-scraping-challenge
Week 12 MongDB and Web Scraping Homework

> Created by Dale Currigan  
> June 2021  
  
![web](/Resources/mission_to_mars.png)    

## Table of contents  
* [Project Intro](#Project-Intro)  
* [Project Structure](#Project-Structure)  
* [Setup](#Setup)  
* [Websites Scraped](#Websites-Scraped)  
* [Contributors](#Contributors)  
* [Status](#Status)  

# Project Intro
This project covers the week 12 MongoDB and Webscraping homework project - Mission to Mars
  
The project briefing was as follows:  
  
*In this assignment, you will build a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. The following outlines what you need to do.* 

The project includes the following elements:  
* Webscraping of:
   - NASA Mars News  
   - JPL Mars Space Images  
   - Mars Facts  
   - Mars Hemispheres  
* MongoDB and Flask Application  
  
# Project Structure  
```
web-scraping-challenge   
|  
|    
|__ mission_to_mars.ipynb               # Jupyter Notebook for the project
|__ app.py                              # The Flask app for the project 
|__ scrape_mars.py                      # Scrape functionality for the Flask app
|__ README.md                           # This file
|
|__ templates/                          # Directory for html docs
|   |__ index.html                      # App homepage
|
|__ static/                              
|   |__css/                             # Directory for css stylesheets
|      |__ booststrap.css               # Boostswatch 'United' boostrap template 
|      |__ styles.css                   # Custom styles for the app           
|
|__ Screenshots/                        # Directory containing screenshots of the app
|   |__ screenshot_1.png
|   |__ screenshot_2.png
|   |__ screenshot_3.png
|
|__ Resources/                          # Directory for images contained in the Readme   
|   |__ meission_to_mars.png                  
|

``` 
  
# Setup 
  
##### Part 1 - Webscrape  
* Open mission_to_mars.ipynb as a Jupyter Notebook  
* Once opened, Select *Restart & Run All* from Kernel menu to view the results  
  
  
##### Part 2 - MongoDB and Flask Application  
* First initialise a Mongo databse by typing 'mongod' at the terminal (requires installation of MongoDB)
* Run app.py with the commond 'python app.py' from the terminal  
* The page will initially be empty except for the title and 'Get New Data' button as the Mongo database is not yet populated with data  
* Click the 'Get New Data' button to perform a scrape of the four sites  
* The App will load the data to the page once the scrape is complete
* The scrape cna be repeated as desired    

# Websites Scraped  
  
|No|Name|Link|
|-|-|-|
|1| NASA Mars News         |https://redplanetscience.com/| 
|2| JPL Mars Space Images  |https://spaceimages-mars.com/|
|3| Mars Facts             |https://galaxyfacts-mars.com/|  
|4| Mars Hemispheres       |https://marshemispheres.com/|  

   
# Contributors  
Dale Currigan 
[@dcurrigan](https://github.com/dcurrigan) 
<dcurrigan@gmail.com>


## Status
Project is: 
````diff 
+ Completed
````

