import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]

#verificando se ele existe
dblist = myclient.list_database_names()

if "mydatabase" in dblist:
    print("eu existo")
else:
    print("Nao existo")