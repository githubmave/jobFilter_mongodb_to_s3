README


What is this repository for?


This data extraction process is mainly for extract and clean data from AWS datalake (json file).
How do I get set up?
this repo managed by data engineer team
Works divided into datapipeline, tags and trigger


Prerequisite


Install and deploy all requirements packages that not provide by AWS Lambda: pymongo, bason, dotenv.
Create a S3 Bucket as data lake to store pre-cleaned data that were extracted from MongoDB.
Create a AWS Lambda service for data extraction.
Set appropriate permission on AWS Lambda for accessing AWS S3.
Contruct an VPC peering between MongoDB and AWS Lambda for sercuity.
Set the MongoDB configuration and permissions. 1. Database Access:
connection driver: Python. version: 3.6 or later
Add your connection string into your application code. 



2. Network Access: 



1. Configure IP Access List Entries (This method should set static ip address for AWS Lambda.)


2. Set up a Network Peering Connection (This method is not available for M0 free clusters, M2, and M5 clusters.) 3. Set up a Private Endpoint (This method is not available for M0 free clusters, M2, and M5 clusters.)




Main Process



Use Python driver called, “PyMongo” to connect MongoDB Atlas.

Explore MongoDB Collections and Documents

Clean and filter out useful data objects like: users, jobs, etc.

Use boto3 Python SDK to connect AWS S3 bucket.

Load data objects into target AWS S3 bucket.

Files:

src folder contains main execution scripts. * src/mongodb_to_s3.py is where execute AWS Lambda handler method.
core folder contains all defined functions. * core/extract.py is where get collection object from MongoDB. * core/filter.py is where pre-clean collection for filtering necessary data. * core/load.py is where load data to S3 Bucket.
requirement.txt: is where list requirement external package need to be installed.
Contribution guidelines
