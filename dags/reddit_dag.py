from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


import os
import sys



# To ensure every commands that is running is from the root directory
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pipelines.reddit_pipeline import reddit_pipeline
from pipelines.aws_s3_pipeline import upload_s3_pipeline


default_args = {
    'owner': 'Jaswanth Gurujala',
    'start_date': datetime(2025, 5, 22)
}

file_postfix = datetime.now().strftime("%Y%m%d")

dag = DAG (
    dag_id='etl_reddit_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
    tags=['reddit', 'etl', 'pipeline']
)

# Extraction from reddit
extract = PythonOperator(
    task_id='reddit_extraction',
    python_callable=reddit_pipeline,
    op_kwargs={
        'file_name': f'reddit_{file_postfix}',
        'subreddit': 'dataengineering',
        'time_filter': 'day',
        'limit': 100
    },
    dag=dag
)

# Upload to S3
upload_s3 = PythonOperator(
    task_id = 's3_upload',
    python_callable=upload_s3_pipeline,
    dag=dag
)

extract >> upload_s3