# 🚀 ISS Tracker – AWS Lambda + RDS PostgreSQL (Serverless VPC Project)
A secure, serverless data pipeline that tracks the real-time location of the International Space Station (ISS) every minute using AWS Lambda and stores the data in a PostgreSQL database hosted on Amazon RDS. All components run inside a private network using AWS VPC with NAT Gateway and subnet routing.

---

## ✨ Features
- Fetches real-time ISS coordinates from a public API

- Stores latitude, longitude, timestamp, and message into PostgreSQL table

- Triggered automatically every 1 minute using Amazon EventBridge

- Lambda is deployed inside a private subnet (no public access)

- Internet access enabled via NAT Gateway (secure outbound only)

- End-to-end setup follows real-world VPC architecture and IAM security

---

## 🎯 Objective
To build a production-like, serverless architecture in AWS that:

- Collects real-time data from a public API

- Runs on automation without any manual trigger

- Stores data in a private PostgreSQL database (Amazon RDS)

- Uses secure networking practices with private subnets and NAT

---

🏗️ Architecture Overview

- Custom VPC with 3 subnets (2 public, 1 private)

- Internet Gateway (IGW) is attached to the VPC

- NAT Gateway is deployed in a public subnet

Route Tables are created:

- Public subnet → Internet Gateway

- Private subnet → NAT Gateway

- Amazon RDS (PostgreSQL) is launched inside the private subnet

- AWS Lambda is deployed in the private subnet (no public IP)

- Amazon EventBridge triggers the Lambda every 1 minute

- Lambda function fetches ISS data and stores it into PostgreSQL

🛠️ Tech Stack

| Tool/Service    | Purpose                                            |
|-----------------|----------------------------------------------------|
| AWS Lambda      | Executes Python code to fetch & store data         |
| Amazon RDS      | PostgreSQL database to store ISS coordinates       |
| Amazon VPC      | Custom network with public/private subnets         |
| NAT Gateway     | Allows secure internet access for private Lambda   |
| Internet Gateway| Enables internet access for public subnets         |
| EventBridge     | Scheduled trigger every 1 minute                   |
| urllib          | Fetches data from public ISS tracking API          |
| psycopg2        | Python PostgreSQL connector                        |

Tool/Service	Purpose
	
	
	
	
	
	
psycopg2	
	

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
python
Copy
Edit
iss-tracker-lambda/
│
├── lambda_function.py       # Main Lambda logic
├── rds_schema.sql           # Optional table schema
├── README.md                # Project documentation
├── screenshots/             # (Optional) Architecture diagrams and logs
🔁 Data Flow
📥 Extract
EventBridge triggers the Lambda function every 1 minute

Lambda uses urllib to call the public ISS API:
http://api.open-notify.org/iss-now.json

🔧 Transform
Extracts fields: latitude, longitude, timestamp, message

Ensures table exists in RDS before inserting

📤 Load
Inserts each new row into the iss_position table in RDS PostgreSQL

🔐 VPC & Network Design
Component	Configuration
VPC	Custom VPC in ap-south-1 (Mumbai)
Subnets	2 Public + 1 Private
Internet Gateway	Attached to VPC, used by public subnets
NAT Gateway	Deployed in public subnet for Lambda internet access
Route Tables	Private → NAT GW, Public → IGW
Lambda	Runs inside private subnet
RDS PostgreSQL	Hosted inside private subnet
Security Groups	Allow Lambda → RDS on port 5432

⚙️ Deployment Steps
Create a custom VPC with 3 subnets:

2 public subnets

1 private subnet

Attach an Internet Gateway to the VPC

Create a NAT Gateway in one of the public subnets

Create 2 route tables:

Public subnets → 0.0.0.0/0 via Internet Gateway

Private subnet → 0.0.0.0/0 via NAT Gateway

Launch Amazon RDS PostgreSQL in the private subnet

Deploy the Lambda function in the private subnet

Create an IAM Role with:

VPC access

RDS connectivity

CloudWatch logs

Create EventBridge rule to trigger Lambda every 1 minute

Monitor and validate data using pgAdmin, DBeaver, or SQL client

📊 Screenshots / Diagram
📁 Folder: screenshots/
(Include architecture diagram and example database output)

🧪 Learnings / Highlights
Built a fully secure VPC-based serverless app in AWS

Used Lambda in private subnet with NAT Gateway for safe outbound API calls

Practiced IAM role configuration, route tables, and NAT setup

Automated ETL workflow using EventBridge + Lambda

Gained real-world experience in RDS + Lambda + API Integration

📎 Related Files
lambda_function.py – Full Lambda source code

rds_schema.sql – Optional SQL table creation script

architecture.png – VPC architecture image (add in your repo)
