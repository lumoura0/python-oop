# Personagem: classe mãe
# Heroi: controlado pelo usuario
# Inimigo: adversário do usuario

class Personagem:
    def __init__(self, nome, vida, nivel):
        self.__nome = nome
        self.__vida = vida
        self.__nivel = nivel

    def get_nome(self):
        return self.__nome
    def get_vida(self):
        return self.__vida
    def get_nivel(self):
        return self.__nivel
    
    def exibir_detalhes(self):
        return f"Nome: {self.get_nome()}, \nVida: {self.get_vida()}, \nNível: {self.get_nivel()}"

class Heroi(Personagem):
    def __init__(self, nome, vida, nivel, habilidade):
        super().__init__(nome, vida, nivel)
        self.__habilidade = habilidade
    
    def get_habilidade(self):
        return self.__habilidade
    
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}, \nHabilidade: {self.get_habilidade()}\n"

class Inimigo(Personagem):
    def __init__(self, nome, vida, nivel, tipo):
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo
    
    def get_tipo(self):
        return self.__tipo
    
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()},\nTipo: {self.get_tipo()}\n"

heroi = Heroi(nome="Guerreiro", vida=100, nivel=1, habilidade="Ataque Poderoso")
print(heroi.exibir_detalhes())
Inimigo = Inimigo(nome="Orc", vida=80, nivel=1, tipo="Besta")
print(Inimigo.exibir_detalhes())