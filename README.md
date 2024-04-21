# INST 767 - Final Project

## Summary about the Project

In this project, we've developed an all-inclusive data system resulting from the integration of four major data sources: CVX (Chevron Corporation), SHEL (Royal Dutch Shell), XOM (ExxonMobil Corporation), and BP (BP plc). This integration aims to explore the fluctuations and trends in crude oil and natural gas prices. The project is structured into four distinct stages: data ingestion, transformation, storage, and analysis. Each stage plays a crucial role in turning raw data into insightful, actionable intelligence that helps in predicting market trends and formulating strategic advice.

## Objective

The main objective is to harness current data on gas prices, crude oil prices, and the stock values of oil & gas companies to develop predictive models and analytical resources. We intend to build business questions to anticipate market trends and provide strategic guidance to address challenges in sectors such as oil & gas, transportation, manufacturing, and finance. The focus is on uncovering relationships between these data points and key economic indicators to assist in decision-making for cost control, investment planning, and operational enhancements. This objective leverages the data's ability to deliver practical insights that can significantly influence business strategies and financial management across various industries.

## 📊 Data Ingestion

In the ingestion stage, a Python function has been implemented within Google Cloud Functions. This function is designed to retrieve daily crude oil and gas prices data from the APIs of the four companies. The data is stored in separate Google Cloud Storage buckets, one for each company.

### Key Technologies Used:
- **google-cloud-storage**: Google Cloud client library for interacting with Google Cloud Storage.
- **requests**: A popular Python HTTP library used for making HTTP requests to APIs.
- **os**: Provides functions for interacting with the operating system, including environment variables.
- **datetime**: For manipulating dates and times.
- **flask**: A lightweight WSGI web application framework used in deploying Google Cloud Functions.

### Process Breakdown:
- Daily API calls to fetch data
- Data validation and preliminary processing
- Storage in designated cloud buckets

## 🔧 Data Transformation

In this stage, we have transformed the data into a unified data model, integrating data from the four different sources into a single model. The transformation of raw data into the data model was carried out using DataProc and PySpark, aimed at processing the data for efficient storage and subsequent analysis.

### Process Breakdown:
- Data cleaning and normalization
- Schema alignment across different datasets
- Integration into a unified data model

## 🗄️ Data Storage

We have established a database on Google Cloud to logically align with our data model. This setup ensures that our data is stored in a way that makes it easily and logically queryable.

### Process Breakdown:
- Database schema design
- Data loading and indexing
- Performance tuning and security settings

## 📈 Data Analysis

Our analysis is guided by business questions that are crucial for strategic decision-making. The analysis focuses on identifying patterns, trends, and correlations that could influence market behaviors and business decisions.

### Process Breakdown:
- Formulating and refining business questions
- Applying statistical and machine learning models
- Visualizing data trends and predictions
- Generating reports and insights for decision support

