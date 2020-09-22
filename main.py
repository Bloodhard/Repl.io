"""Programa de Cryptografia usando cifra de CESAR"""
import sys #biblioteca para funções do sistema
import string #biblioteca para manipulação de texto

arquivo = open(sys.argv[1] , 'r').read().lower() #abre o arquivo em modo leitura
rotacao = int(sys.argv[2]) #O usuario nos informa a quantidade de rotações
alfabeto = string.lowercase #alfabeto de A até Z
resultado = '' #Vamos armazenar o resultado final arquivo

for letra in arquivo:
  if letra in alfabeto:
    posicao = alfabeto.find(letra)
    posicao = (posicao + rotacao) % 26
    resultado = resultado + alfabeto[posicao]
    print (resultado)
    
