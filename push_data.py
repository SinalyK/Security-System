import os 
import sys
import json
import pandas as pd
import numpy as np
import pymongo
from pymongo.server_api import ServerApi
from src.logging.logger import logger
from src.exception.exception import NetworkSecurityException
import certifi
from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL=os.getenv("mongodb_uri")
ca=certifi.where()

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)

    def csv_to_json(self,file_path):
        try:
            data=pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True)
            #records=list(json.loads(data.T.to_json().values()))
            records=list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    def insert_data_to_mongodb(self,records,database,collection):
        try:
            self.database=database
            self.collection=collection
            self.records=records

            self.mongo_client=pymongo.MongoClient(MONGO_DB_URL,tlsCAFile=ca,server_api=ServerApi('1'))
            self.database=self.mongo_client[self.database]

            self.collection=self.database[self.collection]
            self.collection.insert_many(self.records)

            return(self.records)
        
        except Exception as e:
            raise NetworkSecurityException(e,sys)


if __name__=="__main__":
    FILE_PATH="Datas/phisingData.csv"
    DATABASE="SINALYK"
    collection="NETWORKDATA"
    networkobj=NetworkDataExtract()
    records=networkobj.csv_to_json(file_path=FILE_PATH)
    print(networkobj.insert_data_to_mongodb(records=records,database=DATABASE,collection=collection))

