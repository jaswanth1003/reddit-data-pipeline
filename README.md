# reddit-data-pipeline
ETL pipeline using Airflow to extract Reddit data, store in S3, transform with AWS Glue, and load into Redshift. Built with Docker for containerization. Simulates a production-ready cloud data pipeline for analytics and reporting.

## *Table of Contents*

1. [Project Overview](#project-overview)  
2. [System Architecture](#system-architecture)  
3. [Tools & Technologies Used](#tools--technologies-used)  
4. [Prerequisites](#prerequisites)  
5. [Setup & Configuration](#setup--configuration)  
6. [Pipeline Execution Flow](#pipeline-execution-flow)  
7. [Conclusion](#conclusion)

## *Project Overview*
This project implements a modular and scalable ETL pipeline that extracts data from Reddit using its official API, stores raw data in Amazon S3, transforms the data using AWS Glue, and loads it into Amazon Redshift for analytical querying. The orchestration is managed using Apache Airflow, containerized via Docker Compose, making it reproducible and cloud-ready.

## *Key Functionalities*:

.Extracts top posts from specified subreddits using Reddit API
.Schedules and orchestrates tasks via Apache Airflow
.Stores raw data in Amazon S3 (data lake)
.Catalogs and transforms data using AWS Glue
.Loads cleaned data into Amazon Redshift

## *System Architecture*

![Reddit_arch](https://github.com/user-attachments/assets/2d9a6782-4516-4bcb-a7b2-b5b298e17902)

## *Tools & Technologies Used*

| Tool                  | Purpose                                    |
| --------------------- | ------------------------------------------ |
| **Python 3.9+**       | Main programming language                  |
| **Apache Airflow**    | DAG orchestration and task scheduling      |
| **Docker Compose**    | Containerization and local orchestration   |
| **PostgreSQL**        | Airflow metadata database                  |
| **Amazon S3**         | Cloud object storage for raw & clean data  |
| **AWS Glue**          | Metadata cataloging and PySpark transforms |
| **Amazon Athena**     | SQL query engine on S3 data                |
| **Amazon Redshift**   | Cloud-based data warehouse                 |
| **PRAW (Reddit API)** | Data extraction from Reddit                |

## *Prerequisites*

Before setting up the pipeline, ensure you have:

.An AWS account with access to:
  S3, Glue, Athena, Redshift
. Reddit API credentials (client ID, secret)
. Docker and Docker Compose installed
. Python 3.9+ (for local testing/development)

## *Setup & Configuration*

1. Clone the Repository

. git clone https://github.com/your-username/reddit-data-pipeline.git
cd reddit-data-pipeline

2. Configure Environment

Edit the config file to include your:

. Reddit credentials
. AWS keys
. S3 bucket
. Redshift cluster details

3. Start the Environment

. docker-compose up --build

4. Access Airflow UI

. URL: http://localhost:8080

## * Pipeline Execution Flow*
 1. Extraction
. Airflow DAG triggers reddit_pipeline

. Pulls top posts from a subreddit via Reddit API

. Saves .csv file to /opt/airflow/data/output

. Uploads to S3://<bucket>/raw/

 2. Transformation
. AWS Glue crawler catalogs raw data

. Athena transforms JSON/CSV using SQL or Glue scripts

. Cleaned data is written back to S3://<bucket>/processed/

 3. Loading
. Airflow triggers Redshift loader
. Loads transformed data into Redshift using COPY command or AWS Glue jobs

4.  Monitoring
. Airflow DAGs display logs, retries, and status

## *Conclusion* 
This project simulates an end-to-end production-grade ETL pipeline, leveraging industry-standard tools for:

. Automation (Airflow)
. Scalability (Glue, S3, Redshift)
. Modularity (Docker-based microservice architecture)




