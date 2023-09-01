from pymongo.mongo_client import MongoClient
import pandas as pd 
import json

uri = "mongodb+srv://mithileshjaiswal:1234mithi@cluster0.p1yajf0.mongodb.net/?retryWrites=true&w=majority"

# create new client and connect to the server
client = MongoClient(uri)

# create database and collection name
DATABASE_NAME = 'ML_Project'
COLLECTION_NAME = 'CreditData'

# read data frame
df = pd.read_csv(r'/config/workspace/Credit-card-fault-detection/dataset/UCI_Credit_Card.csv')

# convert data into json
json_records = list(json.loads(df.T.to_json()).values())

# dumping the json's record's in database
client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_records)


