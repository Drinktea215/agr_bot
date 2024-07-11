from pymongo import MongoClient
from pymongo.errors import BulkWriteError
import bson
from config import DB_HOST, DB_PORT, DB_NAME, DB_COLL

mongo_client = MongoClient(f"mongodb://{DB_HOST}:{DB_PORT}/")

try:
    db = mongo_client[f"{DB_NAME}"]
    salary = db[f"{DB_COLL}"]

    with open('sampleDB/sample_collection.bson', 'rb') as f:
        documents = bson.decode_all(f.read())

    salary.insert_many(documents)

except BulkWriteError:
    pass
