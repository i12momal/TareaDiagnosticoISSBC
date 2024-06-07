#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 20:26:50 2024

@author: luzmarina
"""

import sys
from PyQt5.QtWidgets import QApplication, QFileDialog, QMenuBar, QAction, QWidget, QVBoxLayout, QLabel, QPushButton, QListWidget, QGridLayout, QTextEdit, QMessageBox, QSizePolicy, QHBoxLayout, QInputDialog
from PyQt5.QtCore import Qt

# Modelo de diagnóstico de fallos de coche
class ModeloDiagnosticoCoche:
    def __init__(self):
        # Simulando una lista de fallos con síntomas asociados
        self.fallos = {
            'Batería': ['El coche no arranca'],
            'Bujía': ['El coche no arranca', 'Pérdida de potencia'],
            'Motor': ['Sobrecalentamiento de motor', 'Pérdida de potencia', 'Ruidos extraños', 'Emisiones de humo extrañas', 'Consumo elevado de combustible'],
            'Radiador': ['Sobrecalentamiento de motor'],
            'Chasis': ['Vibraciones anormales', 'Ruidos extraños', 'Problemas de dirección'],
            'Filtro de aceite': ['Sobrecalentamiento de motor'],
            'Disco de Frenos': ['Pérdida de frenado', 'Ruidos extraños'],
            'Sistema de Inyección': ['El coche no arranca', 'Pérdida de potencia', 'Consumo elevado de combustible'],
            'Suspensión': ['Vibraciones anormales', 'Problemas de dirección'],
            'Neumáticos': ['Vibraciones anormales', 'Pérdida de frenado', 'Problemas de dirección'],
            'Pastilla de Frenos': ['Pérdida de frenado', 'Ruidos extraños'],
            'Filtro de Aire': ['Pérdida de potencia', 'Emisiones de humo extrañas'],
            'Sistema de Refrigeración': ['Sobrecalentamiento de motor', 'Pérdida de potencia'],
            'Sistema de Escape': ['Pérdida de potencia', 'Ruidos extraños', 'Emisiones de humo extrañas'],
            'Sistema de Transmisión': ['Pérdida de potencia', 'Vibraciones anormales', 'Pérdida de frenado', 'Problemas de dirección']
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
            'Batería': 'La batería suministra la energía eléctrica necesaria para arrancar el coche y alimentar los sistemas eléctricos cuando el motor está apagado y, si falla, el coche no arranca.',
            'Bujía': 'Las bujías generan la chispa que enciende la mezcla de aire y combustible en el motor; su mal funcionamiento puede causar que el coche no arranque y una pérdida notable de potencia.',
            'Motor': 'El motor es la fuente de energía del vehículo, convirtiendo el combustible en movimiento; problemas en este componente pueden causar sobrecalentamiento, pérdida de potencia, ruidos inusuales, emisiones de humo anómalas y un consumo excesivo de combustible.',
            'Radiador': 'El radiador es clave en el sistema de enfriamiento del motor, ayudando a disipar el calor; si falla, el motor puede sobrecalentarse rápidamente.',
            'Chasis': 'El chasis es la estructura base del vehículo que soporta y une todos los componentes; daños en él pueden causar vibraciones anormales, ruidos extraños y problemas de dirección.',
            'Filtro de Aceite': 'El filtro de aceite mantiene el aceite del motor limpio al eliminar impurezas; si está obstruido, puede causar sobrecalentamiento del motor debido a la falta de lubricación adecuada.',
            'Disco de Frenos': 'Los discos de freno, junto con las pastillas, generan la fricción necesaria para detener el vehículo; su desgaste o daño puede provocar una pérdida de eficacia en el frenado y generar ruidos molestos.',
            'Sistema de Inyección': 'El sistema de inyección administra la cantidad exacta de combustible al motor; su mal funcionamiento puede impedir que el coche arranque, reducir la potencia y aumentar el consumo de combustible.',
            'Suspensión': 'La suspensión conecta el vehículo con sus ruedas y absorbe las irregularidades del terreno, proporcionando una conducción suave; fallas en este sistema pueden resultar en vibraciones anormales y problemas de dirección.',
            'Neumáticos': 'Los neumáticos, el único contacto del vehículo con la carretera, proporcionan tracción y estabilidad; su desgaste o daño puede ocasionar vibraciones, pérdida de capacidad de frenado y problemas en la dirección.',
            'Pastilla de Frenos': 'Las pastillas de freno presionan contra los discos para detener el vehículo; el desgaste excesivo de estas puede llevar a una pérdida de eficacia en el frenado y causar ruidos al frenar.',
            'Filtro de Aire': 'El filtro de aire impide la entrada de partículas y polvo al motor, manteniéndolo limpio; si está sucio, puede reducir la potencia del motor y provocar emisiones de humo anómalas.',
            'Sistema de Refrigeración': 'El sistema de refrigeración mantiene la temperatura del motor en un rango óptimo para evitar sobrecalentamientos; un fallo en este sistema puede resultar en sobrecalentamiento y pérdida de potencia del motor.',
            'Sistema de Escape': 'El sistema de escape expulsa los gases residuales del motor, reduciendo el ruido y las emisiones contaminantes; fallos en este sistema pueden causar pérdida de potencia, ruidos inusuales y emisiones de humo anormales.',
            'Sistema de Transmisión': 'El sistema de transmisión transfiere la potencia del motor a las ruedas, permitiendo el movimiento del vehículo; problemas en este sistema pueden causar pérdida de potencia, vibraciones anormales, pérdida de eficacia en el frenado y problemas de dirección.'
        }
        return descripcion.get(fallo, 'Descripción no disponible')

    def comprobar_hipotesis(self, fallo):
        # Comprobaciones de hipótesis para cada componente
        if fallo == 'Neumáticos':
            presion = self.obtener_presion_neumaticos()
            if presion < 2.2:  # Umbral hipotético para la presión de los neumáticos en psi
                return True, "La presión del neumático es baja, indicando un posible fallo."
            else:
                return False, "La presión del neumático es adecuada."
        elif fallo == 'Batería':
            carga = self.obtener_carga_bateria()
            if carga < 12:  # Umbral hipotético para la carga de la batería en voltios
                return True, "La batería está descargada, indicando un posible fallo."
            else:
                return False, "La batería tiene carga suficiente."
        # Se pueden agregar más comprobaciones para otros fallos
        return False, "No hay información disponible para la comprobación de este fallo."

    def obtener_presion_neumaticos(self):
        # Simula la obtención de la presión de los neumáticos
        # En una implementación real, esto podría obtenerse de sensores o de la entrada del usuario
        presion, ok = QInputDialog.getDouble(None, "Comprobación de Hipótesis", "Introduce la presión del neumático (bar):", 0, 0, 100, 1)
        if ok:
            return presion
        return 0

    def obtener_carga_bateria(self):
        # Simula la obtención de la carga de la batería
        # En una implementación real, esto podría obtenerse de sensores o de la entrada del usuario
        carga, ok = QInputDialog.getDouble(None, "Comprobación de Hipótesis", "Introduce la carga de la batería (voltios):", 0, 0, 20, 1)
        if ok:
            return carga
        return 0

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
        
        # Botones para añadir y quitar síntomas
        self.boton_anadir_sintoma = QPushButton("->")
        self.boton_quitar_sintoma = QPushButton("<-")
        
        self.boton_anadir_sintoma.clicked.connect(self.anadir_sintoma)
        self.boton_quitar_sintoma.clicked.connect(self.quitar_sintoma)
        
        # Botón de diagnóstico
        self.boton_diagnostico = QPushButton("Realizar Diagnóstico")
        self.boton_diagnostico.clicked.connect(self.realizar_diagnostico)
        
        # Botón para comprobar hipótesis
        self.boton_comprobar_hipotesis = QPushButton("Comprobar hipótesis sobre componente")
        self.boton_comprobar_hipotesis.clicked.connect(self.comprobar_hipotesis)
        self.boton_comprobar_hipotesis.setEnabled(False)
        
        # Text area para mostrar el diagnóstico
        self.texto_diagnostico = QTextEdit()
        self.texto_diagnostico.setReadOnly(True)
        
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
        
        self.layout_principal = QVBoxLayout()
        self.layout_principal.addLayout(self.layout_sintomas_total)
        self.layout_principal.addWidget(self.boton_diagnostico)
        self.layout_principal.addWidget(self.boton_comprobar_hipotesis)
        self.layout_principal.addWidget(self.texto_diagnostico)
        
        self.setLayout(self.layout_principal)
    
    def anadir_sintoma(self):
        items_seleccionados = self.lista_sintomas_disponibles.selectedItems()
        for item in items_seleccionados:
            self.lista_sintomas_seleccionados.addItem(item.text())
            self.lista_sintomas_disponibles.takeItem(self.lista_sintomas_disponibles.row(item))
    
    def quitar_sintoma(self):
        items_seleccionados = self.lista_sintomas_seleccionados.selectedItems()
        for item in items_seleccionados:
            self.lista_sintomas_disponibles.addItem(item.text())
            self.lista_sintomas_seleccionados.takeItem(self.lista_sintomas_seleccionados.row(item))
    
    def realizar_diagnostico(self):
        if self.lista_sintomas_seleccionados.count() == 0:
            self.texto_diagnostico.setPlainText("No se ha seleccionado ningún fallo.")
            self.boton_comprobar_hipotesis.setEnabled(False)
            return
        
        sintomas_seleccionados = [self.lista_sintomas_seleccionados.item(i).text() for i in range(self.lista_sintomas_seleccionados.count())]
        fallos = self.modelo.realizar_diagnostico(sintomas_seleccionados)

        if fallos:
            texto_diagnostico = "Posibles componentes dañados:\n"
            for fallo in fallos:
                texto_diagnostico += f"+ {fallo}: {self.modelo.obtener_descripcion(fallo)}\n\n"
            texto_diagnostico += "Seleccione un componente para comprobar su estado."
            self.texto_diagnostico.setPlainText(texto_diagnostico)
            self.boton_comprobar_hipotesis.setEnabled(True)
        else:
            self.texto_diagnostico.setPlainText("No se encontraron fallos coincidentes.")
            self.boton_comprobar_hipotesis.setEnabled(False)
    
    def comprobar_hipotesis(self):
        fallo, ok = QInputDialog.getItem(self, "Comprobación de Hipótesis", "Seleccione un componente:", self.modelo.realizar_diagnostico([self.lista_sintomas_seleccionados.item(i).text() for i in range(self.lista_sintomas_seleccionados.count())]), 0, False)
        
        if ok:
            resultado, descripcion = self.modelo.comprobar_hipotesis(fallo)
            if resultado:
                QMessageBox.information(self, "Comprobación de Hipótesis", descripcion)
            else:
                QMessageBox.information(self, "Comprobación de Hipótesis", descripcion)

# Vista principal de la aplicación
class AplicacionDiagnosticoCoche(QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.modelo = ModeloDiagnosticoCoche()
        self.vista_diagnostico_coche = VistaDiagnosticoCoche(self.modelo)
        self.vista_diagnostico_coche.showMaximized()

if __name__ == "__main__":
    app = AplicacionDiagnosticoCoche(sys.argv)
    sys.exit(app.exec_())
