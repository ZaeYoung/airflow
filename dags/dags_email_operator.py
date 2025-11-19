from airflow import DAG
import pendulum
import datetime
from airflow.operators.email import EmailOperator

with DAG(
    dag_id="dags_email_operator",
    schedule="08 0 1 * *",
    start_date=pendulum.datetime(2021, 1, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:
    send_email_task = EmailOperator(
        task_id = 'send_email_task',
        to='sjyy1403@naver.com',
        subject='airflow 성공메일',
        html_content='airflow 작업이 완료되었습니다.'
    )