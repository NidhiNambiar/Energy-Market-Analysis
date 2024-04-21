**INST 767 - Final Project**

**Summary about the Project**
In this project, we have an all-inclusive data system which results from the integration of four major data sources, being CVX (Chevron Corporation), SHEL (Royal Dutch Shell), XOM (ExxonMobil Corporation), and BP (BP plc). Our focus is on investigating the fluctuations and trends in crude oil and natural gas prices.
The implementation of this project has been structured into four distinct stages: data ingestion, transformation, storage, and analysis.




**Objective**
To utilize current data on gas prices, crude oil prices, and oil & gas company stock values to develop predictive models and analytical resources. These tools will be designed to predict market trends and offer strategic advice to tackle challenges in various fields such as oil & gas, transportation, manufacturing, and finance. The focus will be on discovering connections between these data points and vital economic indicators to aid in decision-making for cost control, investment planning, and operational enhancements.

This objective capitalizes on the data’s capability to deliver practical insights that can substantially shape business strategies and financial management across various sectors.











![#FFD700](https://via.placeholder.com/15/FFD700/000000?text=+)
`INGEST` 

In this ingest stage, a Python function has been implemented within Google Cloud Functions. This function is designed to retrieve daily crude oil and gass prices data from the APIs of the four companies. The data is stored in separate Google Cloud Storage buckets, one for each company.

In the attached file of this repository, you will find individual scripts for retrieving data for each company.

We have used the main following Packages: 
**google-cloud-storage**: This is the Google Cloud client library for interacting with Google Cloud Storage. It's used to store files in the cloud, manage them, and access cloud storage features programmatically.
**requests**: A popular Python HTTP library used for making HTTP requests to external services, such as APIs.
**os**: A standard library in Python that provides functions for interacting with the operating system. This includes reading or writing environment variables.
**datetime**: A standard library module in Python used for manipulating dates and times.
**flask**: A lightweight WSGI (Web Server Gateway Interface) web application framework. It's used to handle HTTP requests when the function is deployed as a Google Cloud Function.








![#FFD700](https://via.placeholder.com/15/FFD700/000000?text=+)
`TRANSFORM`






![#FFD700](https://via.placeholder.com/15/FFD700/000000?text=+)
`STORAGE `






![#FFD700](https://via.placeholder.com/15/FFD700/000000?text=+)
`ANALYSIS`




 

