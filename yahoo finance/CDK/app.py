from aws_cdk import (core as cdk,
                     aws_s3 as s3,
                     aws_lambda as lambda_,
                     aws_dynamodb as dynamodb,
                     aws_iam as iam,
                     aws_events as events,
                     aws_events_targets as targets,
                     aws_sns as sns,
                     aws_sns_subscriptions as subscriptions
                     )

# Creates reference to already existing s3 bucket and lambda code

app = cdk.App()
stack_name = "damn-final-stack"
bucket_name = "damn-final-raw-bucket"
lambda_name = "damn-final-getyfinancedata"
table_name = "damn-final-dynamodb-table-yfinance"
topic_name = "damn-final-topic"


class LambdaAndBucket(cdk.Stack):
    def __init__(self, app: cdk.App, id: str) -> None:
        super().__init__(app, id)

        new_bucket = s3.Bucket(self, 
                    bucket_name, 
                    bucket_name=bucket_name, 
                    removal_policy=cdk.RemovalPolicy.DESTROY
                    )

        table = dynamodb.Table(self, 
                    table_name, 
                    table_name=table_name,
                    partition_key=dynamodb.Attribute(name="coin",
                                                    type=dynamodb.AttributeType.STRING
                                                    ),
                    removal_policy=cdk.RemovalPolicy.DESTROY
                    )

        handler = lambda_.Function(self, lambda_name,
                    runtime=lambda_.Runtime.PYTHON_3_9,
                    code=lambda_.Code.from_asset("getyfinancedata.zip"),
                    handler="getyfinancedata.lambda_handler",
                    timeout=cdk.Duration.seconds(900),
                    memory_size=512
                    )

        new_bucket.grant_read_write(handler)
        table.grant_read_write_data(handler)

        rule = events.Rule(self, 
                        "damn-final-yfinance-rule", 
                        schedule=events.Schedule.rate(cdk.Duration.days(1))
                        )
        rule.add_target(targets.LambdaFunction(handler))

        damntopic = sns.Topic(self, topic_name, topic_name=topic_name)
        damntopic.add_subscription(subscriptions.EmailSubscription("nikolina.kuhar000@gmail.com"))
        damntopic.grant_publish(handler)

LambdaAndBucket(app, stack_name)
app.synth()