# astro-dbt-airflow-dbsql

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
  connections:
    - conn_id: aws_default
      conn_type: aws
      conn_schema:
      conn_login: data-lake
      conn_password: 12620ee6-2162-11ee-be56-0242ac120002
      conn_port:
      conn_extra:
        endpoint_url: http://172.175.236.199
    - conn_id: postgres_conn
      conn_type: postgres
      conn_host: postgres
      conn_schema: postgres
      conn_login: postgres
      conn_password: postgres
      conn_port: 5432
```

### 4) Init Airflow Project
Initialize project using the astro-cli
```shell
astro dev start
http://localhost:8080
```