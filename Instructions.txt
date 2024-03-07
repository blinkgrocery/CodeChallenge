S3 (.txt)files finder in python

This Python script allows you to search for text files containing a specified substring within an Amazon Web Services (AWS) Simple Storage Service (S3) bucket. Follow these steps to set up and use the script:

## Prerequisites
Install Python 3
 - If you haven’t already, install Python 3 on your system. You can download it from the official Python website.
Install AWS CLI:
https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
 - You can use CMD or installer (make sure you had administrator rights)

## Setup
Install Boto3:
 - Open your terminal or command prompt.
 - Run the following command to install the Boto3 library (AWS SDK for Python):
 - For Python-2.x:  "pip install boto3"  
 - For Python-3.x:  "pip3 install boto3"


## Configure AWS Credentials:
 - Ensure you have valid AWS credentials (access key and secret key) with read access to the desired S3 bucket.
 - You can configure credentials using either the AWS CLI or AWS Portal.(Make sure you keep record of Access Key ID,Secret Access Key,Bucket and Bucket region we will be using this when connecting to AWS)
 - Ensure the AWS user has the necessary permissions for the specified S3 bucket.In Aws Pemission Policy assign "AmazonS3ReadOnlyAccess"

## Script Setup

1. Download the Script:
 - Create a new Python file named codechallenge.py in your preferred directory.

2.Edit the Script:
Replace the placeholders with your specific values:
 * s3_bucket_name = 'your-bucket-name' (This is S3 bucket name where we will be looking for .txt file)
 * substring = 'your-substring'( The is the substring in my case my files name contained "Test" ) so any file name that contain Test will show up.

Ensure you replace 'your-bucket-name' with the actual S3 bucket name and 'your-search-term' with the substring you want to search for.

## Usage
first step is to run "aws configure" in cmd and provide the following details:
 - AWS Access Key ID [****************4V5J]: Your aws access key ID  
 - AWS Secret Access Key [****************FOh3]: Your Secret access key
 - Default region name [eu-west-1]: your s3 bucket region
 - Default output format [json]: output format

Open command prompt and type "cd C:\path\to\location\codechallenge.py"
Then run the file using cmd  "python codechallenge.py"
The script will output the names of text files containing the specified substring in the S3 bucket.Please see the result screenshot attached


## Note

- The script is limited to `.txt` files but can be adjusted for other file types by changing .