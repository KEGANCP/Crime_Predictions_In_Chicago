<p align="center">
  <img src="https://github.com/KEGANCP/Crime_Predictions_In_Chicago/blob/main/Resources/CRIMEPREDICTIONSBANNER.png" alt="HEADER"/>
</p>

# Topic 
Crime Predictions in Chicago based on specific weather conditions via Machine Learning.

We have selected this topic to determine what correlation certain weather patterns have on violent crimes committed within Chicago. Our analysis could be useful for a wide range of purpose; from those seeking potential vacation travel to Chicago, to law enforcement better equipped to forecast violent crime within their precinct.
This topic will allow the utilization of many data analytic tools and functions from optimizing data in Pandas and utilzing Python to initiate Machine Learning models, to providing vizualizations within Tableau & utilzing SQL to query against the database. 

# Goal
Our goal is to utilize Machine Learning to predict future crimes within Chicago based on specific weather conditions.
In order to generate the desired findings we will be using the below datasets to analyze and test through different machine learning methods.

[Chicago Weather Data](https://github.com/KEGANCP/Crime_Predictions_In_Chicago/blob/AustenM/data/clean_weather_data.csv)

[Crime Data SAMPLE](https://github.com/KEGANCP/Crime_Predictions_In_Chicago/blob/AustenM/data/sample_crime_data.csv)

[Logistic Regression SAMPLE](https://github.com/KEGANCP/Crime_Predictions_In_Chicago/blob/triangle/sample_logistic_reg.ipynb)

ERD:
<p align="center">
  <img src="https://github.com/KEGANCP/Crime_Predictions_In_Chicago/blob/AustenM/data/crime_database_erd.png" alt="ERD"/>
</p>



-----

## Instructions

### Tools Needed 
- Anaconda
- Jupyter Notebook
- Python Libraries
  - Pandas
  - SQAlchemy
  - Sci-Kit Learn
  - Dash
  - Plotly
- PostgreSQL
- Tableau


### Steps to Run
- Create a Database in PostgreSQL called "chicago_crime"
- Download the following raw CSV data files from the datasets listed below. 
  - "City of Chicago Crime"
  - "Chicago O'Hare Weather Data"
  - "Chicago Community Data"
- Run the data_cleaner.ipynb notebook in order to clean the raw data files and load the SQL database.
  - Create a config.py file with your PostgreSQL password.
  - Change the read_CSV file pathways to match your file locations.
- Run the chicago_crime_queries.sql file in PostgreSQL to create the joined table for futher analysis and machine learning.
- For Machine Learning:
  - verify that your Python environment has sklearn loaded in it
  - make sure PostgreSQL is running and "chicago_crime" database is connected
  - open up "Random_Forest.ipynb" file in Jupyter Notebook 
  - click on "Kernel" tab and select "Restart & Run All"
- INSERT DASHBOARD STEPS  
- INSERT TABLEAU STEPS


-----

## Datasets

City of Chicago Crime - https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-Present/ijzp-q8t2

Chicago O'Hare Weather Data - https://www.ncdc.noaa.gov/cdo-web/datasets/GHCND/stations/GHCND:USW00094846/detail

Crime Classification Codes - https://gis.chicagopolice.org/pages/crime_details

Used to classify violent crimes - https://chicagopd.maps.arcgis.com/apps/dashboards/8ed0652c9b2a4bc6bf1173e6aae6add4

Chicago Community Data - https://datahub.cmap.illinois.gov/dataset/community-data-snapshots-raw-data/resource/8c4e096e-c90c-4bef-9cf1-9028d094296e

## Preliminary Analysis
Prior to utilzing the weather data, it was first cleaned to provide only the pertinent columns necessary for the initial analysis. Below is a sample of code utilized to drop columns in order get to our clean dataset.
<p align="center">
  <img src="https://github.com/KEGANCP/Crime_Predictions_In_Chicago/blob/main/Resources/Clean_Weather_Snip.png" alt="CleanWeather"/>
</p>

There was also optimization required for our crime data set. Seeing as how this data set was very large we began by dropping columns that would not be pertinent to our research. We also needed to identify "Violent Crimes" and "Non-Violent Crimes". This was achived with the code shown below:
<p align="center">
  <img src="https://github.com/KEGANCP/Crime_Predictions_In_Chicago/blob/main/Resources/Violent_V_Nonviolent.png" alt="ViolentVsNonViolent"/>
</p>

The above mentioned data cleaning allowed for some preliminary Machine Learning model tests. The below is a sample of code showing our Confusion Matrix with an accuracy score of 65%. 
<p align="center">
  <img src="https://github.com/KEGANCP/Crime_Predictions_In_Chicago/blob/main/Resources/CM.png" alt="CM"/>
</p>


## Communication Potocols
- Primary daily communication through use of #Group-6 Slack chat.
- Working sessions every Monday and Wednesday from 7:00p-9:00p with an additional working session on Saturday from 8:00a-10:00a.

## Outline of Project with tools

1. Data collection via either CSV file or JSON format.
2. Data cleaning using Pandas
3. Database creation using SQL
4. Machine Learning model using Python/Jupyter Notebook/Sci-kit Learn
5. Visualize ML output using Tableau or JavaScript

## Roles and Members
### Circle Role - Austen Marden

 -  Segment 1: Creating a mock-up database including an ERD
 -  Segment 2: Continue to refine the analysis
 -  Segment 3: Creating a final dashboard
 -  Segment 4: Final touches on dashboard

### Square Role - Kegan Propster

 -  Segment 1: GitHub repo and creating branches
 -  Segment 2: Refine, train and test the ML model created in segment 1
 -  Segment 3: Tie up loose ends on github
 -  Segment 4: Finalize the Readme

### Triangle Role - Sean Farr

 -  Segment 1: Create a simple machine learning model
 -  Segment 2: Upscaling the project's SQL database
 -  Segment 3: Creating presentation of project
 -  Segment 4: Clean up Github repo
