**Project Overview**

This project is designed to develop predictive models and analytical resources by harnessing data on gas prices, crude oil prices, and the stock values of major oil and gas companies. The companies in focus include Chevron Corporation (CVX), Royal Dutch Shell (SHEL), ExxonMobil Corporation (XOM), and BP plc (BP). The project is structured into four distinct stages: data ingestion, transformation, storage, and analysis. Each stage plays a crucial role in turning raw data into insightful, actionable intelligence that helps in predicting market trends and formulating strategic advice.

**Data Sources**
The data for this project is retrieved from three main sources:
1.	Gas Prices: Daily gas price data.
2.	Crude Oil Prices: Daily crude oil price data.
3.	Stock Values: Daily stock prices of CVX, SHEL, XOM, and BP.
##System Architecture

**Ingest**
The data ingestion process is handled via Python scripts using standard libraries to make API calls. These scripts are deployed on Google Cloud using Cloud Functions, every 30 minutes using Cloud Scheduler, with data being temporarily stored in Cloud Storage buckets in JSON format before transformation.

**Transformation**
Data transformation is conducted using PySpark on Google Cloud's DataProc service, where we have employed cloud scheduler and dataproc workflows which trigger the creation of a compute engine which runs the jobs for all 4 stocks along with crude oil and natural gas. This stage aligns the data from their sources into a unified data model that supports our analytical objectives. Transformations are scheduled to run in accordance with the data ingest timings.

**Storage**
The transformed data is stored in Google Cloud's BigQuery, which provides a robust platform for large-scale data analytics using SQL. We have created 2 separate datasets to store the data. ‘crudedataset’ contains tables storing the crude oil price and natural gas price. Whereas ‘stock_767’ stores the open, close, high, low & volume for the 4 stocks which we are dealing with. The schema has been defined for all the tables to ensure that the datatype is correct, so that queries run properly.

**Analysis**
While in-depth analysis is not the core focus of this project, the data model allows for basic queries that can answer specific questions related to the impact of oil prices on stock values and more. Example SQL queries are provided below to demonstrate this capability:
a.	Is there a correlation between crude oil prices and the stock prices of these companies?
b.	Determine if there are consistent patterns of volume preceding or following price changes.
c.	Assess the liquidity of a stock by looking at the average volume. Higher volumes generally mean better liquidity, making it easier to execute trades without affecting the price too much.
