from flask import Flask, render_template, request
from database import colecao
from datetime import datetime
# inicialize servidor com o nome deste arquivo 
app = Flask(__name__)

@app.route('/ini')
def index():
    
    # incomplete = Todo.query.filter_by(complete=False).all()
    # complete = Todo.query.filter_by(complete=True).all()

    return render_template('index.html')

@app.route('/handle_data', methods=['POST','GET'])
def handle_data():
    projectpath = request.form['projectFilepath']
    # print(projectpath)
    documento1 = {"nome": f"{projectpath}", "idade": "18","caracteristicas": "vira lata branco e preto", "Status": "Não Encontrado"}
    filme = colecao.insert_one(documento1)
    filme
    # your code
    # return a response
    return render_template('index.html')


@app.route('/add', methods=['POST','GET'])
def add():
    # documento1 = {"nome": "amigos", "episódios": 238,"estréia": datetime(1994, 9, 22), "encerrado": True}
    # filme = colecao.insert_one(documento1)
    texto =request.form["todoitem"]
    print(texto)
    return render_template('index.html')


@app.route("/", methods=['POST','GET'])
def mostrar_pagina_principal():
    return render_template('index.html')

# @app.route("/sobre")
# def mostrar_pagina_sobre(): 
#     return "Olá" 

# @app.route("/sequencia/<int:numero_final>") 
# def imprimir_sequencia(numero_final): 
#     texto_da_contagem = ""
#     for numero in range(1, numero_final + 1): 
#         texto_da_contagem += str(numero) + " "
#     return texto_da_contagem 
app.run(port=5000)