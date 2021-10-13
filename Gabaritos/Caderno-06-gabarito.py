#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 07:58:12 2021

@author: anabeatrizmacedo
"""


1.
class User():
    def __init__(self, nome, telefone, idade, país):
        self.nome = nome
        self.telefone = telefone
        self.idade = idade
        self.país = país
    def resgistro(self):
        print('O(a) ' + self.nome + ' tem ' +str(self.idade)+ ' e seu país é o(a)'+self.país)

user1 = User('Magali', 12345678, 45, 'Brasil')
user1.resgistro()

2.
class Smartphone(object):
    def __init__(self, gigas, interface):
        self.gigas = gigas
        self.interface = interface
        
class MP3Player(Smartphone):
    def __init__(self, capacidade, gigas = 'tamanho', interface = 'Gráfica'):
        self.capacidade = capacidade
        Smartphone.__init__(self, gigas, interface)
        
    def print_mp3player(self):
        print("Valores para o objeto criado: %s %s %s"  %(self.gigas, self.interface, self.capacidade))
    
device1 = MP3Player('64 GB')
device1.print_mp3player()

3.
class temperatura():
    def __init__(self, temp):
        self.temp = temp 
    def cel2kel(self):
        return self.temp + 273
    def setRaio(self, temp_kelvin):
        self.temp = temp_kelvin
temp1 = temperatura(0)
temp1.cel2kel()

4.
class Nacionalidade():
  def __init__(self, país, cidade):
    self.país = país
    self.cidade = cidade
  
  def resgistro(self):
    print('Essa pessoa mora no país '+ self.país+ ' e reside na cidade de '+self.cidade)
nacionalidade1 = Nacionalidade('Brasil', 'São Paulo')
nacionalidade1.resgistro()
