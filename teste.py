import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol_carros = mydb["carros"]
mycol_placas = mydb["placa_carro"]

while True:
    nome_carro = input("Insira o nome do carro: ")

    inserir_carro = mycol_carros.insert_one({
        "nome": nome_carro
    })
    
    x = input("Deseja finalizar? ").lower()

    if x == "sim":
        # Atualiza o nome do carro
        mycol_carros.update_one({"nome": nome_carro}, {"$set": {"nome": "Opala SS"}})
        
        # Insere o nome do carro na coleção placa_carro
        insere = mycol_placas.insert_one({"nome": nome_carro})
        break
