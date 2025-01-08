import pymongo
import boto3
import json
import pandas as pd 
from GenerateEmbeddings import generate_embeddings

# try:
#     client = pymongo.MongoClient(
#     host="mongodb://paperpal:paperpal123@localhost:27017",
#     # port=27017,
#     # username="paperpal",
#     # password="paperpal123",
#     retryWrites=False,
#     tls=True,
#     tlsCAFile="global-bundle.pem",
#     tlsAllowInvalidHostnames=True,
#     directConnection=True) #Check the path as per your destination
#     print(client.server_info())  # This will confirm connection
#     print("hi")
# except Exception as e:
#     print("Error:", e)


class DocumentDBVectorSearch:

    def __init__(self):

        self.client = pymongo.MongoClient(
            host="mongodb://paperpal:paperpal123@localhost:27017",
            retryWrites=False,
            tls=True,
            tlsCAFile="global-bundle.pem",
            tlsAllowInvalidHostnames=True,
            directConnection=True)

        self.collection = self.client["mydatabase"]["embeddings"]

    def add_texts(self,texts:list):

        embeddings = generate_embeddings(texts)

        json_docs = [
            {
                "text":texts[i],
                "embedding": embeddings[i].tolist()
            }
            for i in range(len(texts))
        ]

        self.collection.insert_many(json_docs)

        print("Documents inserted successfully.")
     
# db = client["mydatabase"]
# collection = db["embeddings"]

# collection.delete_one({ 'name': "try" })
# result = collection.find({ 'name': "try" })

# for doc in result:
#     print(doc)

# data = {
#     'name': "try",
#     "by": "manav"
# }

# collection.insert_one(data)