class User:
    def __init__(self, nome, email, idade):
        self.nome = nome
        self.email = email
        self.idade = idade
    
    def formatar_dict(self):
        return {'nome': self.nome, 'email': self.email, 'idade': self.idade} 