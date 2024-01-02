import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

#informando a tabela
mydb = myclient["mydatabase"]

mycol = mydb["customers"]

mydict = {"name" : "Murilo", "address": "Rua Potengi 1112"}

# A função insert_one insere um objeto na tabela
x = mycol.insert_one(mydict)

# Insere um id ao objeto
print(x.inserted_id)

