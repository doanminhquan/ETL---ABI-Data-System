from pymongo import MongoClient
import pandas as pd
import numpy as np
from Etl.Transform import TransformData
from . import host, port, dbname  # Import các biến cấu hình từ __init__.py


def connect_mongodb():
    client = MongoClient(f'mongodb://{host}:{port}/')
    db = client.get_database(dbname)
    return db

def get_data_collection_into_df(db, name_collection):
    collection = db.get_collection(name_collection)
    cursor = collection.find({})
    data = list(cursor)
    df = pd.DataFrame(data)
    df.replace(np.nan, None, inplace=True)
    return df