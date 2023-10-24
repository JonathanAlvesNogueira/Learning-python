class Bicicleta:
    def __init__(self, cor, modelo, ano,valor ):
        self.cor = cor
        self.modelo = modelo 
        self.ano = ano
        self.valor = valor 
    # Passa o proprio objeto como parametro 
    def buzinar(self):
        print('biiiiiii')

    def parar(self):
        print('bicicleta parada')

    def correr(self):
        print('Vruuuum')

# cria objetos 
bike = Bicicleta('vermelha', 'bk12', 2018, 2000)
bike.correr()
bike.buzinar()
bike.parar()
### imprime atributos 
print(bike.cor, bike.modelo, bike.ano)
