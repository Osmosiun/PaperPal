import pymongo
import boto3
import json
import pandas as pd 
from GenerateEmbeddings import generate_embeddings

class DocumentDBVectorSearch:

    def __init__(self):

        self.client = None

        self.collection = None

        self.index_created = False
    
    def create_index(self):
        if not self.collection.index_information():

            self.collection.create_index([("embedding","vector")],
                                         vectorOptions= {
                                             "type": "hnsw", 
                                             "similarity": "cosine",
                                             "dimensions": 1024,
                                             "m": 16,
                                             "efConstruction": 64},
                                             name="my_vss_index")
        self.index_created = True

    def establish_connection(self):

        print("Make sure you are running ssh tunnel before executing this function")

        try:
            self.client = pymongo.MongoClient(
                host="mongodb://paperpal:paperpal123@localhost:27017",
                retryWrites=False,
                tls=True,
                tlsCAFile="global-bundle.pem",
                tlsAllowInvalidHostnames=True,
                directConnection=True)
            
            self.collection =self.client["mydatabase"]["embeddings"]
        
        except Exception as e:
            print(e)

    def add_texts(self,texts:list): 

        if not self.index_created:
            raise ValueError("Index Not Created yet. Create the Index first")

        try:

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
        
        except Exception as e:
            raise Exception(print(e))
    
    def vector_search(self, prompt, num_results=3, use_hnsw=True):

        if not self.index_created:
            raise ValueError("Index Not Created yet. Create the Index first")

        try:
            prompt_embed = generate_embeddings([prompt])[0].tolist()
            query = {"vectorSearch" : {"vector" : prompt_embed, "path": "embedding", "similarity": "cosine", "k": num_results}}
            # if not use_hnsw:
            # Needs to write logic for this
            #     query["vectorSearch"]["index"] = None
            results = self.collection.aggregate([{'$search': query}])
            return list(results)
        except Exception as e:
            raise Exception(print(e))
    
    def delete_all_documents(self):
        try:
            self.collection.delete_many({})
            print("Delete all documents successfully.")
        except Exception as e:
            raise Exception(print(e))