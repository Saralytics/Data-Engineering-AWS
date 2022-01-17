# Intro
This project aims to build a pipeline on AWS that serves 2 goals: 
1. Primarily for the users (running your business): process the transactions, give users access to their transactions history
2. Secondary for BI or data science, analyze, visualize the data to extract insights, making predictions.

**What you will see in this project:**
- [x] Connect to data sources 
- [x] Data ingestin in realtime 
- [x] Batch processing 
- [x] Storage 
- [x] Visualization 
- [x] API 

# Dataset

Ecommerce dataset from Kaggle [link](https://www.kaggle.com/carrie1/ecommerce-data)
**Quick look at the dataset:**
Columns
Rows 
Data types 
Unique categorical values 

# Platform Design
####  Overview 
![alt text](image.jpg)

#### Considerations:
We can either implement a relational design or non-relational design, so which one to choose?

- Comparing the relational vs NoSql database design 
![alt text](image.jpg)

- Why use a NoSQL database?
    Minimum modelling required;
    Advantage in speed;
    In our use case, the access patterns are predictable and defined, i.e. retrievel of customer invoices and invoice details. In comparison, if the access patterns are constantly varying (typical in analytical use cases), it's better to use relational DBs.    

# Tools needed

* AWS API Gateway 
* AWS Lambda Function 
* Kinesis, Kinesis Firehose
* Redshift 
* Cloudwatch
* Python, Boto3 (AWS PYTHON API)
* S3 
* Tableau  
* DynamoDB 
* AWS Glue
* Postman (testing API manually)

# Tips before you start
- Limit Lambda retries
- Limit DynamoDB read and write capacity
- Kinesis and DynamoDB costs even when you are not using it
- Add all services in the same region

# 1 Data Ingestion Pipeline

#### 1.1 Create the lambda function & Code for ingestion
choose the correct runtime

#### 1.2 Create the API gateway 
Special note on adding the mapping template under integration request. 

#### 1.3 Create the kinesis data stream 
#### 1.4 Attach the right policies 
#### 1.5 Test the pipeline

- From cloudwatch, go to the logs -> log groups, you can see log events 
- Go to Kinesis to check if the data has been written - this might take a few minutes  
- Another way, manually test from postman


# 2 Ingest to S3 raw storage
Now we have data in the buffer layer, kinesis data stream that we set up in the previous step, we need to put the data into s3 storage. How to do that: Kinesis triggers a lambda function -> function waits sometime to collect enough messages -> put all messages in the same queue into an s3 bucket. 

#### 2.1 Create s3 bucket 
#### 2.2 Create lambda for writing to s3
Add trigger: Kinesis -> data stream <the name of the stream you created>
Batch size: This is important
Code: 

#### 2.3 configure IAM 
read from kinesis data stream
write to s3 
basic execution role (this will be added automatically)

#### 2.4 Test in Lambda 
Create test event 

# 3 Ingest to DynamoDB 
Previous step, raw data is stored in S3 for backup. For transaction use cases, we will ingest data into DynamoDB.

Similar to the s3 pipeline, Kinesis triggers Lambda, Lambda function reformates the data and write to tables. 

#### 3.1 Define tables in Dynamo DB 
Table 1 - Customer purchase, storing invoice by customer ID and Invoice Number

|Customer ID| Invoice Num 1   | Invoice Num 2 | Invoice Num 3| ... | Invoice Num N |
|-----------|-----------------|---------------|--------------|-----|---------------|
|45njg4i8lkg| invoice 1(json) | invoice 2     | invoice 3    | ... | invoice n     |
|lk45abjgriu| invoice 1(json) | invoice 2     |              | ... |               |

Table 2 - Invoice details, storing items info 
|Invoice Num| Stock Code 1     | Stock Code 2  | Stock Code 3 | ... | Stock Code N  |
|-----------|------------------|---------------|--------------|-----|---------------|
|10000029476| Description(json)| invoice 2     | invoice 3    | ... | invoice n     |
|10000487563| ...              |  ...          | ...          | ... |               |

#### 3.2 Create tables 

#### 3.3 IAM
basic execution role
read from kinesis 
write to dynamoDB
[link to policy]()

#### 3.4 Lambda Function

# 4 Data Consumption - Visualization & Redshift 
Overview: 
Kinesis data stream -> Firehose managed delivery stream (gets data from data stream, put in s3 intermediate storage, copy to redhisft) -> redshift

#### 4.1 Configure redshift cluster 

Cluster types (node types)
Networking and security with VPC

#### 4.2 VPC Routing for firehose





# Consuming data using Redshift Datawarehouse 

# Thoughts 

