'''Criar um sistema Orientado a Objeto que Lê o arquivo iris.data.
Gravar em outro arquivo de saida chamado resultado.txt as seguintes informações:
A quantidade de flores de cada tipo;
e qual é o maior  sepal length  de cada classe de flor.'''

class Arquivo:
    def __init__(self):
        self.vetor = []
        self.vetor2 = []
        self.vetor_setosa = []
        self.vetor_versicolor = []
        self.vetor_virginica = []
    
    def abre_arquivo(self):
        self.arquivo = open('iris.data', 'rt')

    def transformar_em_vetor(self):
        for linha in self.arquivo:
            self.vetor.append(linha.replace('\n', '')[16:])
            self.vetor2.append(linha.replace('\n', '')[0:3])
        for i in range(50):
            self.vetor_setosa.append(self.vetor2[i])
        self.vetor_setosa.sort()
        for i in range(50, 100):
            self.vetor_versicolor.append(self.vetor2[i])
        self.vetor_versicolor.sort()
        for i in range(100, 150):
            self.vetor_virginica.append(self.vetor2[i])
        self.vetor_virginica.sort()
            
    def contar_setosa(self):
        self.qtd_setosas = self.vetor.count('Iris-setosa')

    def contar_versicolor(self):
        self.qtd_versicolor = self.vetor.count('Iris-versicolor')

    def contar_virginica(self):
        self.qtd_virginica = self.vetor.count('Iris-virginica')

    def maior_sepal_length(self):
        self.setosa_sepal_length = self.vetor_setosa[len(self.vetor_setosa) - 1]
        self.versicolor_sepal_length = self.vetor_versicolor[len(self.vetor_versicolor) - 1]
        self.virginica_sepal_length = self.vetor_virginica[len(self.vetor_virginica) - 1]

    def fecha_arquivo(self):
        self.arquivo.close()

    def abrir_escrita(self):
        self.arquivo_saida = open('resultado.txt', 'wt')
    
    def escrever(self):
        self.texto = [
            'Quantidade de Iris-setosa: ', str(self.qtd_setosas),
            '\nQuantidade de Iris-versicolor: ', str(self.qtd_versicolor),
            '\nQuantidade de Iris-virginica: ', str(self.qtd_virginica),
            '\nO maior sepal length da classe Iris-setosa tem: ', str(self.setosa_sepal_length), 'cm',
            '\nO maior sepal length da classe Iris-versicolor tem: ', str(self.versicolor_sepal_length), 'cm',
            '\nO maior sepal length da classe Iris-virginica tem: ', str(self.virginica_sepal_length), 'cm',
        ]
        self.arquivo_saida.writelines(self.texto)
    
    def fechar_saida(self):
        self.arquivo_saida.close()

#############################
teste = Arquivo()
teste.abre_arquivo()
teste.transformar_em_vetor()
teste.contar_setosa()
teste.contar_versicolor()
teste.contar_virginica()
teste.maior_sepal_length()
teste.fecha_arquivo()
teste.abrir_escrita()
teste.escrever()
teste.fechar_saida()