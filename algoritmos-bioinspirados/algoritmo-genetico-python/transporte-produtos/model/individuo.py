from random import random

class Individuo():
    def __init__(self, espacos, valores, limite_espaco, cromossomo=None, geracao=0):
        self.espacos = espacos
        self.valores = valores
        self.limite_espaco = limite_espaco
        self.nota_avaliacao = 0
        self.espaco_usado = 0
        self.geracao = geracao
        self.cromossomo = cromossomo if cromossomo is not None else []
        self.inicializa_cromossomo()
        
    def inicializa_cromossomo(self):
        if(len(self.cromossomo) == 0):
            for i in range(len(self.espacos)):
                if(random() < 0.5):
                    self.cromossomo.append("0")
                else:
                    self.cromossomo.append("1")
    
    def avaliacao(self):
        nota = 0
        soma_espacos = 0
        for i in range(len(self.cromossomo)):
            if(self.cromossomo[i] == "1"):
                nota += self.valores[i]
                soma_espacos += self.espacos[i]
        
        if(soma_espacos > self.limite_espaco):
            nota = 1
        self.nota_avaliacao = nota
        self.espaco_usado = soma_espacos
    
    def crossover(self, outro_individuo):
        corte = round(random() * len(self.cromossomo))
        filho1 = self.cromossomo[0:corte] + outro_individuo.cromossomo[corte::]
        filho2 = outro_individuo.cromossomo[0:corte] + self.cromossomo[corte::]
        filhos = [Individuo(self.espacos, self.valores, self.limite_espaco, filho1, self.geracao+1),
                  Individuo(self.espacos, self.valores, self.limite_espaco, filho2, self.geracao+1)]
        return filhos
    
    def mutacao(self, taxa_mutacao):
        for i in range(len(self.cromossomo)):
            if(random() < taxa_mutacao):
                if(self.cromossomo[i] == "1"):
                    self.cromossomo[i] = "0"
                else:
                    self.cromossomo[i] = "1"
        return self

    def __str__(self) -> str:
        return f"""Geracao: {self.geracao} \nNota: {round(self.nota_avaliacao, 2)} \nEspaço usado: {round(self.espaco_usado, 2)} \nCromossomo: {self.cromossomo}"""