from flask import jsonify
from flask_restful import Resource, reqparse
from app.models.alunos import Alunos

class Index(Resource):
    def get(self):
        return jsonify("Notas de alunos")

#definir quais argumentos são esperados e como devem ser tratados.   
argumentos = reqparse.RequestParser() #Cria um objeto RequestParser
argumentos.add_argument('cpf', type=int)
argumentos.add_argument('nome', type=str)
argumentos.add_argument('data_nasc', type=str)
argumentos.add_argument('idade', type=int)
argumentos.add_argument('sexo', type=str)
argumentos.add_argument('av1', type=float)
argumentos.add_argument('av2', type=float)
argumentos.add_argument('media', type=float)

class AlunoCreate(Resource):
    def post(self):
        try:
            datas = argumentos.parse_args() #obter os valores dos argumentos,armazenados em um dicionario
            user = Alunos(**datas) #descompactar os valores do dicionário como argumentos do construtor da classe
            user.save_alunos() #salvar no banco de dados o objeto
            return {"message": 'Aluno registrado com sucesso!'}, 201

        except Exception as e:
            return jsonify({'status': 500, 'msg': f'{e}'}), 500

class AlunosSearch(Resource):
    
    def get(self):
        try:
            return {'alunos': [alunos.json() for alunos 
                                  in Alunos.query.all()]} #retorna um dicionário com uma lista de alunos (alunos) em formato JSON,a partir de todos os alunos encontrados na consulta ao banco de dados
        except Exception as e:
            return jsonify({'status': 500, 'msg': f'{e}'}), 500