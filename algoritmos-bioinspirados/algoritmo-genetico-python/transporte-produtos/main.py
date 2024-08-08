from model.algoritmo_genetico import AlgoritmoGenetico
from model.produto import Produto
import matplotlib.pyplot as plt
import pymysql

lista_produtos = []
conexao = pymysql.connect(host="localhost", user="root", passwd="123456", db="produtos")
cursor = conexao.cursor()
cursor.execute('select nome, espaco, valor, quantidade from produto')
for produto in cursor:
    for i in range(produto[3]):
        lista_produtos.append(Produto(produto[0], produto[1], produto[2]))

cursor.close()
conexao.close()

espacos = []
valores = []
nomes = []
limite = 10
tamanho_populacao = 20
taxa_mutacao = 0.05
numero_geracoes = 200

for produto in lista_produtos:
    espacos.append(produto.espaco)
    valores.append(produto.valor)
    nomes.append(produto.nome)

ag = AlgoritmoGenetico(tamanho_populacao)
ag.executa(espacos, valores, limite, numero_geracoes, taxa_mutacao)

print("---------- Melhor Resultado ----------")
print(ag.melhor_solucao)
ag.produtos_selecionados(ag.melhor_solucao, nomes)
print("--------------------------------------")
resultados_valores = []
for i in range(len(ag.lista_solucoes)):
    resultados_valores.append(ag.lista_solucoes[i].nota_avaliacao)

plt.plot(resultados_valores)
plt.title("Acompanhamento das gerações")
plt.show()