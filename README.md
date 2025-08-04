# 🚀 ISS Tracker using AWS Lambda + RDS PostgreSQL
A secure, serverless pipeline that tracks the real-time position of the International Space Station (ISS) every minute using AWS Lambda and stores the data into Amazon RDS (PostgreSQL). The solution runs fully within a custom VPC using private subnets, NAT Gateway, and EventBridge for scheduling.

##  ✨ Features
Fetches real-time ISS location from a public API

Stores latitude, longitude, timestamp, and message in RDS PostgreSQL

Triggered automatically every 1 minute using Amazon EventBridge

All components run inside a secured, private VPC network

Lambda uses a NAT Gateway for secure internet access (no public IP)

Designed using real-world cloud and network architecture practices

🎯 Objective
To create a production-style AWS serverless architecture that:

Automatically pulls real-time ISS data every minute

Stores the data securely in a private PostgreSQL database

Uses VPC networking best practices (private subnets, NAT Gateway, etc.)

Demonstrates secure serverless data engineering patterns on AWS

🏗️ Architecture Overview
<!-- Replace with your actual GitHub image path -->

A custom VPC is created with 3 subnets (2 public + 1 private)

An Internet Gateway is attached to allow public subnet internet access

A NAT Gateway is deployed in a public subnet for outbound access from private subnets

Private subnet is associated with a route table pointing to the NAT Gateway

Amazon RDS (PostgreSQL) is launched in the private subnet for data storage

AWS Lambda is deployed in the private subnet (with no public IP)

Amazon EventBridge triggers the Lambda function every 1 minute

Lambda fetches ISS data and stores it into the RDS database

IAM Role is attached to Lambda with permissions for VPC, RDS, and logging

🛠️ Tech Stack
Tool/Service	Purpose
AWS Lambda	Executes Python code to fetch and store data
Amazon RDS	PostgreSQL database to store ISS location
Amazon VPC	Custom networking and subnet isolation
NAT Gateway	Enables outbound internet from private subnet
Internet Gateway	Enables internet access for public subnets
EventBridge	Scheduled trigger every 1 minute
psycopg2	PostgreSQL connector for Python
urllib	Fetches data from ISS public API

🧱 Database Schema
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
📂 Project Structure
graphql
Copy
Edit
iss-tracker-lambda/
│
├── lambda_function.py       # Main Lambda code
├── rds_schema.sql           # Optional SQL schema file
├── README.md                # This documentation
├── screenshots/             # Architecture diagram & logs
🔁 Execution Workflow
📥 Extract (Lambda + EventBridge)
EventBridge triggers Lambda every 1 minute

Lambda uses urllib to call: http://api.open-notify.org/iss-now.json

🔧 Transform (Lambda)
Extracts latitude, longitude, timestamp, and message

Ensures table exists before inserting

📤 Load (Lambda + RDS)
Inserts data into iss_position table in RDS PostgreSQL

All activity runs within a private subnet

🔐 VPC and Network Configuration
Component	Configuration Description
VPC	Custom VPC in ap-south-1 (Mumbai)
Subnets	2 Public + 1 Private
Internet Gateway	Attached to VPC to support public subnet traffic
NAT Gateway	Placed in public subnet for secure outbound access
Route Tables	Public route → IGW, Private route → NAT Gateway
RDS	Launched in private subnet
Lambda	Runs in private subnet (no public IP)
Security Groups	Allows Lambda to access RDS on port 5432

⚙️ Deployment Steps
Create a custom VPC with:

2 Public subnets

1 Private subnet

Attach an Internet Gateway to the VPC

Launch a NAT Gateway in one of the public subnets

Configure Route Tables:

Public subnets → 0.0.0.0/0 → Internet Gateway

Private subnet → 0.0.0.0/0 → NAT Gateway

Launch Amazon RDS PostgreSQL in the private subnet

Create an IAM Role for Lambda:

VPC access

RDS connectivity

CloudWatch logging

Deploy Lambda function in private subnet

Create EventBridge rule to trigger Lambda every 1 minute

Verify records in RDS using DBeaver, pgAdmin, or SQL client

🧪 Learnings / Highlights
Implemented real-world VPC architecture with subnet isolation

Learned how to use NAT Gateway for private Lambda internet access

Automated data collection using EventBridge + Lambda

Secured database setup using RDS in private subnets

Applied best practices in IAM roles, routing, and security groups

Demonstrated serverless ETL with zero EC2 or manual infra

📎 Related Files
lambda_function.py – Full Lambda code

rds_schema.sql – Optional SQL schema

architecture.png – VPC architecture diagram (add this image to your repo)
