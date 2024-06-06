#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 20:26:50 2024

@author: luzmarina
"""

import sys
from PyQt5.QtWidgets import QApplication, QFileDialog, QMenuBar, QAction, QWidget, QVBoxLayout, QLabel, QPushButton, QListWidget, QGridLayout, QTextEdit, QMessageBox, QSizePolicy, QHBoxLayout
from PyQt5.QtCore import Qt

# Modelo de diagnóstico de fallos de coche
class ModeloDiagnosticoCoche:
    def __init__(self):
        # Simulando una lista de fallos con síntomas asociados
        self.fallos = {
            'Batería descargada': ['El coche no arranca', 'Luces tenues', 'Ruidos de clic'],
            'Alternador defectuoso': ['Luces parpadeantes', 'Batería baja', 'El coche se apaga'],
            'Filtro de aire sucio': ['Pérdida de potencia', 'Humo negro', 'Consumo elevado de combustible'],
            'Bujías desgastadas': ['Dificultad para arrancar', 'Fallo del motor', 'Pérdida de potencia']
        }

    def obtener_sintomas(self):
        # Devuelve una lista de todos los síntomas disponibles
        return list(set(sum(self.fallos.values(), [])))

    def realizar_diagnostico(self, sintomas):
        # Realiza un diagnóstico basado en los síntomas proporcionados
        fallos_coincidentes = []
        for fallo, sintomas_fallo in self.fallos.items():
            if all(sintoma in sintomas_fallo for sintoma in sintomas):
                fallos_coincidentes.append(fallo)
        return fallos_coincidentes

    def obtener_descripcion(self, fallo):
        # Devuelve una descripción detallada del fallo
        descripcion = {
            'Batería descargada': 'Una batería descargada puede ser causada por un alternador defectuoso o por dejar las luces encendidas durante mucho tiempo.',
            'Alternador defectuoso': 'Un alternador defectuoso puede hacer que las luces parpadeen, la batería se descargue y, en casos extremos, el coche se apague mientras conduce.',
            'Filtro de aire sucio': 'Un filtro de aire sucio puede causar una pérdida de potencia en el motor, humo negro en el escape y un aumento en el consumo de combustible.',
            'Bujías desgastadas': 'Las bujías desgastadas pueden causar dificultad para arrancar el motor, fallos en el funcionamiento del motor y una pérdida de potencia mientras se conduce.'
        }
        return descripcion.get(fallo, 'Descripción no disponible')

# Vista de diagnóstico de fallos de coche
class VistaDiagnosticoCoche(QWidget):
    def __init__(self, modelo):
        super().__init__()
        self.modelo = modelo
        self.setWindowTitle("Diagnóstico de Fallos de Coche")
        
        # Lista de síntomas seleccionables
        self.label_sintomas_disponibles = QLabel("Fallos Posibles:")
        self.lista_sintomas_disponibles = QListWidget()
        self.lista_sintomas_disponibles.addItems(self.modelo.obtener_sintomas())
        
        # Síntomas seleccionados
        self.label_sintomas_seleccionados = QLabel("Fallos Detectados:")
        self.lista_sintomas_seleccionados = QListWidget()
        
        # Botón para mover síntomas
        self.btn_agregar_sintoma = QPushButton("Agregar Fallo Detectado")
        self.btn_agregar_sintoma.setFixedSize(200, 50)
        self.btn_quitar_sintoma = QPushButton("Quitar Fallo Detectado")
        self.btn_quitar_sintoma.setFixedSize(200, 50)
        self.btn_agregar_sintoma.clicked.connect(self.agregar_sintoma)
        self.btn_quitar_sintoma.clicked.connect(self.quitar_sintoma)
        
        # Botón para diagnosticar
        self.btn_diagnosticar = QPushButton("Diagnosticar")
        self.btn_diagnosticar.clicked.connect(self.realizar_diagnostico)
        
        # Cuadrículas para organizar los widgets
        layout = QGridLayout()
        layout.addWidget(self.label_sintomas_disponibles, 0, 0)
        layout.addWidget(self.lista_sintomas_disponibles, 1, 0)
        layout.addWidget(self.label_sintomas_seleccionados, 0, 1)
        layout.addWidget(self.lista_sintomas_seleccionados, 1, 1)
        
        # Botones para agregar y quitar fallos
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.btn_agregar_sintoma, alignment=Qt.AlignCenter)  # Alinea el botón al centro
        button_layout.addWidget(self.btn_quitar_sintoma, alignment=Qt.AlignCenter)  # Alinea el botón al centro
        layout.addLayout(button_layout, 2, 0, 1, 2)  # Agrega el layout de los botones en la fila 2 y que ocupe las 2 columnas
        
        layout.addWidget(self.btn_diagnosticar, 3, 0, 1, 2)
    
        self.setLayout(layout)
        
        # Horizontal layout for diagnosis, button, and detailed description
        horizontal_layout = QHBoxLayout()
        
        # Cuadrícula para mostrar el diagnóstico
        layout_desc = QVBoxLayout()
        layout_desc.addWidget(QLabel("Diagnóstico:"))
        self.descripcion_diagnostico = QTextEdit()
        self.descripcion_diagnostico.setReadOnly(True)
        layout_desc.addWidget(self.descripcion_diagnostico)
        
        horizontal_layout.addLayout(layout_desc)
        
        # Botón para obtener descripción detallada
        self.btn_obtener_descripcion = QPushButton("Descripción\nMás Detallada\nDel Diagnóstico")
        self.btn_obtener_descripcion.clicked.connect(self.obtener_descripcion_detallada)
        self.btn_obtener_descripcion.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.btn_obtener_descripcion.setFixedSize(200, 100)  # Ajusta el tamaño del botón según sea necesario
        horizontal_layout.addWidget(self.btn_obtener_descripcion)
        
        # Botón para resetear
        self.btn_resetear = QPushButton("Resetear Aplicación")
        self.btn_resetear.clicked.connect(self.resetear)
        self.btn_resetear.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        
        # Alineamos y estiramos el botón de "Resetear" en la esquina derecha
        layout.addWidget(self.btn_resetear, 6, 1, Qt.AlignRight)
        
        # Cuadrícula para mostrar la descripción detallada del fallo
        layout_desc2 = QVBoxLayout()
        layout_desc2.addWidget(QLabel("Descripción del Diagnóstico:"))
        self.descripcion_diagnostico2 = QTextEdit()
        self.descripcion_diagnostico2.setReadOnly(True)
        layout_desc2.addWidget(self.descripcion_diagnostico2)
        
        horizontal_layout.addLayout(layout_desc2)
        
        layout.addLayout(horizontal_layout, 4, 0, 1, 2)
        
        # Ajustar tamaños
        self.descripcion_diagnostico.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.descripcion_diagnostico2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        
        layout.setRowMinimumHeight(2, 55) 
        layout.setRowMinimumHeight(3, 55) 
        
        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 1)
        layout.setRowStretch(1, 1)
        layout.setRowStretch(4, 1)
        
        self.crear_menu()
        self.fallos_coincidentes = []  # Inicializar la lista de fallos coincidentes

    def mostrar(self):
        self.show()
        
    def agregar_sintoma(self):
        item = self.lista_sintomas_disponibles.takeItem(self.lista_sintomas_disponibles.currentRow())
        if item:
            self.lista_sintomas_seleccionados.addItem(item.text())

    def quitar_sintoma(self):
        item = self.lista_sintomas_seleccionados.takeItem(self.lista_sintomas_seleccionados.currentRow())
        if item:
            self.lista_sintomas_disponibles.addItem(item.text())

    def realizar_diagnostico(self):
        sintomas_seleccionados = [self.lista_sintomas_seleccionados.item(i).text() for i in range(self.lista_sintomas_seleccionados.count())]
        self.fallos_coincidentes = self.modelo.realizar_diagnostico(sintomas_seleccionados)
        
        if self.fallos_coincidentes:
            descripcion = "\n".join(self.fallos_coincidentes)
            self.descripcion_diagnostico.setText(descripcion)
        else:
            self.descripcion_diagnostico.setText("No se encontraron fallos coincidentes")

    def obtener_descripcion_detallada(self):
        descripcion = "\n\n".join([self.modelo.obtener_descripcion(fallo) for fallo in self.fallos_coincidentes])
        self.descripcion_diagnostico2.setText(descripcion)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Confirmar Cierre', '¿Estás seguro de que deseas salir?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
            
    def resetear(self):
        # Limpiar la descripción del diagnóstico
        self.descripcion_diagnostico.clear()

        # Limpiar la descripción detallada del diagnóstico
        self.descripcion_diagnostico2.clear()

        # Mover los elementos de la lista de síntomas seleccionados de vuelta a la lista de síntomas disponibles
        for i in range(self.lista_sintomas_seleccionados.count()):
            item = self.lista_sintomas_seleccionados.item(i)
            self.lista_sintomas_disponibles.addItem(item.text())
        
        # Limpiar la lista de síntomas seleccionados
        self.lista_sintomas_seleccionados.clear()
        
        
    def crear_menu(self):
        # Creamos una nueva barra de menú
        menu_bar = QMenuBar()
    
        # Añadimos la barra de menú a la ventana principal
        self.layout().setMenuBar(menu_bar)
    
        # Creamos el menú "Archivo"
        file_menu = menu_bar.addMenu("Archivo")
    
        # Acción para exportar datos
        export_action = QAction("Exportar Datos Diagnóstico", self)
        export_action.triggered.connect(self.exportar_datos)
        file_menu.addAction(export_action)

    def exportar_datos(self):
        # Obtener el contenido de las cuadrículas 2, 3 y 4
        contenido_cuadricula2 = "\n".join([self.lista_sintomas_seleccionados.item(i).text() for i in range(self.lista_sintomas_seleccionados.count())])
        contenido_cuadricula3 = self.descripcion_diagnostico.toPlainText()
        contenido_cuadricula4 = self.descripcion_diagnostico2.toPlainText()
        # Aquí debes agregar el contenido de la cuadrícula 4 si tienes algún contenido relevante
    
        # Abrir un archivo para escribir
        file_path, _ = QFileDialog.getSaveFileName(self, "Guardar archivo", "", "Archivos de texto (*.txt)")
    
        # Escribir el contenido en el archivo
        with open(file_path, "w") as file:
            file.write("Fallos Detectados:\n")
            file.write(contenido_cuadricula2)
            file.write("\n\nDiagnóstico:\n")
            file.write(contenido_cuadricula3)
            file.write("\n\nDescripción del Diagnóstico:\n")
            file.write(contenido_cuadricula4)
            # Aquí debes escribir el contenido de la cuadrícula 4 si tienes algún contenido relevante

# Código principal
if __name__ == "__main__":
    app = QApplication([])
    modelo = ModeloDiagnosticoCoche()
    vista_diagnostico = VistaDiagnosticoCoche(modelo)
    vista_diagnostico.resize(1000, 700)
    vista_diagnostico.mostrar()
    sys.exit(app.exec_())
