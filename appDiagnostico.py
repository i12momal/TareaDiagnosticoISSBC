#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 17:26:53 2024

@author: joaquin / luzmarina
"""

import sys
from PyQt5.QtWidgets import QApplication, QInputDialog
from bcFallosVehiculo import FallosVehiculo
from bcFallosOrdenador import FallosOrdenador
from modDiagnostico import ModeloDiagnostico
from vistaDiagnostico import VistaDiagnostico
from ctrlDiagnostico import ControladorDiagnostico

def main():
    app = QApplication(sys.argv)

    # Define una lista de opciones para el tipo de fallos.
    tipos = ["Coche", "Ordenador"] 

    # Muestra un cuadro de diálogo para que el usuario seleccione el tipo de fallos.
    tipo_fallo, ok = QInputDialog.getItem(None, "Seleccionar tipo de fallos", "Elige el tipo de fallos con los que deseas trabajar:", tipos, 0, False)
   
    # Si el usuario cancela el cuadro de diálogo, finaliza la aplicación.
    if not ok:
        sys.exit()

    # Según la selección del usuario, instancia la clase correspondiente a los fallos del coche o del ordenador.
    if tipo_fallo == "Coche":
        bcFallos = FallosVehiculo()
    else:
        bcFallos = FallosOrdenador()

    # Crea una instancia del modelo de diagnóstico, pasándole la instancia de fallos seleccionada.
    modelo = ModeloDiagnostico(bcFallos)

    # Crea una instancia de la vista del diagnóstico.
    vista = VistaDiagnostico()

    # Crea una instancia del controlador del diagnóstico, pasándole el modelo, la vista y la instancia de fallos.
    controlador = ControladorDiagnostico(modelo, vista, bcFallos)

    # Muestra la vista en pantalla completa.
    vista.showMaximized()

    # Inicia el bucle principal de eventos de la aplicación PyQt.
    sys.exit(app.exec_())

# Si el script se ejecuta directamente (no importado como módulo), llama a la función principal.
if __name__ == "__main__":
    main()
