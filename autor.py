class Autor:
    def __init__(self, nome: str, nacionalidade: str, dataNascimento: str):
        self.__nome = nome
        self.__nacionalidade = nacionalidade
        self.__dataNascimento = dataNascimento
    
    def get_nome(self):
        return self.__nome

    def set_nome(self, nome: str):
        self.__nome = nome

    def get_nacionalidade(self):
        return self.__nacionalidade

    def set_nacionalidade(self, nacionalidade: str):
        self.__nacionalidade = nacionalidade

    def get_dataNascimento(self):
        return self.__dataNascimento

    def set_dataNascimento(self, dataNascimento: str):

        self.__dataNascimento = dataNascimento
        
    def exibirAutor(self):
        print(f"Nome: {self.__nome}")
        print(f"Nacionalidade: {self.__nacionalidade}")
        print(f"Data de Nascimento: {self.__dataNascimento}")
