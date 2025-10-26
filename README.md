# AWS-Lambda-Boto3-Automation-Assignments
This repository contains solutions for AWS automation assignments using AWS Lambda and Boto3.   Each assignment demonstrates automation of common AWS tasks such as EC2 management, S3 cleanup, bucket monitoring, and EBS snapshot handling.


---

##  Assignments Implemented

###Assignment 1: Automated EC2 Instance Management
- Objective: Start/Stop EC2 instances based on tags (`Auto-Start` / `Auto-Stop`).
- steps:
  1. Created two EC2 instances with tags.
  2. Created IAM role with `AmazonEC2FullAccess` + `AWSLambdaBasicExecutionRole`.
  3. Wrote Lambda function using Boto3.
  4. Tested via manual invocation.
- Result: Instances started/stopped automatically.
- Screenshot:  

  <img width="940" height="209" alt="image" src="https://github.com/user-attachments/assets/71f496b5-e3aa-43cf-83ba-668d389bd2fe" />

  <img width="940" height="381" alt="image" src="https://github.com/user-attachments/assets/5a643127-5e7e-40c8-a6a1-eabb80dbe341" />

  <img width="940" height="459" alt="image" src="https://github.com/user-attachments/assets/885e15c7-2edd-43d4-a851-79e89c1f267e" />

  <img width="940" height="453" alt="image" src="https://github.com/user-attachments/assets/3af99be4-98ae-4100-a0f3-f329fd786b99" />

  <img width="940" height="186" alt="image" src="https://github.com/user-attachments/assets/9a558b6f-9c51-4b62-9cc0-5b45975cab4a" />


## Assignment 2: Automated S3 Bucket Cleanup
- Objective: Delete files older than 30 days.
- Steps:
  1. Created S3 bucket and uploaded files.
  2. Created IAM role with `AmazonS3FullAccess` + `AWSLambdaBasicExecutionRole`.
  3. Wrote Lambda function to list and delete old files.
  4. Tested via manual invocation.
- Result: Old files deleted, recent files retained.
- Screenshot:  

 <img width="940" height="345" alt="image" src="https://github.com/user-attachments/assets/5a9de5c0-b1e5-47ca-b3b5-3c1aa27a6218" />

 <img width="940" height="375" alt="image" src="https://github.com/user-attachments/assets/c1d07478-2cd1-49f1-9b44-fac0aba4f074" />

 <img width="940" height="497" alt="image" src="https://github.com/user-attachments/assets/417816c6-a6ed-4d27-ad88-a0e616f3abdb" />

 <img width="940" height="417" alt="image" src="https://github.com/user-attachments/assets/0001605e-0167-4589-a7d3-4c69e6450f21" />

 
## Assignment 3: Monitor Unencrypted S3 Buckets
- Objective: Detect S3 buckets without server-side encryption.
- Steps:
  1. Created multiple buckets (some encrypted, some not).
  2. Created IAM role with `AmazonS3ReadOnlyAccess` + `AWSLambdaBasicExecutionRole`.
  3. Wrote Lambda function to check encryption.
  4. Tested via manual invocation.
- Result: Logs show unencrypted bucket names.
- Screenshot:

  <img width="940" height="403" alt="image" src="https://github.com/user-attachments/assets/2267cc78-1759-4f6b-92e3-e3c12aaab062" />

  <img width="940" height="501" alt="image" src="https://github.com/user-attachments/assets/996fabd4-8a4e-4947-a7e8-7aa9182b9bde" />

  <img width="940" height="370" alt="image" src="https://github.com/user-attachments/assets/ba41b6c1-7886-41a1-9234-3fa1af7a88f5" />


---

## Assignment 4: Automatic EBS Snapshot and Cleanup
- Objective: Create snapshots and delete those older than 30 days.
- Steps:
  1. Identified EBS volume ID.
  2. Created IAM role with `AmazonEC2FullAccess` + `AWSLambdaBasicExecutionRole`.
  3. Wrote Lambda function to create and clean snapshots.
  4. Tested via manual invocation.
- Result: New snapshot created, old ones deleted.
- Screenshot:

  <img width="940" height="183" alt="image" src="https://github.com/user-attachments/assets/fc1f4c99-1561-4815-8930-6970057502d3" />

  <img width="940" height="287" alt="image" src="https://github.com/user-attachments/assets/b1ad2064-415d-4d65-be83-f82a66e535f0" />

  <img width="940" height="480" alt="image" src="https://github.com/user-attachments/assets/4b7eaa43-cdd7-4928-a035-77134b19dfd9" />

  <img width="940" height="390" alt="image" src="https://github.com/user-attachments/assets/a2cee4e9-a534-44ea-83f4-d6f103b5484c" />

  <img width="940" height="200" alt="image" src="https://github.com/user-attachments/assets/f3d4e734-c0eb-4a25-b60f-99d0fbc59d1a" />


