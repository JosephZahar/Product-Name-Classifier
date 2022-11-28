 <img alt="Python" src="https://img.shields.io/badge/Python%20-%2314354C.svg?style=flat-square&logo=python&logoColor=white" /> <img alt="Jupyter" src="https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white&style=flat" /> <img alt="Snowflake" src="https://img.shields.io/badge/Snowflake-29B5E8?logo=Snowflake&logoColor=white&style=flat" />
  
 
# Product-Name-Classifier
The focus of this repository is to provide a detailed methodology of the steps to automate the categorisation of product names into different granular levels. The project consists of predicting product name categories and then feed them back into our Snowflake data warehouse.

 <img width="1270" alt="Screen Shot 2022-11-28 at 11 01 49 AM" src="https://user-images.githubusercontent.com/70657426/204236758-ef18ee3c-ceb0-4e6b-ae12-c27e4599e039.png">

## Table of Contents

- [Overview](#overview)
- [Built With](#built-with)
- [Features](#features)

## Overview
### Webscrapping Product Names
Before starting to build our classifier, we need to make sure that we have the right quality and amount of data to train our model. In this step, we are going to webscrape different type of Food and Drinks from several websites. 

### Semi-labelling the Data
Next, we will use a heuristic approach to label part of our trainning data before feeding it to the model. 

### Building the Naïve Bayes Models
Once the data is ready and preprocessed, we will create a pipeline that vectorise our text data and then send it for training. We also propose a grid search approach to obtain sub-optimal hyperparameters. These models will then be evaluated and modified for higher accuracy.

### Deploying the model to Snowflake
Once the models have yielded to the desired accuracy, we will deploy the model to our Snowflake data warehouse so that every time new products are 

### Built With
- Data Processing & Manipulation: [Numpy](https://numpy.org), [Pandas](https://pandas.pydata.org)
- Static and Dynamic Webscrapping: [BeautifulSoup](https://pypi.org/project/beautifulsoup4/), [selenium](https://pypi.org/project/selenium/)
- ML model: [sklearn](https://scikit-learn.org/stable/)
- Deploying to Snowflake: [snowflake.connector](https://docs.snowflake.com/en/user-guide/python-connector.html)

## Features
Both models yields to a >90% accuracy, reducing the cost of manually labelling text data (product names) while providing a model based on probabilities and historical data instead of heuristic approaches.
