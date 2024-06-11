#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 17:28:23 2024

@author: joaquin / luzmarina
"""

class ModeloDiagnostico:
    def __init__(self, bcFallos):
        self.bcFallos = bcFallos

    def obtener_sintomas(self):
        # Devuelve una lista de todos los síntomas disponibles
        return list(set(sum(self.bcFallos.fallos.values(), [])))

    def realizar_diagnostico(self, sintomas):
        # Realiza un diagnóstico basado en los síntomas proporcionados
        fallos_coincidentes = []
        for fallo, sintomas_fallo in self.bcFallos.fallos.items():
            if all(sintoma in sintomas_fallo for sintoma in sintomas):
                fallos_coincidentes.append(fallo)
        return fallos_coincidentes
