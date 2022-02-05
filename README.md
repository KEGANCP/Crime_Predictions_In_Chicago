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
  - Dash-Bootstrap-Components
  - Dash-daq
  - Plotly
  - Gunicorn 
  - Joblin
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
  - app.py is required to initialize the Dash application.
  - procfile with run.py is used to deploy the application.
  - requirements.txt describes all Python dependencies to run the app successfully.
  - Contents within "pages" folder are required for the layout of each page within the webpage.
  - The predictions within our interactive dashboard are made possible by utilizing a machine learning algorithm saved via pipeline, and recalled within our prediction page.
- Further details to deploy Dash [here](https://dash.plotly.com/deployment) 
- WHAT .PY FILE NEEDS TO BE RUN IN ORDER TO DEPLOY THE DASHBOARD?
-----

## Datasets

City of Chicago Crime - https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-Present/ijzp-q8t2

Chicago O'Hare Weather Data - https://www.ncdc.noaa.gov/cdo-web/datasets/GHCND/stations/GHCND:USW00094846/detail

Crime Classification Codes - https://gis.chicagopolice.org/pages/crime_details

Used to classify violent crimes - https://chicagopd.maps.arcgis.com/apps/dashboards/8ed0652c9b2a4bc6bf1173e6aae6add4

Chicago Community Data - https://datahub.cmap.illinois.gov/dataset/community-data-snapshots-raw-data/resource/8c4e096e-c90c-4bef-9cf1-9028d094296e


---
## ETL & Database Creation

Using the data_cleaner notebook, all datasets required cleanup prior to analysis. the weather data was cleaned to provide only the pertinent columns, Crime data bucketed by violence status and community data trimmed down to a reference table. Below are samples of code utilized in order get to our clean dataset.
<p align="center">
  <img src="https://github.com/KEGANCP/Crime_Predictions_In_Chicago/blob/main/Resources/Clean_Weather_Snip.png" alt="CleanWeather"/>
</p>

<p align="center">
  <img src="https://github.com/KEGANCP/Crime_Predictions_In_Chicago/blob/main/Resources/Violent_V_Nonviolent.png" alt="ViolentVsNonViolent"/>
</p>

Once the data was cleaned, we used SQAlchemy to connect our cleaned dataframes directly to our SQL database in Postgres. Once all of our tables were loaded into SQL they were joined using the query file to create a master table used for analysis and our machine learning algorithms.
<p align="center">
  <img src="https://github.com/KEGANCP/Crime_Predictions_In_Chicago/blob/main/Resources/data_to_sql.png" alt="SQLConnection"/>
</p>

ERD:
<p align="center">
  <img src="https://github.com/KEGANCP/Crime_Predictions_In_Chicago/blob/AustenM/data/crime_database_erd.png" alt="ERD"/>
</p>

Join Query:
<p align="center">
  <img src="https://github.com/KEGANCP/Crime_Predictions_In_Chicago/blob/main/Resources/sql_query.png" alt="SQLQuery"/>
</p>

---

## Preliminary Analysis


The above-mentioned data cleaning allowed for some preliminary Machine Learning model tests. The below is a sample of code showing our Confusion Matrix with an accuracy score of 65%. 
<p align="center">
  <img src="https://github.com/KEGANCP/Crime_Predictions_In_Chicago/blob/main/Resources/CM.png" alt="CM"/>
</p>

Additional exploration of the dataset using Tableau was used to get a better picture of our information and A preliminary dashboard was created to also visualize our findings.

<p align="center">
  <img src="https://github.com/KEGANCP/Crime_Predictions_In_Chicago/blob/main/Resources/images%20for%20slides/prelim_tableau.jpg" alt="prelim"/>
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
- Model choice:  After an exploration of Logistic Regression, which predicted everything as violent, we switched gears and tried a decision tree model to sort through the features.When we plugged in the Random Forest Classifier, which runs efficiently on larger datasets like ours, we had much better results.Random Forest is fast and can show feature importances. However, the predictions it makes are always in the range of the training set.
- Accuracy goal was 75% to be moderately certain of our prediction (more than just a guess)
- Explanation of changes in model choice 
  - The Random Forest Classifier achieved an accuracy score of 65.5% when we ran our sample dataset.
  - Once connected to the database and running on our 3-year dataset, the accuracy dropped to 62.8%.
  - Several attempts were made to try to adjust the model to attain a higher accuracy rate. The estimators were raised to 300, which only had a minimal effect (63.24%)
  - Ultimately our model did not attain our goal of 75%, which was disappointing. The dataset did not allow any closer association between the weather and the violence status. We would not want to predict whether a crime would be violent or not with so low an accuracy.
  - Looking back at our questions, the third question stood out when looking back at the data, “Can we predict the number of crimes based on the community and weather?”. With a crime count being a continuous target, we switched our model to the Random Forest Regressor 
- Description of model training
  - This model was trained with
    - a new target of "Crimes_per_day" 
    - the features of Community Area, Average Teperature, Month, Day, and Weekday
- Description of current Accuracy Score
  - Regression models do not use accuracy like classification models. Instead different metrics are computed, we used the MAPE(Mean Absolute Percentage Error) to calculate the accuracy. This ended up being 86.87%, well above our 75% goal for predictions.

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
