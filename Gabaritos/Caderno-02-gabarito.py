#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 14:08:05 2021

@author: anabeatrizmacedo
"""

1.
num = int(input('Descubra se o número é Par ou Ímpar: '))
if num % 2 ==0:
  print('Esse número é Par.')
else:
  print('Esse número é Ímpar')
  
  
2.
contador = 0
for k in range(2, 99, 2):
  contador += 1
print(contador)

3. 

4.
nota1 = float(input('Qual a primeira nota?'))
nota2 = float(input('Qual a segunda nota?'))
média = (nota1+nota2)/2
if média >= 8:
  print('Aprovado! Sua média foi: {} '.format(média))
elif média >= 5:
  print('Aprovado! Sua média foi {}, mas pode melhorar'.format(média))
else:
  print('Reprovado. Estude mais')