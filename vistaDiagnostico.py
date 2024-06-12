#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 17:25:44 2024

@author: joaquin / luzmarina
"""

from PyQt5.QtWidgets import (QApplication, QLineEdit, QFileDialog, QMenuBar, QAction, QMainWindow, QVBoxLayout,QLabel, QPushButton,
                            QListWidget, QGridLayout, QTextEdit, QMessageBox, QSizePolicy, QHBoxLayout, QInputDialog, QWidget)
from PyQt5.QtCore import Qt

class VistaDiagnostico(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Diagnóstico de Fallos de Coche")
        self.componentes_a_comprobar = []  
        
        # Crear barra de menú
        self.menu_bar = QMenuBar(self)
        self.menu_archivo = self.menu_bar.addMenu("Archivo")

        self.accion_nuevo_diagnostico = QAction("Nuevo Diagnóstico", self)
        self.accion_guardar_diagnostico = QAction("Guardar Diagnóstico", self)
        self.menu_archivo.addAction(self.accion_nuevo_diagnostico)
        self.menu_archivo.addAction(self.accion_guardar_diagnostico)
        
        # Lista de síntomas seleccionables
        self.label_sintomas_disponibles = QLabel("Fallos Disponibles:")
        self.lista_sintomas_disponibles = QListWidget()
        
        # Síntomas seleccionados
        self.label_sintomas_seleccionados = QLabel("Fallos Seleccionados:")
        self.lista_sintomas_seleccionados = QListWidget()

        # Etiqueta para mostrar el resultado del diagnóstico
        self.label_resultado_diagnostico = QLabel("Resultado Diagnostico:")
        # Etiqueta para mostrar la comprobación de hipótesis
        self.label_comprobacion_hipotesis = QLabel("Comprobación hipótesis:")
        
        # Botones para añadir y quitar síntomas
        self.boton_anadir_sintoma = QPushButton("->")
        self.boton_quitar_sintoma = QPushButton("<-")
        
        # Botón de diagnóstico
        self.boton_diagnostico = QPushButton("Realizar Diagnóstico")
        
        # Botón para comprobar hipótesis
        self.boton_comprobar_hipotesis = QPushButton("Comprobar hipótesis sobre componente")
        self.boton_comprobar_hipotesis.setEnabled(False)
        
        # Text area para mostrar el diagnóstico
        self.texto_diagnostico = QTextEdit()
        self.texto_diagnostico.setReadOnly(True)

        # Listas y text area para mostrar las hipotesis
        self.texto_hipotesis = QTextEdit()
        self.texto_hipotesis.setReadOnly(True)

        #Hipotesis final
        self.label = QLabel('Hipótesis final:', self)
        self.input1 = QLineEdit(self)
        self.input2 = QLineEdit(self)
        self.input2.setReadOnly(True)
        
        # Botón Guardar
        self.boton_guardar = QPushButton('Guardar Hipótesis', self)
        self.boton_guardar.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.boton_guardar.clicked.connect(self.saveText)
        
        # Botón Eliminar
        self.boton_borrar = QPushButton('Eliminar Hipótesis', self)
        self.boton_borrar.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.boton_borrar.clicked.connect(self.deleteText)

        # Layouts
        self.layout_sintomas = QVBoxLayout()
        self.layout_sintomas.addWidget(self.label_sintomas_disponibles)
        self.layout_sintomas.addWidget(self.lista_sintomas_disponibles)
        
        self.layout_sintomas_seleccionados = QVBoxLayout()
        self.layout_sintomas_seleccionados.addWidget(self.label_sintomas_seleccionados)
        self.layout_sintomas_seleccionados.addWidget(self.lista_sintomas_seleccionados)
        
        self.layout_botones = QVBoxLayout()
        self.layout_botones.addWidget(self.boton_anadir_sintoma)
        self.layout_botones.addWidget(self.boton_quitar_sintoma)
        
        self.layout_sintomas_total = QHBoxLayout()
        self.layout_sintomas_total.addLayout(self.layout_sintomas)
        self.layout_sintomas_total.addLayout(self.layout_botones)
        self.layout_sintomas_total.addLayout(self.layout_sintomas_seleccionados)

        #Hipotesis final
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.input1)
        self.vbox.addWidget(self.input2)
        
        # Layout horizontal para los botones Guardar y Eliminar
        self.hbox_buttons = QHBoxLayout()
        self.hbox_buttons.addStretch(1)  # Añadir espacio flexible para empujar los botones a la derecha
        self.hbox_buttons.addWidget(self.boton_guardar)
        self.hbox_buttons.addWidget(self.boton_borrar)
        self.vbox.addLayout(self.hbox_buttons)

        # Layouts para Diagnóstico e Hipótesis
        self.layout_diagnostico_hipotesis = QHBoxLayout()

        # Layout para Diagnóstico
        layout_diagnostico = QVBoxLayout()
        layout_diagnostico.addWidget(QLabel('Resultado del Diagnóstico:'))
        layout_diagnostico.addWidget(self.texto_diagnostico)

        # Layout para Hipótesis
        layout_hipotesis = QVBoxLayout()
        layout_hipotesis.addWidget(QLabel('Comprobación de las Hipótesis:'))
        layout_hipotesis.addWidget(self.texto_hipotesis)

        # Añadir ambos layouts al layout horizontal
        self.layout_diagnostico_hipotesis.addLayout(layout_diagnostico)
        self.layout_diagnostico_hipotesis.addLayout(layout_hipotesis)
        
        self.layout_principal = QVBoxLayout()
        self.layout_principal.addWidget(self.menu_bar)
        self.layout_principal.addLayout(self.layout_sintomas_total)
        self.layout_principal.addWidget(self.boton_diagnostico)
        self.layout_principal.addWidget(self.boton_comprobar_hipotesis)
        self.layout_principal.addLayout(self.layout_diagnostico_hipotesis)
        self.layout_principal.addLayout(self.vbox)
        
        self.setLayout(self.layout_principal)

    #Agrega el texto del input1 al input2 separado por una nueva línea y luego limpia input1
    def saveText(self):
        text = self.input2.text()
        text += f"\n"
        text += self.input1.text()
        self.input2.setText(text)
        self.input1.clear()

    #Limpia tanto input1 como input2
    def deleteText(self):
        self.input1.clear()
        self.input2.clear()