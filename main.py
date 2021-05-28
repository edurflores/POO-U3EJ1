# -*- coding: utf-8 -*-
"""
Created on Sun May 23 22:20:28 2021

@author: Eduardo
"""

from claseManejaLibros import ManejaLibros

if __name__ == '__main__':
    ml = ManejaLibros()
    ml.CargaLibros()
   # ml.MuestraLibros() #Opcional para ver info de todos los libros.
    print('Menu')
    print('1- Mostrar informacion de libro (Consigna 1).\n2- Buscar palabra (Consigna 2).\n3- Salir.')
    op = int(input('Seleccione opcion:'))
    if op == 1:
        idli = int(input('Ingrese identificador de libro:'))
        ml.MuestraInfo(idli)
    elif op == 2:
        palabra = input('Ingrese palabra a buscar:')
        ml.BuscaPalabra(palabra)
    elif op == 3:
        print('Saliendo del programa.')
    
    