import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol_carros = mydb["carros"]

for carro in mycol_carros.find():
    print(carro)