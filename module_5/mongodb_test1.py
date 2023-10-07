"""    
    Author: John
    Date: 07 September 2023
    Description: Test program for connecting to a 
                 MongoDB Atlas cluster
"""

""" import statements """
from pymongo import MongoClient

# MongoDB connection string 
url="mongodb+srv://notadmin:not12345@cluster99.mgxdpzx.mongodb.net/"

# connect to the MongoDB cluster 
client = MongoClient(url)

# connect pytech database
db = client.pytech

# show the connected collections 
print("\n -- Pytech Collection List --")
print(db.list_collection_names())