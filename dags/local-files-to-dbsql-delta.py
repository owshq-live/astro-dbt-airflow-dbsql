"""
Astro Python SDK & Databricks Integration
https://astro-sdk-python.readthedocs.io/en/stable/guides/databricks.html

This integration works with the rest api to submit a [job] to an existing cluster. It can allow the following locations:
- Local
- S3
- Google Cloud Storage

With the data ingested into Delta tables now you can query the raw data.
SELECT * FROM default.users;
SELECT * FROM default.payments;
SELECT * FROM default.rides;

Databricks Environment {owshq-dbr}
https://adb-2090585310411504.4.azuredatabricks.net/?o=2090585310411504

The process leverages the COPY INTO functionality to move data. If file is the same data does not get appended.
https://docs.databricks.com/en/sql/language-manual/delta-copy-into.html
"""

from datetime import datetime, timedelta

from airflow.decorators import dag
from airflow.utils.task_group import TaskGroup
from airflow.operators.empty import EmptyOperator

from astro import sql as aql
from astro.files import File
from astro.sql.table import Table, Metadata

default_args = {
    "owner": "luan moreno m. maciel",
    "retries": 1,
    "retry_delay": 0
}


@dag(
    dag_id="local-files-to-dbsql-delta",
    start_date=datetime(2024, 3, 14),
    max_active_runs=1,
    schedule_interval=timedelta(hours=24),
    default_args=default_args,
    catchup=False,
    tags=['development', 'elt', 'astrosdk', 'local', 'databricks']
)
def load_local_files_dbsql():

    schema = "default"

    init_data_load = EmptyOperator(task_id="init")
    finish_data_load = EmptyOperator(task_id="finish")

    with TaskGroup(group_id="Users") as users_task_group:

        load_local_users_dbsql = aql.load_file(
            task_id="load_local_users_dbsql",
            input_file=File("dags/data/users/users.csv"),
            output_table=Table(metadata=Metadata(schema=schema), name="users", conn_id="databricks_conn")
        )

    load_local_users_dbsql

    with TaskGroup(group_id="Payments") as payments_task_group:

        load_local_payments_dbsql = aql.load_file(
            task_id="load_local_payments_dbsql",
            input_file=File("dags/data/payments/payments.csv"),
            output_table=Table(metadata=Metadata(schema=schema), name="payments", conn_id="databricks_conn")
        )

    load_local_payments_dbsql

    with TaskGroup(group_id="Rides") as rides_task_group:

        load_local_rides_dbsql = aql.load_file(
            task_id="load_local_rides_dbsql",
            input_file=File("dags/data/rides/rides.csv"),
            output_table=Table(metadata=Metadata(schema=schema), name="rides", conn_id="databricks_conn")
        )

    load_local_rides_dbsql

    init_data_load >> [users_task_group, payments_task_group, rides_task_group] >> finish_data_load


dag = load_local_files_dbsql()
