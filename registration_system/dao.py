import json

class UserDao():

    @staticmethod
    def carregar_usuarios():
        try:
            with open("database.json", "r") as arq:
                return json.load(arq)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
        
    
    @staticmethod
    def salvar_usuarios(usuario):
        try:
            with open("database.json", "w") as arq:
                json.dump(arq, usuario, indent=4)
        except Exception as E:
            return False, "⚠️ Erro ao salvar os dados."