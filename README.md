# Project Overview

This project is designed to analyze insights from datasets containing gas prices, crude oil prices, and the stock values of major oil and gas companies. The companies in focus are Chevron Corporation (CVX), Royal Dutch Shell (SHEL), ExxonMobil Corporation (XOM), and BP plc (BP). The project is delineated into four distinct stages: data ingestion, transformation, storage, and analysis. Each of these stages plays a significant role in transforming raw data into insightful, actionable intelligence that helps predict market trends and formulate strategic advice.

## Data Sources

The data for this project is retrieved from three main sources using the [Alphavantage API](https://www.alphavantage.co/):
1.	Gas Prices: Daily gas price data.
2.	Crude Oil Prices: Daily crude oil price data.
3.	Stock Values: Daily stock prices of CVX, SHEL, XOM, and BP.

## Data Pipeline Overview

![Untitled Jam 1](https://github.com/animeshnandan/inst767/assets/83339335/87f8bab2-6697-43ad-b748-e4f581f3cdd2)
|:--:|
| Data Pipeline |

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

The data ingestion process is handled via [Python scripts](https://github.com/animeshnandan/inst767/tree/main/cloudfunctions) using standard libraries to make API calls. These scripts are deployed on Google Cloud using Cloud Functions, every 30 minutes using Cloud Scheduler.

![cloud functions](https://github.com/animeshnandan/inst767/assets/83339335/3ae21dec-d1fb-4cb1-be36-0a04d30d5c63)
|:--:|
| List of Google Cloud Functions. |

![cloud scheduler for cloud functions](https://github.com/animeshnandan/inst767/assets/83339335/c7c080cc-bbdb-407a-af48-6ee9d503b216)
|:--:|
| Cloud Scheduler interface with scheduled jobs for triggering Cloud Functions. |

![cloud function running](https://github.com/animeshnandan/inst767/assets/83339335/37ca2d4c-84f5-491a-9efb-8a6ab8fbfc77)
|:--:|
| Running example of cloud function for 'shel'. |

Once the cloud functions successfully execute, the data being stored in Cloud Storage buckets in JSON format before transformation.

![cloud storage buckets 1](https://github.com/animeshnandan/inst767/assets/83339335/a57ef3e2-daf7-4d61-b61a-7a8e8104bbb2)
|:--:|
| An overview of various Cloud Storage buckets |

![cloud storage buckets 2](https://github.com/animeshnandan/inst767/assets/83339335/da61c989-3070-4fb1-9fe4-4500058d2935)
|:--:|
| Google Cloud Storage bucket, 'stock767_xom', listing JSON files within it. |

### Transformation

Data transformation is conducted using [PySpark code](https://github.com/animeshnandan/inst767/tree/main/dataprocjobs) on DataProc, where we have employed cloud scheduler and dataproc workflows which trigger the creation of a compute engine which runs the jobs for all 4 stocks along with crude oil and natural gas. This stage aligns the data from their source JSON files into a data model in Bigquery that supports our analytical objectives to answer a couple of business questions. Transformations are scheduled to run in accordance with the data ingest timings every 30 minutes.

![cloud storage bucket storing pyspark files](https://github.com/animeshnandan/inst767/assets/83339335/bef4c8d8-91c6-47e3-a41e-54df46f3f3f6)
|:--:|
| Google Cloud Storage bucket, showing the 'code_files' folder within the dataproc bucket. It contains several pyspark scripts which will run as jobs. |

![cloud scheduler triggering dataproc workflow](https://github.com/animeshnandan/inst767/assets/83339335/ea19305f-c068-4b4d-af47-0c163990a962)
|:--:|
| The Cloud Scheduler which triggers the Dataproc Workflow. |

![dataproc compute engine](https://github.com/animeshnandan/inst767/assets/83339335/6487efa8-b83b-4d5c-8763-e67c75681aed)
|:--:|
| DataProc cluster. |

![dataproc jobs](https://github.com/animeshnandan/inst767/assets/83339335/9f0ae15a-ab03-49e3-9058-c26c6fd38e94)
|:--:|
| DataProc Jobs interface, showing a list of completed PySpark jobs by cluster. |

### Storage

The transformed data is stored in Google Cloud's BigQuery, which is a robust platform for large-scale data analytics using SQL. We have created 2 separate datasets to store the data. ‘crudedataset’ contains tables storing the crude oil price and natural gas price. Whereas ‘stock_767’ stores the open, close, high, low & volume for the 4 stocks which we are dealing with. The schema has been defined for all the tables to ensure that the datatype is correct, so that queries run properly.

![bigquery crude price preview](https://github.com/animeshnandan/inst767/assets/83339335/afbe469f-90cb-4c84-93f1-ffbf90ac0cbd)
|:--:|
| The 'crudeprice' dataset in BigQuery, showcasing rows of data with date and value fields. |

![bigquery exxon stock preview](https://github.com/animeshnandan/inst767/assets/83339335/2667767d-9fdd-4469-b79d-448691a8532f)
|:--:|
| The preview of the 'exxonstock' dataset in BigQuery with all the fields. |

### Analysis

While carrying out a comprehensive analysis is beyond the scope of this project, the data model supports basic [queries](https://github.com/animeshnandan/inst767/tree/main/bigqueries) to address specific questions, such as the impact of oil prices on stock values, among others. Below, example SQL queries are provided to illustrate this functionality:

a.	Is there a correlation between crude oil prices and natural gas, as well as the stock prices of the four major companies: CVX, SHEL, XOM, and BP?

![bigquery correlation](https://github.com/animeshnandan/inst767/assets/83339335/d7912f04-0f29-49fc-baec-f406d048951b)
|:--:|
| A query and its results in BigQuery, analyzing the correlation between crude oil prices and Exxon stock prices. The results indicate significant correlations (p < 0.05), as reflected by correlation coefficients. |

b.	Are there consistent patterns in trading volume preceding or following price changes?

![consistent patterns of volume](https://github.com/animeshnandan/inst767/assets/83339335/302a7cd4-bceb-4366-8b42-7b9f3e64b42a)
|:--:|
| A query analyzing if there are consistent patterns of trading volume before significant price changes in Exxon stock. The query results show the dates, volumes, and corresponding price changes, providing insights into the trading behavior preceding price adjustments. |

c.How does the average volume of a stock influence its liquidity, and how can analyzing average trading volume over various months demonstrate the stock's liquidity and impact trade execution?

![assessing the liquidity](https://github.com/animeshnandan/inst767/assets/83339335/9e1b19a8-52f6-41fb-b05c-f749237fb82f)
|:--:|
| A query to assess stock liquidity by analyzing the average trading volume for 'bpstock' over various months. The results demonstrate the average volume traded, which helps assess the liquidity of these stocks. |

**[Looker Studio Visualization](https://lookerstudio.google.com/reporting/80dbad03-eff7-45f0-8eff-f19dea39fabd)**
|:--:|

### Management

The project is managed through GitHub, with regular commits that reflect continuous integration and development. Each team member's contributions are clearly documented through meaningful small commits. Code is orgainized into respective folders for each stage ([Ingest](https://github.com/animeshnandan/inst767/tree/main/cloudfunctions), [Transformation](https://github.com/animeshnandan/inst767/tree/main/dataprocjobs), Storage, [Analysis](https://github.com/animeshnandan/inst767/tree/main/bigqueries))
