# -*- coding: utf-8 -*-
"""
Created on Mon May 24 19:30:04 2021

@author: Eduardo
"""
import csv
from claseLibro import Libro
from claseCapitulo import Capitulo

class ManejaLibros:
    def __init__(self):
        self.__listaLibros = []
    def AgregaLibro(self,unLibro):
        self.__listaLibros.append(unLibro)
    def CargaLibros(self):
        archivo = open('archivoLibros.txt')
        reader = csv.reader(archivo, delimiter=',')
        for fila in reader:
            idlib = int(fila[0])
            titu = fila[1]
            autor = fila[2]
            edit = fila[3]
            isnb = int(fila[4])
            cantcapi = int(fila[5])
            unLibro = Libro(idlib, titu, autor, edit, isnb, cantcapi)
            for fila1 in reader:    
                titucap = fila1[0]
                pags = int(fila1[1])
                unCapitulo = Capitulo(titucap, pags)
                unLibro.AgregaCapitulo(unCapitulo)
                cantcapi -= 1
                if cantcapi == 0:
                    break
            self.AgregaLibro(unLibro)
        archivo.close()
        print('Se han cargado los libros.')
    def MuestraLibros(self): # Funcion que muestra todos los libros con sus capitulos, uso opcional
        print('Informacion de libros:')
        for i in range(len(self.__listaLibros)):
            print('Libro nro: ',i+1)
            print('----------------------------------------')
            print('Id de libro:{}'.format(int(self.__listaLibros[i].GetId())))
            print('Titulo:{}'.format(str(self.__listaLibros[i].GetTitu())))
            print('Autor:{}'.format(str(self.__listaLibros[i].GetAutor())))
            print('Editor:{}'.format(str(self.__listaLibros[i].GetEditor())))
            print('ISBN:{}'.format(int(self.__listaLibros[i].GetIsbn())))
            print('Cantidad capitulos:{}'.format(int(self.__listaLibros[i].GetCantCapi())))
            print('Capitulos')
            print('-----------')
            for j in range(len(self.__listaLibros[i].GetListaCapis())):
                print('Capitulo: ',j+1)
                print('Titulo: ',self.__listaLibros[i].GetListaCapis()[j].GetTituCap())
                print('Cantidad de paginas: ',self.__listaLibros[i].GetListaCapis()[j].GetCantPags())
            
    def MuestraInfo(self,idlibro): # Funcion para consigna 1
        print('---------------------')
        print('ID de libro ingresado:',idlibro)
        acum = 0 # Acumulador para cantidad de paginas
        for i in range(len(self.__listaLibros)):
            if self.__listaLibros[i].GetId() == idlibro:
                print('Titulo:{}'.format(str(self.__listaLibros[i].GetTitu())))
                print('Capitulos')
                print('---------------------')
                for j in range(len(self.__listaLibros[i].GetListaCapis())):
                    print('Capitulo {}: {} '.format(int(j+1),str(self.__listaLibros[i].GetListaCapis()[j].GetTituCap())))
                    acum += self.__listaLibros[i].GetListaCapis()[j].GetCantPags()
                print('Total de paginas del libro:{}'.format(int(acum)))
                break
    def BuscaPalabra(self,palabra):
        for i in range(len(self.__listaLibros)):
           aux = self.__listaLibros[i].GetTitu().split() # Arma lista con las palabras de la cadena
           if palabra in aux:
               print('Encontrado en')
               print('Libro: "{}"'.format(str(self.__listaLibros[i].GetTitu())))
               print('Autor: {}'.format(str(self.__listaLibros[i].GetAutor())))
           else:
               for j in range(len(self.__listaLibros[i].GetListaCapis())): # Si no esta en el titulo, busca en sus capitulos
                   aux = self.__listaLibros[i].GetListaCapis()[j].GetTituCap().split()
                   if palabra in aux:
                       print('Encontrado en')
                       print('Libro: "{}"'.format(str(self.__listaLibros[i].GetTitu())))
                       print('Autor: {}'.format(str(self.__listaLibros[i].GetAutor())))