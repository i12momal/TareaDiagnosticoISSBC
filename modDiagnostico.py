#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 17:28:23 2024

@author: joaquin / luzmarina
"""

class ModeloDiagnostico:
    #Constructor de la clase ModeloDiagnostico
    def __init__(self, bcFallos):
    # Inicializa el objeto con una instancia de fallos (bcFallos)
        self.bcFallos = bcFallos

    def obtener_sintomas(self):
        # Devuelve una lista de todos los síntomas disponibles
        # Utiliza set para eliminar duplicados y sum para aplanar la lista de listas
        return list(set(sum(self.bcFallos.fallos.values(), [])))

    # Realiza un diagnóstico basado en los síntomas proporcionados
    def realizar_diagnostico(self, sintomas):
        fallos_coincidentes = [] # Lista para almacenar los fallos que coinciden con los síntomas proporcionados
        # Itera sobre cada fallo y sus síntomas asociados en el diccionario de fallos
        for fallo, sintomas_fallo in self.bcFallos.fallos.items():
            # Verifica si todos los síntomas proporcionados están presentes en los síntomas del fallo actual
            if all(sintoma in sintomas_fallo for sintoma in sintomas):
                fallos_coincidentes.append(fallo) # Si coinciden todos los síntomas, agrega el fallo a la lista de fallos coincidentes
        return fallos_coincidentes # Devuelve la lista de fallos que coinciden con los síntomas proporcionados
