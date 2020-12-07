class Pessoa:
    def __init__(self, nome = None, idade = 57):
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return f'olá {id(self)}'

if __name__ == '__main__':
    p = Pessoa ('Luciana')
    print(Pessoa.cumprimentar(p))
    print (id(p))
    p.nome ='Jean'
    print (p.nome)
    print (p.idade)
