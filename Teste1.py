print("hello word", "eu sou a Sofia")
name = "sofia"
idade = "15"
altura = "1,52"
estudante = "true"

print("Nome: ", name)
print("Idade: ", idade)
print("Altura: ", altura)
print("Estudante: ", estudante)

print(type(name))
print(type(idade))
print(type(altura))
print(type(estudante))

a=10
b=3

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)

nota1=7.5
nota2=8.0
nota3=6.5
media=(nota1+nota2+nota3)/3
ptint=("media das notas: ",media)

nome_usuario=input("digite seu nome:")
print("ola, ", nome_usuario)

idade_usuario = input("digite sua idade:")
idade_usuario = int(idade_usuario)
print("em 5 anos sua idade sera" ,idade_usuario+5)

import math

print("raiz quadrada de 16:", math.sqrt(16))
print("valor de pi:", math.pi)

import numpy as np

numeros = np.array([2,4,6,8,10])

print("arrary de numeros:" ,numeros)
print("media:" ,np.max(numeros))
print("maior valor:" ,np.max(numeros))

import pandas as pd
import seaborn as sns

dados = {"nome" :["ana" ,"beatriz"],"idade":[16,17],"nota":[7.5,8.0]}
df = pd.DataFrame(dados)
sns.barplot(x="nome" ,y="nota",data=df)

import matplotlib.pyplot as plt
plt.show()