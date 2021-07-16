#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 14:27:41 2021

@author: anabeatrizmacedo
"""

1. 
from math import sqrt
def hipotenusa(a, b):
  return sqrt(a**2+b**2)
def catetos():
    a = int(input('Digite um cateto: '))
    b = int(input('Digite outro cateto: '))
    print('O valor da Hipotenusa será: {}'.format(hipotenusa(a, b)))
catetos()

2.
def Par():
    for k in range(2, 26, 2): 
        print(k)
Par()    

3.
def fah2cel(fah):
    return (fah - 32) * 5/9

def graus():
    temp = float(input('Qual o valor em Fahrenheit deseja converter?'))
    print('O valor em Celcius será: {} '.format(fah2cel(temp)))
    
graus()

4.
fah2cel = lambda fah: (fah - 32) * 5/9
fah2cel(32)

5.
from math import pi
def area(raio):
  r = pi*raio**2
  return r
def raio():
  raio = int(input('Digite o raio do círculo: '))
  print('A área do círculo é: {}'.format(area(raio)))
raio()