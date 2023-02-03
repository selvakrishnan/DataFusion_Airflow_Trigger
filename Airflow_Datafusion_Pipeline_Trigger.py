
import airflow
from airflow.providers.google.cloud.operators.datafusion import CloudDataFusionStartPipelineOperator
from datetime import datetime

class Constants(object):
    OWNER = "Static Dag"
    RETRIES = 0
    START_DATE = datetime(2020, 1, 1)

# DAG configuration variables
default_args = {"owner": Constants.OWNER,
                "depends_on_past": False,
                "retries": Constants.RETRIES,
                "catchup": False,
                "start_date": Constants.START_DATE
                }

with airflow.DAG(
        'Static_Dag',
        'catchup=False',
        default_args=default_args,
        schedule_interval=None) as dag:
        #schedule_interval for weekly or daily triggere provide based on your buiness requirment.
        #minutes_hour_day_month_week
        #10****

    start_pipeline = CloudDataFusionStartPipelineOperator(
        location='....', #provide the location of your instance.
        pipeline_name='....',#provide the pipeline name.
        instance_name='...', #provide the instance name.
        task_id="start_pipeline", #This is the workflow name inside the dag.
        namespace='....', #provide the namespace name.
        runtime_args={}, #provide your arguments from here instead of providing it in datafusion UI.

    )

    start_pipeline
