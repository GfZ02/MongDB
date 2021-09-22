import pymongo
from pymongo import MongoClient
import json
import pandas as pd

with open("keys.json") as keys:
    vars = json.load(keys)['mongo_users']['gfz02']

user = vars[0]
senha = vars[1]

link = f"mongodb+srv://{user}:{senha}@firstcluster.d3xpy.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

cluster = MongoClient(link)

database = cluster['sample_training']

collection = database['zips']

result = collection.find()

df = pd.DataFrame(list(result))

df['loc_x'] = df['loc'].apply(lambda x: x['x'])
df['loc_y'] = df['loc'].apply(lambda x: x['y'])
df = df.drop(columns=['loc'])
df