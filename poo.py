# POO

# Classe exemplo
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

# Criando uma instância da classe Pessoa
pessoa1 = Pessoa("Shiro", 22)
# Chamando o método apresentar
pessoa1.apresentar()