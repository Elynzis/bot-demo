"""
This is an example DAG
"""
from datetime import datetime, timedelta
from airflow import DAG
from airflow.models import Variable
from airflow.operators.dummy_operator import DummyOperator
from utils.dag_notification import send_dag_failed_notification

DAG_NAME = "example_workflow_v1"

default_args = {
    "owner": "BOT_DE",
    "depends_on_past": False,
    "email": ["airflow@example.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
    "on_failure_callback": send_dag_failed_notification,
}

default_config = {
    "database": "A",
    "raw_data_location": "/raw",
    "clean_target_location": "/clean",
    "jar_name": "my_spark_app.jar"
}

config = Variable.get("example_variable",
                      deserialize_json=True,
                      default_var={})

config = {**default_config, **config}

with DAG(DAG_NAME,
         default_args=default_args,
         start_date=datetime(2020, 9, 26),
         schedule_interval="0 15 * * *"
         ) as dag:
    start_task = DummyOperator(
        task_id="start_task"
    )

    # your CustomIngestionOperator
    ingest_data_task = DummyOperator(
        task_id="ingest_data_task",
        database=config["database"],
        location=config["raw_data_location"]
    )

    # your SparkCleanTransformOperator
    clean_data_task = DummyOperator(
        task_id="clean_data_task",
        jar=config["jar_name"],
        target_location=config["clean_target_location"]
    )

    # your SlackOperator
    notify_slack_de_team = DummyOperator(
        task_id="notify_slack_de_team",
        slack_conn_id="de_slack_conn",
        message="example_workflow: Success, N rows was ingested"
    )

    # your SlackOperator
    notify_slack_ds_team = DummyOperator(
        task_id="notify_slack_ds_team",
        slack_conn_id="ds_slack_conn",
        message="example_workflow: Success, data is available at X"
    )

    end_task = DummyOperator(
        task_id="end_task"
    )

    # build task association here
    start_task >> ingest_data_task >> clean_data_task
    clean_data_task >> [notify_slack_de_team, notify_slack_ds_team] >> end_task
