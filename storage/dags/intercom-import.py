#  Sample DAG file
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
}

with DAG('my_dag', default_args=default_args, schedule_interval='@daily') as dag:
    task1 = BashOperator(
        task_id='task1',
        bash_command='echo "Hello World!"',
    )
    task2 = BashOperator(
        task_id='task2',
        bash_command='echo "Goodbye World!"',
    )
    task1 >> task2
