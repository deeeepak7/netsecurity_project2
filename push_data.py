import os
from  networksecurity.logging.logger import logging
from networksecurity.exception.exception import customException
import json
import sys
from load_dotenv import load_dotenv

load_dotenv()

mongo_url = os.getenv("mongo_url")

import certifi

ca = certifi.where()

import pymongo
import pandas as pd

class networkdataextract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise customException(e,sys)
        
    def cv_to_json(self,file_path):
        try:
            data=pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True)
            record=list(json.loads(data.T.to_json()).values()) 
            return record
        except Exception as e:
            raise customException(e,sys)


    def insert_data_mongodb(self, record, database, collection):
        try:
            self.record = record
            self.database = database
            self.collection = collection
            self.mongo_client = pymongo.MongoClient(mongo_url, ca)
            db = self.mongo_client[self.database]
            coll = db[self.collection]
            coll.insert_many(self.record)
            return len(self.record)
        except Exception as e:
            raise customException(e, sys)


if __name__ == "__main__":
     File_path =r"C:\project\netsecurity\network_data\phisingData.csv"
     database = "deepakreturn"
     collection = "phishingData"
     networkobj = networkdataextract()
     record = networkobj.cv_to_json(file_path=File_path)
     print(record)
     no_of_record = networkobj.insert_data_mongodb(record,database,collection)
     print(no_of_record, "record inserted successfully")