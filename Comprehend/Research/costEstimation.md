Lambda (Yahoo):
    - number of requests per hour: 1 500
    - duration of each request (in ms): 3 000
    - amount of memory allocated: 128 MB
    - amount of storage allocated: 512 MB
        Lambda costs - With Free Tier (Monthly): 0.02 USD

Lambda (Twitter):
    - number of requests per month: 100 000
    - duration of each request (in ms): 3 000
    - amount of memory allocated: 128 MB
    - amount of storage allocated: 512 MB
        Lambda costs: 0.00 USD
         
Glue (Yahoo):
    - number of DPUs for Apache Spark job: 20
    - duration for which Apache Spark ETL job runs: 60 min
    - number of DPUs for Python Shell job: 0.07
    - duration for which Python Shell job ETL runs: 10 min
    - number of DPUs for each provisioned development endpoint: 5
    - Duration for provisioned development endpoint: 1 hour
        ETL jobs and development endpoint cost (Monthly): 11.01 USD

Glue (Twitter):
    - number of DPUs for Apache Spark job: 20
    - duration for which Apache Spark ETL job runs: 60 min
    - number of DPUs for Python Shell job: 0.07
    - duration for which Python Shell job ETL runs: 10 min
    - number of DPUs for each provisioned development endpoint: 5
    - Duration for provisioned development endpoint: 1 hour
        ETL jobs and development endpoint cost (Monthly): 11.01 USD

Athena: 
    - total number of queries per day: 30
    - data amount scanned per query: 128 MB
        Total Monthly cost: 0.56 USD

DynamoDB (on-demand capacity):
    - data storage size: 5 GB
    - average item size: 10 KB
    - on-demand write: number of write per day: 100
    - on-demand read: number of reads per day: 100
        Total Monthly cost: 1.58 USD

S3 (raw):
    - S3 Standard storage: 1 GB per month
    - S3 Standard Average Object Size: 20 KB 
    - data returned by S3 Select: 1 GB per month
    - data scanned by S3 Select: 1 GB per month
        Total Upfront cost: 0.28 USD
        Total Monthly cost: 0.03 USD

S3 (parquet):
    - S3 Standard storage: 1 GB per month
    - data returned by S3 Select: 1 GB per month
    - data scanned by S3 Select: 1 GB per month 
        Total Monthly cost: 0.03 USD


