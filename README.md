# Designing-an-Automatic-Data-Collection-and-Storage-System-with-AWS-Lambda

# Overview
You want to create an AWS Lambda function that can fetch data from an API periodically, and store it in an Amazon RDS instance. The function needs to be triggered every 1 minute by an Amazon CloudWatch Event. To fetch the data from the API, the function should use the requests library or a similar library to make a GET request to the API.

# Project Goals
* Create an AWS Lambda function and configure it to be triggered by an Amazon CloudWatch Event that occurs every 15 seconds.
* In the function's code, use the urllib library to make a GET request to the API to fetch the data.
* Use a library such as psycopg2 to connect to the Amazon RDS instance and store the data in the database.
* Deploy the function to run indefinitely, continuing to fetch and store the data on a regular basis.

# Services used
* AWS Lambda: Lambda is a computing service that allows programmers to run code without creating or managing servers.
* AWS IAM: This is nothing but identity and access management which enables us to manage access to AWS services and resources securely.
* AWS RDS: It is a managed service provided by Amazon Web Services (AWS) that makes it easier to set up, operate, and scale a relational database in the cloud.
* AWS CloudWatch: CloudWatch is a monitoring service that enables you to collect and track metrics, as well as set alarms based on those metrics.
