# Project Overview

This project is designed to draw insights by harnessing data on gas prices, crude oil prices, and the stock values of major oil and gas companies. The companies in focus include Chevron Corporation (CVX), Royal Dutch Shell (SHEL), ExxonMobil Corporation (XOM), and BP plc (BP). The project is structured into four distinct stages: data ingestion, transformation, storage, and analysis. Each stage plays a crucial role in turning raw data into insightful, actionable intelligence that helps in predicting market trends and formulating strategic advice.

## Data Sources

The data for this project is retrieved from three main sources using the [Alphavantage API](https://www.alphavantage.co/):
1.	Gas Prices: Daily gas price data.
2.	Crude Oil Prices: Daily crude oil price data.
3.	Stock Values: Daily stock prices of CVX, SHEL, XOM, and BP.

## Data Pipeline Overview

![Untitled Jam 1](https://github.com/animeshnandan/inst767/assets/83339335/87f8bab2-6697-43ad-b748-e4f581f3cdd2)

- **Data Acquisition via APIs**

  The pipeline initiates by interfacing with external APIs that provide real-time data on stock, crude oil, and natural gas prices.

- **Data Fetching with Google Cloud Functions**

  The pipeline automates the fetching of market data at a regular interval of every 30 minutes using Cloud Functions and Cloud Scheduler.

- **Data Storage in Google Cloud Storage**

  Post-fetching, the data is stored in JSON format in Google Cloud Storage.

- **Data Processing with Cloud Dataproc and Cloud Scheduler**

  Scheduled data processing tasks are orchestrated by Cloud Scheduler, which triggers Cloud Dataproc jobs every 30 minutes. Dataproc, transforms the raw JSON data into a structured format suitable for Bigquery.

- **Data Storage and Analysis in BigQuery**

  The structured data is then loaded into BigQuery. In BigQuery, the data is organized into tables, facilitating efficient data queries.

- **Data Visualization with Looker Studio**

  Looker Studio is used to create visual representations of the analyzed data. Looker Studio can directly pull data from BigQuery to provide real-time access to insights, enhancing decision-making processes.

### Ingest

The data ingestion process is handled via [Python scripts](https://github.com/animeshnandan/inst767/tree/main/cloudfunctions) using standard libraries to make API calls. These scripts are deployed on Google Cloud using Cloud Functions, every 30 minutes using Cloud Scheduler, with data being temporarily stored in Cloud Storage buckets in JSON format before transformation.

![cloud functions](https://github.com/animeshnandan/inst767/assets/83339335/3ae21dec-d1fb-4cb1-be36-0a04d30d5c63)

![cloud scheduler for cloud functions](https://github.com/animeshnandan/inst767/assets/83339335/c7c080cc-bbdb-407a-af48-6ee9d503b216)

![cloud storage buckets 1](https://github.com/animeshnandan/inst767/assets/83339335/a57ef3e2-daf7-4d61-b61a-7a8e8104bbb2)

![cloud storage buckets 2](https://github.com/animeshnandan/inst767/assets/83339335/da61c989-3070-4fb1-9fe4-4500058d2935)

![cloud stoarge buckets 3](https://github.com/animeshnandan/inst767/assets/83339335/e300eacb-1a59-43b5-8de5-6625d34fd30f)

### Transformation

Data transformation is conducted using [PySpark code](https://github.com/animeshnandan/inst767/tree/main/dataprocjobs) on Google Cloud's DataProc service, where we have employed cloud scheduler and dataproc workflows which trigger the creation of a compute engine which runs the jobs for all 4 stocks along with crude oil and natural gas. This stage aligns the data from their sources into a unified data model that supports our analytical objectives. Transformations are scheduled to run in accordance with the data ingest timings.

![cloud storage bucket storing pyspark files](https://github.com/animeshnandan/inst767/assets/83339335/bef4c8d8-91c6-47e3-a41e-54df46f3f3f6)

![cloud scheduler triggering dataproc workflow](https://github.com/animeshnandan/inst767/assets/83339335/ea19305f-c068-4b4d-af47-0c163990a962)

![dataproc compute engine](https://github.com/animeshnandan/inst767/assets/83339335/6487efa8-b83b-4d5c-8763-e67c75681aed)

![dataproc jobs](https://github.com/animeshnandan/inst767/assets/83339335/9f0ae15a-ab03-49e3-9058-c26c6fd38e94)

### Storage

The transformed data is stored in Google Cloud's BigQuery, which provides a robust platform for large-scale data analytics using SQL. We have created 2 separate datasets to store the data. ‘crudedataset’ contains tables storing the crude oil price and natural gas price. Whereas ‘stock_767’ stores the open, close, high, low & volume for the 4 stocks which we are dealing with. The schema has been defined for all the tables to ensure that the datatype is correct, so that queries run properly.

![bigquery bp stock schema](https://github.com/animeshnandan/inst767/assets/83339335/4759b642-207e-481a-a05a-d71da1da9d5d)

![bigquery chevron stock schema](https://github.com/animeshnandan/inst767/assets/83339335/0568b831-fdc0-42ae-b81a-245cc7109b05)

![bigquery crude price preview](https://github.com/animeshnandan/inst767/assets/83339335/afbe469f-90cb-4c84-93f1-ffbf90ac0cbd)

![bigquery exxon stock preview](https://github.com/animeshnandan/inst767/assets/83339335/2667767d-9fdd-4469-b79d-448691a8532f)

![bigquery natural gas preview](https://github.com/animeshnandan/inst767/assets/83339335/9d169fac-d827-4ab7-81f6-3e7ef362ce92)

![bigquery shell stock preview](https://github.com/animeshnandan/inst767/assets/83339335/06681947-716b-4eee-9047-9797266c38c2)

### Analysis

While in-depth analysis is not the core focus of this project, the data model allows for basic [queries](https://github.com/animeshnandan/inst767/tree/main/bigqueries) that can answer specific questions related to the impact of oil prices on stock values and more. Example SQL queries are provided below to demonstrate this capability:

a.	Is there a correlation between crude oil prices and the stock prices of these companies?

![bigquery correlation](https://github.com/animeshnandan/inst767/assets/83339335/d7912f04-0f29-49fc-baec-f406d048951b)

b.	Determine if there are consistent patterns of volume preceding or following price changes.

![consistent patterns of volume](https://github.com/animeshnandan/inst767/assets/83339335/302a7cd4-bceb-4366-8b42-7b9f3e64b42a)

c.	Assess the liquidity of a stock by looking at the average volume. Higher volumes generally mean better liquidity, making it easier to execute trades without affecting the price too much.

![assessing the liquidity](https://github.com/animeshnandan/inst767/assets/83339335/9e1b19a8-52f6-41fb-b05c-f749237fb82f)
