class Pessoa:
    def __init__(self, *filhos, nome = None, idade = 57):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'olá {id(self)}'

if __name__ == '__main__':
    jean = Pessoa(nome='Jeam')
    luciana = Pessoa(jean, nome='Luciana')
    print(Pessoa.cumprimentar(luciana))
    print (id(luciana))
    print (luciana.cumprimentar())
    print (luciana.nome)
    print (luciana.idade)
    for filho in luciana.filhos:
        print(filho.nome)
    print(luciana.filhos)
