#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 15:42:54 2021

@author: anabeatrizmacedo
"""

1.
x = -1

if x < 0:
  raise Exception("Número menor do que zero")
  
2.
def num():
        try:
            num1 = int(input("Digite um número: "))
        except:
            print ("Você não digitou um número!")
            num2 = int(input("Tente novamente. Digite um número: "))
        finally:
            print ("Obrigado!")
        print (val) 
num()

3. Lista = ['a', 'e', 'i', 'o', 'u']
for index, res in enumerate(Lista):
    if index < 3:
        print(res)
4.
listaA = [0, 2, 4]
listaB = [1, 3, 5]
listaC = [12, 8, 5]
list(map(lambda x, y, z: x*y*z, listaA, listaB, listaC))

5.
lista_num = [1, -1, -2, 2, 3, -3, -4, -5]
list(filter(lambda x: x<0, lista_num))