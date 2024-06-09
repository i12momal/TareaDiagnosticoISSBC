#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 17:26:53 2024

@author: joaquin / luzmarina
"""

import sys
from PyQt5.QtWidgets import QApplication
from modDiagnostico import ModeloDiagnosticoCoche
from vistaDiagnostico import VistaDiagnosticoCoche
from ctrlDiagnostico import ControladorDiagnosticoCoche

def main():
    app = QApplication(sys.argv)
    modelo = ModeloDiagnosticoCoche()
    vista = VistaDiagnosticoCoche()
    controlador = ControladorDiagnosticoCoche(modelo, vista)
    vista.showMaximized()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
