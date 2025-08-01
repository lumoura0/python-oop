# @classmethod
# @staticmethod
# Decoradores comuns em Python

class MinhaClasse:
    valor = 10
    def __init__(self, nome):
        self.nome = nome # atributo de instância
    # requer uma instância para ser chamado
    def metodo_instancia(self):
        return f'Método de instância: {self.nome}'
    
    @classmethod
    def metodo_classe(cls):
        return f'Método de classe: {cls.valor}'
    
    @staticmethod
    def metodo_estatico():
        return 'Método estático: não depende de instância ou classe'
    

obj = MinhaClasse(nome='Exemplo')
print(obj.metodo_instancia())  # Chama o método de instância
print(MinhaClasse.metodo_classe())  # Chama o método de classe
print(MinhaClasse.metodo_estatico())  # Chama o método estático
print(obj.metodo_estatico())  # Também pode ser chamado pela instância


class Carro:
    def __init__(self, marca, modelo, ano):
        self.modelo = modelo
        self.marca = marca
        self.ano = ano
    
    @classmethod
    def criar_carro(cls, configuracao):
        marca, modelo, ano = configuracao.split(',')
        return cls(marca, modelo, int(2025))

configuracao1 = "Toyota,Corolla,2025"
carro1 = Carro.criar_carro(configuracao1)
print(carro1.marca)  # Saída: Toyota
print(carro1.ano)    # Saída: 2025
print(carro1.modelo)  # Saída: Corolla

class Matematica:
    @staticmethod
    def soma(a, b):
        return a + b

print(Matematica.soma(5, 3))