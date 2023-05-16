from app import db

class Alunos(db.Model):
    __tablename__ = 'alunos'
    __table_args__ = {'sqlite_autoincrement': True} #ja faz o auto-incremento para as chaves primarias
    cpf = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255))
    data_nasc = db.Column(db.String(20))
    sexo = db.Column(db.String(9))
    idade = db.Column(db.Integer)
    av1 = db.Column(db.Float)
    av2 = db.Column(db.Float)
    media = db.Column(db.Float)

    def __init__(self, cpf, nome, data_nasc, sexo, idade, av1, av2, media):
        self.cpf=cpf
        self.nome = nome
        self.data_nasc = data_nasc
        self.sexo = sexo
        self.idade = idade
        self.av1 = av1
        self.av2 = av2
        self.media = media
    
    def json(self): #retornar a representação nesse formato de dicionario
        return {
            'nome': self.nome,
            'data_nasc': self.data_nasc,
            'sexo': self.sexo,
            'idade': self.idade,
            'av1': self.av1,
            'av2': self.av2,
            'media':self.media
        }
    
    def save_alunos(self): #salvar a instancia no banco de dados
        try:
            db.session.add(self) #adicionar a instância
            db.session.commit() #confirma
        except Exception as e: #se a operação de salvar falhas, cai na exceção
            print(e)