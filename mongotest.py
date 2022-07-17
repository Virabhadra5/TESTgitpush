import pymongo
client = pymongo.MongoClient("mongodb+srv://ineuron:1234@cluster0.vnqyz.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)

d={
    "name":"sudhanshu",
    "email":"sudhanshu@ineuron.ai",
    "surname":"kumar"
}

db1=client['mongtest']
coll=db1['test']
coll.insert_one(d)