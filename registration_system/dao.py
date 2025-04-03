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
    def salvar_usuarios(usuarios):
        try:
            with open("database.json", "w") as arq:
                json.dump(usuarios, arq, indent=4)
                return True
        except Exception as E:
            return False