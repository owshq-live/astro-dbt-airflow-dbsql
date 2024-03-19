"""
dbt + Databricks using Astronomer Cosmos
"""

import os
import logging
from datetime import datetime
from pathlib import Path

from airflow.decorators import dag

from cosmos.profiles import DatabricksTokenProfileMapping
from cosmos import (
    DbtTaskGroup,
    ProfileConfig,
    ProjectConfig
)

logger = logging.getLogger(__name__)
doc_md = """
"""

default_args = {
    "owner": "owshq",
    "retries": 1,
    "retry_delay": 0
}

default_dbt_root_path = Path(__file__).parent / "dbt"
dbt_root_path = Path(os.getenv("DBT_ROOT_PATH", default_dbt_root_path))


@dag(
    dag_id="databricks-dbt-sql-transform",
    default_args=default_args,
    max_active_runs=1,
    schedule_interval="@daily",
    start_date=datetime(2024, 3, 19),
    catchup=False,
    tags=['development', 'dbt', 'databricks', 'cosmos']
)
def dag_sql_transform():
    """
    """

    profile_config = ProfileConfig(
        profile_name="default",
        target_name="dev",
        profile_mapping=DatabricksTokenProfileMapping(
            conn_id="databricks_conn",
            profile_args={
                "schema": "default"
            }
        )
    )

    dbt_databricks = DbtTaskGroup(
        project_config=ProjectConfig(default_dbt_root_path / "databricks"),
        profile_config=profile_config,
        operator_args={
            "install_deps": True
        }
    )

    dbt_databricks


dag_sql_transform()