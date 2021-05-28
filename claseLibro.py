# -*- coding: utf-8 -*-
"""
Created on Sun May 23 22:20:41 2021

@author: Eduardo
"""

class Libro:
    __idLibro = 0
    __titulo = ''
    __autor = ''
    __editorial = ''
    __isbn = 0
    __cantidadCapitulos = 0
    __listacapis = None # Lista de objetos de clase capitulo
    def __init__(self,idl,tit,aut,edit,isn,cantcapis):
        if type(idl) is int:
            self.__idLibro = idl
        self.__titulo = tit
        self.__autor = aut
        self.__editorial = edit
        if type(isn) is int:
            self.__isbn = isn
        if type(cantcapis) is int:
            self.__cantidadCapitulos = cantcapis
        self.__listacapis = []
    def AgregaCapitulo(self,unCapitulo):
        self.__listacapis.append(unCapitulo)
    def GetId(self):
        return self.__idLibro
    def GetTitu(self):
        return self.__titulo
    def GetAutor(self):
        return self.__autor
    def GetEditor(self):
        return self.__editorial
    def GetIsbn(self):
        return self.__isbn
    def GetCantCapi(self):
        return self.__cantidadCapitulos
    def GetListaCapis(self):
        return self.__listacapis