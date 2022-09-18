
#NOT DONE!!!!!!!!!!


from aws_cdk import (
    aws_s3 as s3,
    aws_kinesisfirehose as firehose,
    aws_kinesisfirehose_destinations as destinations,
    aws_kinesis as kinesis,
    aws_lambda as lambda_,
    aws_stepfunctions as sfn,
    aws_stepfunctions_tasks as tasks,
    aws_iam as iam,
    aws_glue as glue,
    aws_s3_deployment as s3deploy,
    core,
)

# STREAM'S
#stream_name='-objects-stream'  # STREAM FOR OBJECT'S TABLE
#department_stream_name="-departments-stream" # STREAM FOR DEPARTMENT TABLE

#stack
stack_name = "damn-final-stack"

# GLUE:
database_name="damn-final-database"
# OBJECTS
objects_job_name="-glue-objects"

# twitter
twitter_job_name="-glue-twitter"

yfinance_workflow_name="-yfinance-workflow"
twitter_workflow_name="-twitter-workflow"



# TABLE NAMES

object_table_name="jsonobjects"
departments_table_name='jsondepartments'
final_objects_table_name="objects"
final_department_table_name="department"


class BucketOnly(core.Stack):
    def __init__(self, app: core.App, id: str) -> None:
        super().__init__(app, id)       

        #bucket
        bucket = s3.Bucket(self, "damn-final-raw-bucket", website_redirect=s3.WebsiteRedirect(
            host_name="aws.amazon.com"))
        bucketParquet = s3.Bucket(self, "damn-final-parquet-bucket", website_redirect=s3.WebsiteRedirect(
            host_name="aws.amazon.com"))

# GLUE
       # create database

        glue.Database(self, "MyDatabase", database_name=database_name)

        # create role

        glue_role = iam.Role(self, "glue_role", role_name ="damnfinal-glue-role",
            assumed_by=iam.ServicePrincipal("glue.amazonaws.com"),
            managed_policies=[iam.ManagedPolicy.from_aws_managed_policy_name('service-role/AWSGlueServiceRole')],
            description="Role for lambda function"  
        )

        bucket = s3.Bucket()
        bucket.grant_read_write(glue_role) 

        # upload script's for jobs

        s3deploy.BucketDeployment(self, "DeployWebsite",
            sources=[s3deploy.Source.asset("./GLUE")],
            destination_bucket=bucketParquet,
            destination_key_prefix="glue/"
        )

        # WORKFLOW for objects table

        cfn_objects_workflow = glue.CfnWorkflow(self, "MyCfnWorkflow",
            # default_run_properties=default_run_properties,
            name=objects_workflow_name
        )


        # JOB1-CONVERT TO PARQUET
        # job1:twitter - convert json to parquet
        glue_job1=glue.Job(self, "PythonShellJob",
            executable=glue.JobExecutable.python_etl(
                glue_version=glue.GlueVersion.V3_0,
                python_version=glue.PythonVersion.THREE,
                script=glue.Code.from_bucket(bucket, "glue/twitter_script.py") # PROVJERIT AKO JE DOBRO
            ),
            description="Job for conversion to parquet",
            job_name=objects_job_name,
            worker_type = glue.WorkerType.G_1_X,
            worker_count=10,
            role=glue_role,
            default_arguments={
                "--database_name": database_name,
                "--table_name": object_table_name,
                "--final_table": final_objects_table_name
            }
        )


        # WORKFLOW for departments table

        cfn_departments_workflow = glue.CfnWorkflow(self, "DamnCfnWorkflow2",
            # default_run_properties=default_run_properties,
            name=departments_workflow_name
        )

        # JOB 2
        #job2: yfinance - convert json to parquet
        glue_job2=glue.Job(self, "DamnPythonShellJob2",
            executable=glue.JobExecutable.python_etl(
                glue_version=glue.GlueVersion.V3_0,
                python_version=glue.PythonVersion.THREE,
                script=glue.Code.from_bucket(bucket, "glue/yfinance_script.py")
            ),
            description="Job for conversion to parquet",
            # job_name=departments_job_name,
            worker_type = glue.WorkerType.G_1_X,
            worker_count=10,
            role=glue_role,
            default_arguments={
                "--database_name": database_name,
                "--table_name": departments_table_name,
                "--final_table": final_department_table_name
            }   
        )

        # cfn_objects_trigger2 = glue.CfnTrigger(self, "DamnCfnTrigger11",
        #     actions=[glue.CfnTrigger.ActionProperty(job_name=glue_job2.job_name)],
        #     type="CONDITIONAL", # [CONDITIONAL, ON_DEMAND, SCHEDULED, EVENT] 
        #     name="first_trigger1",
        #     predicate=glue.CfnTrigger.PredicateProperty(
        #         conditions=[glue.CfnTrigger.ConditionProperty(
        #             crawler_name=departments_crawler1_name,
        #             crawl_state='SUCCEEDED',
        #             logical_operator='EQUALS',
        #             # state="SUCCEEDED"
        #         )]
        #     ),
        #     # start_on_creation=True,
        #     workflow_name=departments_workflow_name
        # )

        # # CRAWLER 4

        # cfn_departments_crawler2 = glue.CfnCrawler(self, "DamnCfnCrawler4",
        #     role=glue_role.role_arn,
        #     targets=glue.CfnCrawler.TargetsProperty(
        #         s3_targets=[glue.CfnCrawler.S3TargetProperty(path="s3://damn-final-parquet-bucket/"+ final_department_table_name + '/')] # CHANGE PREFIX ENVIRON?? prefix je ime tablice!
        #         ),
        #     name=departments_crawler2_name, 
        #     database_name=database_name
        # )

        # # TRIGGER 4

        # cfn_objects_trigger2 = glue.CfnTrigger(self, "DamnCfnTrigger5",
        #     actions=[glue.CfnTrigger.ActionProperty(crawler_name=departments_crawler2_name)],
        #     type="CONDITIONAL", # [CONDITIONAL, ON_DEMAND, SCHEDULED, EVENT] 
        #     name="second_trigger1",
        #     predicate=glue.CfnTrigger.PredicateProperty(
        #         conditions=[glue.CfnTrigger.ConditionProperty(
        #             job_name=glue_job2.job_name,
        #             crawl_state='SUCCEEDED',
        #             logical_operator='EQUALS',
        #             state="SUCCEEDED"
        #         )]
        #     ),
        #     # start_on_creation=True,
        #     workflow_name=departments_workflow_name
        # )

    

app = core.App()
BucketOnly(app, stack_name)
app.synth()

# cdk synth
# cdk deploy

