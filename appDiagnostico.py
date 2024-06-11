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
    tipos = ["Coche", "Ordenador"]
    tipo_fallo, ok = QInputDialog.getItem(None, "Seleccionar tipo de fallos", "Elige el tipo de fallos con los que deseas trabajar:", tipos, 0, False)
    if not ok:
        sys.exit()
    if tipo_fallo == "Coche":
        bcFallos = FallosVehiculo()
    else:
        bcFallos = FallosOrdenador()
    modelo = ModeloDiagnostico(bcFallos)
    vista = VistaDiagnostico()
    controlador = ControladorDiagnostico(modelo, vista, bcFallos)
    vista.showMaximized()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
