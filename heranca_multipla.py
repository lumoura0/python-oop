class Animal:
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        pass

class Mamifero(Animal):
    def amamentar(self):
        return f"{self.nome} está amamentando."

class Ave(Animal):
    def voar(self):
        return f"{self.nome} está voando."

class Morcego(Mamifero, Ave):
    def emitir_som(self):
        super().emitir_som()
        return "Morcego faz um som característico."

Morcego = Morcego("Batman")
# criando uma instância da classe Morcego
# accessando os métodos de ambas as classes
print("Nome do morcego:", Morcego.nome)
print(Morcego.voar())
print(Morcego.emitir_som())
print(Morcego.amamentar())