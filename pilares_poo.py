# Programação Orientada a Objetos
# Pilares da POO
# 1. Abstração
# 2. Encapsulamento
# 3. Herança
# 4. Polimorfismo

# Exemplo de Herança
print("\nExemplo de Herança")
class Animal:
    def __init__(self, nome):
        self.nome = nome
    
    def andar(self):
        print(f"{self.nome} está andando.")
        
    def emitir_som(self):
        pass

class Cachorro(Animal):
    def emitir_som(self):
       return "Au Au!"

class Gato(Animal):
    def emitir_som(self):
        return "Miau!"

dog = Cachorro(nome="Rex")
cat = Gato(nome="Mia")

# print(f"Nome do cachorro: {dog.nome}")
# print(f"Nome do gato: {cat.nome}")

print("\nExemplo de Polimorfismo")
animais = [dog, cat]
for animal in animais:
    print(f"{animal.nome} faz: {animal.emitir_som()}")

print("\nExemplo de Encapsulamento")
class ContaBancaria:
    def __init__(self, saldo) -> None:
        self.__saldo = saldo # Atributo privado
    
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de {valor} realizado. Saldo atual: {self.__saldo}")
        else:
            print("Valor de depósito inválido.")
    
    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Saque de {valor} realizado. Saldo atual: {self.__saldo}")
    
    def consultar_saldo(self):
        return self.__saldo

conta = ContaBancaria(saldo=1000)
print(f"Saldo inicial: {conta.consultar_saldo()}")
conta.depositar(500)
conta.sacar(200)
print(f"Saldo final: {conta.consultar_saldo()}")


print("\nExemplo de Abstração")
from abc import ABC, abstractmethod

class Veiculo(ABC):
    @abstractmethod
    def ligar(self):
        pass
    
    @abstractmethod
    def desligar(self):
        pass

class Carro(Veiculo):
    def __init__(self) -> None:
        pass
    
    def ligar(self):
        # Simula o processo de ligar o carro
        return "Carro ligado."
    
    def desligar(self):
        # Simula o processo de desligar o carro
        return "Carro desligado."


carro_amarelo = Carro()
print(carro_amarelo.ligar())
print(carro_amarelo.desligar())