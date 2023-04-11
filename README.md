# Data Mesh

This is an attempt to provide Data as a Service(Data Mesh Concept) using Snowflake, DBT and Airflow implemented in Django Rest Framework.


## Initial Setup

1. Create a virtual environment
```
python -m venv .venv
```

2. Activate the virtual environment
```
. .venv/bin/activate
```

3. Install the Dependencies
```
python install django
python install djangorestframework 
```

4. Start the server
```
python manage.py runserver
```

## Postman Collection

[API collections](https://api.postman.com/collections/2394978-6a0c132d-c844-422a-aaa2-29abf2d1f1a0?access_key=PMAT-01GXS2F64NEQMD09MNY2285395)

It supports the most CRUDS operation for the following resources
- Transformations
- DAG Files
- Dags
- Airflow Pools
- Airflow Variables
- Airflow Connections
- Teams and Members

It also supports the following actions
- Trigger a DAG
- Backfill a DAG
