# astro-dbt-airflow-dbsql

- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- [Astro CLI](https://docs.astronomer.io/astro/cli/install-cli)
- [Astro Python SDK](https://github.com/astronomer/astro-sdk)

### 1) Install Docker Desktop
Install docker desktop to run airflow locally
```shell
https://www.docker.com/products/docker-desktop/
```

### 2) Install Astro-CLI
Install astro-cli to develop DAGs
```shell
https://github.com/astronomer/astro-cli

curl -sSL install.astronomer.io | sudo bash -s
brew install astro

astro dev init
```

### 3) Add Airflow Connections
Add these configurations into the airflow_settings.yaml file
```yaml
airflow:
  connections: databricks_conn
```

### 4) Init Airflow Project
Initialize project using the astro-cli
```shell
astro dev start
http://localhost:8080
astro dev restart
```

### 5) Install Libraries for Development
Install the required libraries for the project to develop the DAGs locally
```shell
pip install apache-airflow
pip install astro-sdk-python
pip install bt-databricks
pip install astronomer-cosmos
```