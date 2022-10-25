
def hello():
    nome = input('Informe seu nome ')
    return nome


if __name__ == "__main__":
    nome_pes = hello()
    print(f'Olá {nome_pes} seja bem vindo(a)')