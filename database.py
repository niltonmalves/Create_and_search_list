from pymongo import MongoClient
from pymongo import ASCENDING, DESCENDING
from datetime import datetime

cliente = MongoClient("localhost", 27017)


banco = cliente["Animais"]
colecao = banco["perdidos"]

# class Pets(colecao):
#     # insere = colecao.insert_one()
#     # procura_um = colecao.find_one()
#     colecao = colecao
    
# busca = {"encerrado": False}

# ordenacao = [ ["estréia", ASCENDING] ]

# documento1 = {"nome": "Friends", "episódios": 236,\
# "estréia": datetime(1994, 9, 22), "encerrado": True}
# # colecao.insert_one(documento1)

# busca = {"nome": "Friends"}

# documento = colecao.find_one(busca)
# print(documento)

# print(list( colecao.find(busca, sort=ordenacao) ))