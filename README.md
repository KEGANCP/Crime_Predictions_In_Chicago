<p align="center">
  <img src="https://github.com/KEGANCP/Crime_Predictions_In_Chicago/blob/main/Resources/CRIMEPREDICTIONSBANNER.png" alt="HEADER"/>
</p>

# Project 
Crime Predictions in Chicago based on specific weather conditions via Machine Learning.

We have selected this topic to determine what correlation certain weather patterns have on violent crimes committed within Chicago. Our analysis could be useful for a wide range of purpose; from those seeking potential vacation travel to Chicago, to law enforcement better equipped to forecast violent crime within their precinct.
This topic will allow the utilization of many data analytic tools and functions from optimizing data in Pandas and utilizing Python to initiate Machine Learning models, to providing visualizations within Tableau & utilizing SQL to query against the database. 

View our interactive dashboard(s) [here](https://chicagocrimepredictions.herokuapp.com)

Our goal is to utilize Machine Learning to predict future crimes within Chicago based on specific weather conditions.
In order to generate the desired findings we will be using the below datasets to analyze and test through different machine learning methods.


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
- Run the chicago_crime_queries.sql file in PostgreSQL to create the joined table for further analysis and machine learning.
- For Machine Learning:
  - verify that your Python environment has sklearn loaded in it
  - make sure PostgreSQL is running and "chicago_crime" database is connected
  - open up "Random_Forest.ipynb" file in Jupyter Notebook 
  - click on "Kernel" tab and select "Restart & Run All"
- How to deploy Dash (by Plotly) via Heroku
  - Tools needed to install
    - Heroku
    - Dash
    - Dash-Bootstrap-Componenets
    - Dash-daq
    - Plotly  
    - Gunicorn 
    - Joblin
    - Scikit-Learn
  - Once all our app's dependencies are installed the below steps outline how to deploy our app remotely.
     - Our app will deploy with the following files: app.py, run.py, requirements.txt, and procfile.
     - Access your local project file via terminal.
     - Utilize the following steps to initialize our deploy via Heroku.
<p align="center">
  <img src="https://github.com/KEGANCP/Crime_Predictions_In_Chicago/blob/KeganDash/Resources/deploy.png" alt="deploy"/>
</p>
     - Once pushed you can view our dashboard at https://my-dash-app.herokuapp.com (changing "my-dash-app" to the previously created unique name. Further details to deploy Dash [here](https://dash.plotly.com/deployment)

-----

## Datasets

City of Chicago Crime - https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-Present/ijzp-q8t2

Chicago O'Hare Weather Data - https://www.ncdc.noaa.gov/cdo-web/datasets/GHCND/stations/GHCND:USW00094846/detail

Crime Classification Codes - https://gis.chicagopolice.org/pages/crime_details

Used to classify violent crimes - https://chicagopd.maps.arcgis.com/apps/dashboards/8ed0652c9b2a4bc6bf1173e6aae6add4

Chicago Community Data - https://datahub.cmap.illinois.gov/dataset/community-data-snapshots-raw-data/resource/8c4e096e-c90c-4bef-9cf1-9028d094296e

---

## Preliminary Analysis
Prior to utilizing the weather data, it was first cleaned to provide only the pertinent columns necessary for the initial analysis. Below is a sample of code utilized to drop columns in order get to our clean dataset.
<p align="center">
  <img src="https://github.com/KEGANCP/Crime_Predictions_In_Chicago/blob/main/Resources/Clean_Weather_Snip.png" alt="CleanWeather"/>
</p>

There was also optimization required for our crime data set. Seeing as how this data set was very large we began by dropping columns that would not be pertinent to our research. We also needed to identify "Violent Crimes" and "Non-Violent Crimes". This was archived with the code shown below:
<p align="center">
  <img src="https://github.com/KEGANCP/Crime_Predictions_In_Chicago/blob/main/Resources/Violent_V_Nonviolent.png" alt="ViolentVsNonViolent"/>
</p>

The above-mentioned data cleaning allowed for some preliminary Machine Learning model tests. The below is a sample of code showing our Confusion Matrix with an accuracy score of 65%. 
<p align="center">
  <img src="https://github.com/KEGANCP/Crime_Predictions_In_Chicago/blob/main/Resources/CM.png" alt="CM"/>
</p>

---

## Machine Learning
- Preliminary data preprocessing: 
  - With the question being a yes/no (violent/Non-Violent) based on weather, we knew that we were looking at predicting discrete outcomes. 
  - Initial exploration of the data showed that there were several columns that were similar in description to each other (several types of location, etc.), so we dropped them to eliminate noise.
- Preliminary feature engineering:
    - For some of the columns that were in string format, pandas “get_dummies” was utilized to preprocess the data(these were later eliminated when the columns weren’t strong on feature importance and did not appear to be significant)
    - NaN's were replaced with 0 
- Data was split based on the “Violence_Status” column:
    - The Target was the “Violence_Status” column
    - The Features were narrowed down by their feature importance and are “Community_Area”, “Average_Wind_Speed”, “ Average_Temperature”, “Fog_Ice_Freezing_Fog”, “Smoke_or_Haze”
- Model choice:  After an exploration of Logistic Regression, which predicted everything as violent, we switched gears and tried a decision tree model to sort through the features.When we plugged in the Random Forest Classifier, which runs efficiently on larger datasets like ours, we had much better results.
- Accuracy goal was 75% to be moderately certain of our prediction (more than just a guess)

---

## Dashboard Storyboard 

<a target="_blank" href="https://docs.google.com/presentation/d/1g3GqBM35xMLTo6jP8FhdkAf1CYKovgrgu2nAPzJwjTI/edit#slide=id.g25f6af9dd6_0_0">Dashboard Storyboard on Google slides<a/>

## Preliminary Dashboard Link 

<a target="_blank" href="https://public.tableau.com/app/profile/austen.marden/viz/chicago_crime_story_2/ChicagoCrimeDashboard?publish=yes">Tableau Dashboard<a/>

## Link to Google Slides

<a target="_blank" href="https://docs.google.com/presentation/d/1eTzayAK_KPfpSJd6vPzA7zdwXh-dtZpn5IW0fO2QbIA/edit?usp=sharing">Google Presentation Slides<a/>

---

## Team members
### ETL Process and Database Engineer - Austen Marden

 -  Github Link: https://github.com/austenmarden
 -  LinkedIn: https://www.linkedin.com/in/austen-marden/

### Dashboard Technician & Repo Management - Kegan Propster

 -  Github Link: https://github.com/SeanTFarr
 -  LinkedIn: https://www.linkedin.com/in/sean-farr-462171135/

### Machine Learning Algorithms and Presentation - Sean Farr

 -  Github Link: https://github.com/KEGANCP
 -  LinkedIn: https://www.linkedin.com/in/kegan-propster/
