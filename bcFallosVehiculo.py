#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 16:28:35 2024

@author: joaquin
"""

class Fallo():
    def __init__(self,nombre=None,tipo=None,valoresPermitidos=None,valor=None):
        #print 'Fallo->',valor
        self.nombre=nombre
        self.valor=valor
        self.tipo=tipo
        self.valoresPermitidos=valoresPermitidos

class ProblemaArranque(Fallo):
    def __init__(self,valor=None)
    nombre='Problema al arrancar'
    tipo='Booleano'
    valoresPermitidos=None
    Fallo.__init__(self,nombre ,tipo ,valoresPermitidos,valor)
    self.valor=valor

class SobrecalentamientoMotor(Fallo):
    def __init__(self,valor=None)
    nombre='Sobrecalentamiento del motor'
    tipo='Multiple'
    valoresPermitidos=[bajo,medio,alto]
    Fallo.__init__(self,nombre ,tipo ,valoresPermitidos,valor)
    self.valor=valor

def mostrarFallos():
    fallos=[]
    fallos.append(ProblemaArranque())
    fallos.append(SobrecalentamientoMotor())
    
    return fallos