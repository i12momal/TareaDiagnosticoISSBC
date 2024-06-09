#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 17:24:32 2024

@author: joaquin / luzmarina
"""

from PyQt5.QtWidgets import (QInputDialog, QMessageBox, QFileDialog)

class ControladorDiagnosticoCoche:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

        # Conectar señales y slots
        self.vista.boton_anadir_sintoma.clicked.connect(self.anadir_sintoma)
        self.vista.boton_quitar_sintoma.clicked.connect(self.quitar_sintoma)
        self.vista.boton_diagnostico.clicked.connect(self.realizar_diagnostico)
        self.vista.boton_comprobar_hipotesis.clicked.connect(self.comprobar_hipotesis)
        self.vista.lista_sintomas_disponibles.addItems(self.modelo.obtener_sintomas())
        self.vista.accion_nuevo_diagnostico.triggered.connect(self.nuevo_diagnostico)
        self.vista.accion_guardar_diagnostico.triggered.connect(self.guardar_diagnostico)

    def anadir_sintoma(self):
        items_seleccionados = self.vista.lista_sintomas_disponibles.selectedItems()
        for item in items_seleccionados:
            self.vista.lista_sintomas_seleccionados.addItem(item.text())
            self.vista.lista_sintomas_disponibles.takeItem(self.vista.lista_sintomas_disponibles.row(item))
    
    def quitar_sintoma(self):
        items_seleccionados = self.vista.lista_sintomas_seleccionados.selectedItems()
        for item in items_seleccionados:
            self.vista.lista_sintomas_disponibles.addItem(item.text())
            self.vista.lista_sintomas_seleccionados.takeItem(self.vista.lista_sintomas_seleccionados.row(item))
    
    def realizar_diagnostico(self):
        if self.vista.lista_sintomas_seleccionados.count() == 0:
            self.vista.texto_diagnostico.setPlainText("No se ha seleccionado ningún síntoma.")
            self.vista.texto_hipotesis.clear()
            self.vista.boton_comprobar_hipotesis.setEnabled(False)
            return

        sintomas_seleccionados = [self.vista.lista_sintomas_seleccionados.item(i).text() for i in range(self.vista.lista_sintomas_seleccionados.count())]
        fallos_coincidentes = []

        # Buscar si alguno de los síntomas seleccionados coincide con alguno de los síntomas asociados a cada componente
        for fallo, sintomas_fallo in self.modelo.fallos.items():
            for sintoma in sintomas_seleccionados:
                if sintoma in sintomas_fallo:
                    fallos_coincidentes.append(fallo)
                    break  # Si se encuentra al menos un síntoma asociado al fallo, se agrega el fallo y se sale del bucle interno

        if fallos_coincidentes:
            texto_diagnostico = "Posibles componentes dañados:\n"
            for fallo in fallos_coincidentes:
                descripcion_componente = self.modelo.obtener_descripcion(fallo)
                fallos_asociados = [f for f in self.modelo.fallos[fallo] if f in sintomas_seleccionados]
                if fallos_asociados:
                    texto_diagnostico += f"+ {fallo}: {descripcion_componente}\n"
                    texto_diagnostico += f"[Fallos asociados: {', '.join(fallos_asociados)}]\n\n"
            self.vista.texto_diagnostico.setPlainText(texto_diagnostico)
            self.vista.componentes_a_comprobar = fallos_coincidentes
            self.vista.boton_comprobar_hipotesis.setEnabled(True)
        else:
            self.vista.texto_diagnostico.setPlainText("No se encontraron fallos coincidentes.")
            self.vista.boton_comprobar_hipotesis.setEnabled(False)

        self.vista.texto_hipotesis.clear()
 
    def comprobar_hipotesis(self):
        fallo_seleccionado, ok = QInputDialog.getItem(self.vista, "Comprobación de Hipótesis", "Seleccione un componente:", self.vista.componentes_a_comprobar, 0, False)
        
        if ok:
            resultado, descripcion = self.modelo.comprobar_hipotesis(fallo_seleccionado)
            if resultado:
                QMessageBox.information(self,vista, "Comprobación de Hipótesis", descripcion)
            else:
                QMessageBox.information(self.vista, "Comprobación de Hipótesis", descripcion)
            
            # Eliminar el componente comprobado de la lista
            self.vista.componentes_a_comprobar.remove(fallo_seleccionado)
            
            # Mostrar el resultado en el cuadro de texto_hipotesis
            texto_actual = self.vista.texto_hipotesis.toPlainText()
            texto_actual += f"- Comprobación de hipótesis, componente {fallo_seleccionado}\nResultado del análisis: {descripcion}\n\n"
            self.vista.texto_hipotesis.setPlainText(texto_actual)

    def nuevo_diagnostico(self):
        # Limpiar las listas de síntomas seleccionados y el diagnóstico
        self.vista.lista_sintomas_disponibles.clear()
        self.vista.lista_sintomas_seleccionados.clear()
        self.vista.texto_diagnostico.clear()
        self.vista.texto_hipotesis.clear()
        self.vista.input2.clear()
        self.vista.boton_comprobar_hipotesis.setEnabled(False)
        # Re-poblar la lista de síntomas disponibles
        self.vista.lista_sintomas_disponibles.addItems(self.modelo.obtener_sintomas())

    def guardar_diagnostico(self):
        contenido_input2 = self.vista.input2.text()
        if self.vista.lista_sintomas_seleccionados.count() == 0 or not self.vista.texto_diagnostico.toPlainText():
            QMessageBox.warning(self.vista, "Guardar Diagnóstico", "No hay diagnóstico para guardar.")
            return
        
        opciones = QFileDialog.Options()
        archivo, _ = QFileDialog.getSaveFileName(self.vista, "Guardar Diagnóstico", "", "Archivos de Texto (*.txt)", options=opciones)
        if archivo:
            with open(archivo, 'w') as file:
                file.write("FALLOS DETECTADOS:\n")
                for i in range(self.vista.lista_sintomas_seleccionados.count()):
                    file.write(f"- {self.vista.lista_sintomas_seleccionados.item(i).text()}\n")
                file.write("\nDESCRIPCIÓN DEL DIAGNÓSTICO:\n")
                file.write(self.vista.texto_diagnostico.toPlainText())
                file.write("\nCOMPROBACIÓN DE LAS HIPÓTESIS:\n")
                file.write(self.vista.texto_hipotesis.toPlainText())
                file.write("\nHIPÓTESIS FINAL:\n")
                file.write(contenido_input2)
