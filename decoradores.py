# Um decorador é um tipo especial de função que permite modificar ou estender o comportamento de outras funções, sem precisar alterar o código original delas.

def meu_decorador(func):
    def wrapper():
        print("Antes da execução da função.")
        func()
        print("Depois da execução da função.")
    return wrapper

# Aplicando o decorador à função
@meu_decorador
def minha_funcao():
    print("Esta é a minha função.")

# Chamando a função decorada
minha_funcao()

class MeuDecoradorDeClasse:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("Antes da execução do método da classe.")
        self.func()
        print("Depois da execução do método da classe.")
        return 

@MeuDecoradorDeClasse
def segunda_funcao():
    print("Esta é a segunda função.")

segunda_funcao()