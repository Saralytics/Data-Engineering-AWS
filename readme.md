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
    No modelling required;
    Fast retrival;
    In our use case, only retrival is needed, we don't need to be full ACID compliant;


# Tools needed

* Postman (testing API manually)
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

# Tips before you start


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
    
Key consideration: 
1. Super important to decide on data access patterns prior to creating tables, because NoSQL databases don't accomodate reshaping data when being queried like RDBMS. [Access pattern matrix](https://docs.aws.amazon.com/prescriptive-guidance/latest/dynamodb-data-modeling/template-access-patterns.html)
2. Choosing the right partition key is important for velocity and scalability. [Best practices](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-time-series.html)

#### 3.1 Define tables in Dynamo DB 
|           | Invoice Num 1   | Invoice Num 2 | Invoice Num 3| ... | Invoice Num N |
|-----------|-----------------|---------------|--------------|-----|---------------|
|Customer ID| invoice 1(json) | invoice 2     | invoice 3    | ... | invoice n     |





# Consuming data using Redshift Datawarehouse 

# Thoughts, improvements, other ideas 
It's pretty easy to get lost, so get familiar with AWS
