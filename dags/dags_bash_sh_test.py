from airflow import DAG
import pendulum
import datetime
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="dags_bash_sh_test",
    schedule="10 0 * * 6#1",
    start_date=pendulum.datetime(2025, 11, 19, tz="Asia/Seoul"),
    catchup=False,
    #dagrun_timeout=datetime.timedelta(minutes=60),
    #tags=["example", "example2"],
    #params={"example_key": "example_value"},
) as dag:
    
    t1_a = BashOperator(
        task_id = "t1_a",
        bash_command="/opt/airflow/plugins/shell/sh_test.sh A",
    )

    t2_a = BashOperator(
        task_id = "t2_a",
        bash_command="/opt/airflow/plugins/shell/sh_test.sh C",
    )

    t1_a >> t2_a