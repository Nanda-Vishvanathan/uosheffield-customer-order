# UoS - Take Home Assignment

**Task Description:**
2. Build a simple API on top of this data. This API should provide 2 REST endpoints that return JSON for Customers and their Orders. The REST endpoints should be as follows:<br>
  A. One that returns Customer and Order data for all Customers. This endpoint should also allow you to query for all active or archived Customers.<br>
  B. Another that returns the same data for a single Customer using a Customer id.<br>

**Tech Stack:**

1. Programming: Python 3.x<br>
2. AWS Serverless - Lambda Function<br>
3. AWS RDS- MySQL<br>
4. AWS S3, SSM, Cloud Watch.<br>
5. AWS API Gateway


**Design Approach:**

![image](https://github.com/Nanda-Vishvanathan/uosheffield-customer-order/assets/59757238/c627af23-4958-4fa3-a3b5-2266cf5eef6c)



**Code Walkthrough:**

As part of task 2, this project contains the code for an AWS Lambda function that is invoked by API Gateway that fetches data for customers and order from database. <br>
Following are the AWS API Gateway (REST API):<br>
***<<aws:>>/customers*** - Return data of all the customers. <br>
***<<aws:>>/customer?id=<<int>>*** - return data of customer based on id.<br>


**Code Use**

Clone the code:<br>
***git clone https://github.com/Nanda-Vishvanathan/uosheffield-customer-order.git<br>***

Create a new branch<br>
***git checkout -b <branch_name><br>***

Make the changes & push to the repo.<br>
***git add .<br>***
***git commit -m "Description of changes"<br>***
***git push origin <branch_name><br>***

To deploy please, follow the steps below:

please install the requirements.txt from the folder<br>
***pip install -r requirements.txt -t .<br>***

Zip the code using the following command:<br>
***zip -r customers_and_orders_processing_lambda.zip .<br>***

Deploy/Push the zip file manually, s3 or using CLI.
