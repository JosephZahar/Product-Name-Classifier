# Product-Name-Classifier
The focus of this repository is to provide a detailed methodology of the steps to automate the categorisation of product names into different granular levels. The project consists of predicting product name categories and then feed them back into our Snowflake data warehouse.

## Table of Contents

- [Overview](#overview)
- [Built With](#built-with)
- [Features](#features)
- [Contact](#contact)
- [Acknowledgements](#acknowledgements)

## Overview
### Webscrapping Product Names
Before starting to build our classifier, we need to make sure that we have the right quality and amount of data to train our model. In this step, we are going to webscrape different type of Food and Drinks from several websites. 

### Semi-labelling the Data
Next, we will use a heuristic approach to label part of our trainning data before feeding it to the model. 

### Building the Naïve Bayes Models
Once the data is ready and preprocessed, we will create a pipeline that vectorise our text data and then send it for training. We also propose a grid search approach to obtain sub-optimal hyperparameters. These models will then be evaluated and modified for higher accuracy.

### Deploying the model to Snowflake
Once the models have yielded to the desired accuracy, we will deploy the model to our Snowflake data warehouse so that every time new products are 
<!-- TODO: Add a screenshot of the live project.
    1. Link to a 'live demo.'
    2. Describe your overall experience in a couple of sentences.
    3. List a few specific technical things that you learned or improved on.
    4. Share any other tips or guidance for others attempting this or something similar.
 -->

### Built With
- Data Processing & Manipulation: [Numpy](https://numpy.org), [Pandas](https://pandas.pydata.org)
- Static and Dynamic Webscrapping: [BeautifulSoup](https://pypi.org/project/beautifulsoup4/), [selenium](https://pypi.org/project/selenium/)
- ML model: [sklearn](https://scikit-learn.org/stable/)
- Deploying to Snowflake: [snowflake.connector](https://docs.snowflake.com/en/user-guide/python-connector.html)

## Features
Both models yields to a >90% accuracy, reducing the cost of manually labelling text data (product names) while providing a model based on probabilities and historical data instead of heuristic approaches.
