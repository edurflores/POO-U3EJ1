# -*- coding: utf-8 -*-
"""
Created on Mon May 24 19:26:52 2021

@author: Eduardo
"""

class Capitulo:
    __titulo = ''
    __cantidadPaginas = 0
    def __init__(self,titu,pags):
        self.__titulo = titu
        if type(pags) is int:            
            self.__cantidadPaginas = pags
    def GetTituCap(self):
        return self.__titulo
    def GetCantPags(self):
        return self.__cantidadPaginas