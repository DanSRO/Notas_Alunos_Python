from flask import Flask
from flask_sqlalchemy import SQLAlchemy #SQLAlchemy é uma biblioteca de mapeamento objeto-relacional (ORM) para Python
from flask_restful import Api #gerenciar rotas, recursos e outros aspectos para APIs RESTful
import sqlite3

app = Flask(__name__)
#configuração com banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///alunos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # desativando o rastreamento de modificações do SQLAlchemy no app Flask

db = SQLAlchemy(app)
api = Api(app)

from app.models.alunos import Alunos
with app.app_context(): #garantir que as tabelas existam antes que a aplicação Flask comece a lidar com as solicitações.
    db.create_all()

from app.resources.notas_alunos import Index,AlunoCreate, AlunosSearch
api.add_resource(Index, '/') #como se fosse a rota, so que com a chamada da api
api.add_resource(AlunoCreate, '/criar')
api.add_resource(AlunosSearch, '/buscar_todos')
#uma forma
'''
@app.route("/")
def index():
    return "<h1> Minha Aplicação em Flask</h1>"
'''

