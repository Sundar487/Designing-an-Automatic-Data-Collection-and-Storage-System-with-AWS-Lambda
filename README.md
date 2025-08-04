🚀 ISS Tracker using AWS Lambda + RDS PostgreSQL (Secure Serverless Architecture)
This project creates a secure, serverless data pipeline to track the real-time location of the International Space Station (ISS) every minute. It uses:

AWS Lambda to fetch and store the data

Amazon EventBridge to schedule the trigger

Amazon RDS (PostgreSQL) to store the results

A secured VPC network with private subnets and a NAT Gateway to control internet access

🎯 Objective
Automatically collect data from a public API every minute

Store the data in a secure PostgreSQL database

Build a production-like architecture using AWS VPC, NAT Gateway, and private subnets

Follow best practices for secure serverless design

🧭 Architecture Flow
A custom VPC is created with 3 subnets: 2 public and 1 private

An Internet Gateway is attached to the VPC for public subnet access

A NAT Gateway is created in one of the public subnets

The private subnet is associated with a route table that forwards internet traffic to the NAT Gateway

Amazon RDS (PostgreSQL) is launched in the private subnet

The Lambda function is deployed in the private subnet so it's not exposed to the public internet

The Lambda function accesses the internet (to call the API) via the NAT Gateway

EventBridge triggers the Lambda function every 1 minute

Lambda fetches the ISS location and stores it in the PostgreSQL table

IAM Role attached to Lambda allows access to RDS and VPC resources

🔁 Data Flow
pgsql
Copy
Edit
+--------------------+     every 1 minute      +----------------------+
|   Amazon EventBridge  |  ------------------>  |     AWS Lambda        |
+--------------------+                        | (in private subnet)   |
                                              +----------+-----------+
                                                         |
                                                         v
                                                +-------------------+
                                                |  Public Subnet    |  ← NAT Gateway
                                                +-------------------+
                                                         |
                                                         v
                                                +-------------------+
                                                | Private Subnet    |
                                                |  RDS PostgreSQL   |
                                                +-------------------+
📦 Lambda Function (Python)
Uses urllib to fetch data from http://api.open-notify.org/iss-now.json

Extracts latitude, longitude, timestamp, and message

Creates the table if it doesn’t exist

Inserts the data into the iss_position table

🛠️ Tech Stack
Tool	Purpose
AWS Lambda	Executes code every minute (Python)
Amazon RDS	Stores ISS data securely (PostgreSQL)
Amazon VPC	Provides private networking and isolation
NAT Gateway	Allows Lambda (in private subnet) to access the internet
Internet Gateway	Enables internet access for public subnets
EventBridge	Triggers Lambda function on a schedule
psycopg2	Python connector for PostgreSQL
urllib	To fetch API data from the public endpoint

🧱 Database Table Schema
sql
Copy
Edit
CREATE TABLE IF NOT EXISTS iss_position (
  id SERIAL PRIMARY KEY,
  latitude INTEGER,
  longitude INTEGER,
  timestamp INTEGER,
  message VARCHAR(255)
);
📁 Project Structure
python
Copy
Edit
iss-tracker-lambda/
│
├── lambda_function.py       # Main Lambda logic
├── rds_schema.sql           # Optional table schema
├── README.md                # Project documentation
├── screenshots/             # (Optional) Architecture and DB screenshots
⚙️ Deployment Steps
Create a custom VPC with:

2 public subnets

1 private subnet

Attach an Internet Gateway to the VPC

Create a NAT Gateway in one of the public subnets

Set up route tables:

Public route table → 0.0.0.0/0 via Internet Gateway

Private route table → 0.0.0.0/0 via NAT Gateway

Launch Amazon RDS PostgreSQL in the private subnet

Create a Lambda function in the private subnet

Attach IAM role with permissions:

RDS access

VPC and network interfaces

CloudWatch logs

Create an Amazon EventBridge rule to trigger Lambda every 1 minute

Monitor data using pgAdmin, DBeaver, or other PostgreSQL tools

🧪 Learnings & Highlights
Built a secure serverless pipeline in AWS

Used Lambda in a private subnet with NAT Gateway for outbound access

Applied real-world networking configurations using VPC

Practiced IAM role assignment and CloudWatch monitoring

Demonstrated scheduled ETL workflow without using external schedulers
