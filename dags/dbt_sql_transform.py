"""
dbt + Databricks using Astronomer Cosmos
"""

import os
import logging
from datetime import datetime
from datetime import timedelta
from pathlib import Path

from cosmos import (
    DbtDag,
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

profile_config = ProfileConfig(
    profile_name="default",
    target_name="dev",
    profiles_yml_filepath=(dbt_root_path / "databricks/profiles.yml")
)

dbt_sql_transform = DbtDag(
    project_config=ProjectConfig((dbt_root_path / "databricks").as_posix()),
    profile_config=profile_config,
    operator_args={
        "install_deps": True,
        "full_refresh": True,
    },

    schedule_interval=timedelta(minutes=30),
    start_date=datetime(2024, 2, 23),
    catchup=False,
    dag_id="dbt_sql_transform",
    default_args={"retries": 2},
)
