#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 17:28:23 2024

@author: joaquin / luzmarina
"""

from PyQt5.QtWidgets import (QInputDialog)

class ModeloDiagnosticoCoche:
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

    def comprobar_hipotesis(self, fallo):
        if fallo == 'Batería':
            carga_parado = self.obtener_carga_bateria("parado")
            carga_marcha = self.obtener_carga_bateria("en marcha")
            if carga_parado < 12.4 or carga_marcha < 13.7:
                return True, "La batería está descargada o no se está cargando correctamente, el componente se encuentra averiado."
            else:
                return False, "La batería tiene carga suficiente en ambos estados."

        elif fallo == 'Neumáticos':
            presion = self.obtener_presion_neumaticos()
            if presion < 30:
                return True, "La presión del neumático es baja, el componente se encuentra averiado."
            else:
                return False, "La presión del neumático es adecuada."

        elif fallo == 'Bujía':
            resistencia = self.obtener_resistencia_bujia()
            if resistencia < 4 or resistencia > 8:
                return True, "La resistencia de la bujía está fuera de los límites normales, el componente se encuentra averiado."
            else:
                return False, "La resistencia de la bujía es adecuada."

        elif fallo == 'Motor':
            compresion = self.obtener_compresion_motor()
            temperatura = self.obtener_temperatura_motor()
            presion_aceite = self.obtener_presion_aceite_motor()
            if compresion < 120 or compresion > 160 or temperatura < 85 or temperatura > 105 or presion_aceite < 20 or presion_aceite > 60:
                return True, "Uno o más valores del motor están fuera del rango normal, el componente se encuentra averiado."
            else:
                return False, "Los valores del motor son adecuados."

        elif fallo == 'Radiador':
            temperatura = self.obtener_temperatura_radiador()
            presion = self.obtener_presion_radiador()
            if temperatura < 85 or temperatura > 95 or presion < 13 or presion > 16:
                return True, "La temperatura o presión del radiador está fuera del rango óptimo, el componente se encuentra averiado."
            else:
                return False, "La temperatura y presión del radiador son adecuadas."

        elif fallo == 'Chasis':
            desviacion = self.obtener_desviacion_chasis()
            if desviacion > 3:
                return True, "La desviación del chasis es significativa, el componente se encuentra averiado."
            else:
                return False, "La desviación del chasis es mínima y aceptable."

        elif fallo == 'Filtro de Aceite':
            presion = self.obtener_presion_aceite()
            if presion < 20 or presion > 60:
                return True, "La presión de aceite está fuera del rango normal, el componente se encuentra averiado."
            else:
                return False, "La presión de aceite es adecuada."

        elif fallo == 'Disco de Frenos':
            grosor = self.obtener_grosor_disco_frenos()
            if grosor < 22:
                return True, "El grosor del disco de frenos está por debajo del mínimo, el componente se encuentra averiado."
            else:
                return False, "El grosor del disco de frenos es adecuado."

        elif fallo == 'Sistema de Inyección':
            presion_combustible = self.obtener_presion_combustible()
            if presion_combustible < 40 or presion_combustible > 60:
                return True, "La presión de combustible está fuera del rango normal, el componente se encuentra averiado."
            else:
                return False, "La presión de combustible es adecuada."

        elif fallo == 'Suspensión':
            altura = self.obtener_altura_suspension()
            if altura < 15 or altura > 20:
                return True, "La altura de la suspensión está fuera del rango aceptable, el componente se encuentra averiado."
            else:
                return False, "La altura de la suspensión es adecuada."

        elif fallo == 'Pastilla de Frenos':
            grosor_pastilla = self.obtener_grosor_pastilla_frenos()
            if grosor_pastilla < 3:
                return True, "El grosor de la pastilla de frenos está por debajo del mínimo, el componente se encuentra averiado."
            else:
                return False, "El grosor de la pastilla de frenos es adecuado."

        elif fallo == 'Filtro de Aire':
            resistencia_aire = self.obtener_resistencia_aire()
            if resistencia_aire > 2.5:
                return True, "La resistencia al flujo de aire es demasiado alta, indicando un posible fallo en el filtro de aire."
            else:
                return False, "La resistencia al flujo de aire es adecuada."

        elif fallo == 'Sistema de Refrigeración':
            presion_refrigerante = self.obtener_presion_refrigerante()
            if presion_refrigerante < 13 or presion_refrigerante > 16:
                return True, "La presión del sistema de refrigeración está fuera del rango normal, el componente se encuentra averiado."
            else:
                return False, "La presión del sistema de refrigeración es adecuada."

        elif fallo == 'Sistema de Escape':
            emisiones_CO = self.obtener_emisiones_CO()
            if emisiones_CO > 0.5:
                return True, "Las emisiones de monóxido de carbono son demasiado altas, indicando un posible fallo en el sistema de escape."
            else:
                return False, "Las emisiones de monóxido de carbono son adecuadas."

        elif fallo == 'Sistema de Transmisión':
            presion_transmision = self.obtener_presion_transmision()
            if presion_transmision < 70 or presion_transmision > 120:
                return True, "La presión del sistema de transmisión está fuera del rango normal, el componente se encuentra averiado."
            else:
                return False, "La presión del sistema de transmisión es adecuada."

        return False, "No hay información disponible para la comprobación de este fallo."

    # Métodos para obtener valores simulados
    def obtener_presion_neumaticos(self):
        presion, ok = QInputDialog.getDouble(None, "Comprobación de Hipótesis", "Introduce la presión del neumático (psi):", 2.5, 0, 10, 1)
        if ok:
            return presion
        return 0

    def obtener_carga_bateria(self, estado):
        mensaje = f"Introduce la carga de la batería (voltios) ({estado}):"
        carga, ok = QInputDialog.getDouble(None, "Comprobación de Hipótesis", mensaje, 12, 0, 20, 1)
        if ok:
            return carga
        return 0

    def obtener_resistencia_bujia(self):
        resistencia, ok = QInputDialog.getDouble(None, "Comprobación de Hipótesis", "Introduce la resistencia de la bujía (ohmios):", 5, 0, 20, 1)
        if ok:
            return resistencia
        return 0

    def obtener_compresion_motor(self):
        compresion, ok = QInputDialog.getDouble(None, "Comprobación de Hipótesis", "Introduce la compresión del motor (psi):", 130, 0, 200, 1)
        if ok:
            return compresion
        return 0

    def obtener_temperatura_motor(self):
        temperatura, ok = QInputDialog.getDouble(None, "Comprobación de Hipótesis", "Introduce la temperatura del motor (°C):", 90, 0, 150, 1)
        if ok:
            return temperatura
        return 0

    def obtener_presion_aceite_motor(self):
        presion, ok = QInputDialog.getDouble(None, "Comprobación de Hipótesis", "Introduce la presión del aceite del motor (psi):", 30, 0, 100, 1)
        if ok:
            return presion
        return 0

    def obtener_temperatura_radiador(self):
        temperatura, ok = QInputDialog.getDouble(None, "Comprobación de Hipótesis", "Introduce la temperatura del radiador (°C):", 90, 0, 150, 1)
        if ok:
            return temperatura
        return 0

    def obtener_presion_radiador(self):
        presion, ok = QInputDialog.getDouble(None, "Comprobación de Hipótesis", "Introduce la presión del radiador (psi):", 15, 0, 30, 1)
        if ok:
            return presion
        return 0

    def obtener_desviacion_chasis(self):
        desviacion, ok = QInputDialog.getDouble(None, "Comprobación de Hipótesis", "Introduce la desviación del chasis (mm):", 0, 0, 10, 1)
        if ok:
            return desviacion
        return 0

    def obtener_presion_aceite(self):
        presion, ok = QInputDialog.getDouble(None, "Comprobación de Hipótesis", "Introduce la presión del aceite (psi):", 40, 0, 100, 1)
        if ok:
            return presion
        return 0

    def obtener_grosor_disco_frenos(self):
        grosor, ok = QInputDialog.getDouble(None, "Comprobación de Hipótesis", "Introduce el grosor del disco de frenos (mm):", 25, 0, 50, 1)
        if ok:
            return grosor
        return 0

    def obtener_presion_combustible(self):
        presion, ok = QInputDialog.getDouble(None, "Comprobación de Hipótesis", "Introduce la presión de combustible (psi):", 50, 0, 100, 1)
        if ok:
            return presion
        return 0

    def obtener_altura_suspension(self):
        altura, ok = QInputDialog.getDouble(None, "Comprobación de Hipótesis", "Introduce la altura de la suspensión (cm):", 18, 0, 30, 1)
        if ok:
            return altura
        return 0

    def obtener_grosor_pastilla_frenos(self):
        grosor, ok = QInputDialog.getDouble(None, "Comprobación de Hipótesis", "Introduce el grosor de la pastilla de frenos (mm):", 10, 0, 20, 1)
        if ok:
            return grosor
        return 0

    def obtener_resistencia_aire(self):
        resistencia, ok = QInputDialog.getDouble(None, "Comprobación de Hipótesis", "Introduce la resistencia del flujo de aire (pulgadas de H2O):", 1, 0, 10, 1)
        if ok:
            return resistencia
        return 0

    def obtener_presion_refrigerante(self):
        presion, ok = QInputDialog.getDouble(None, "Comprobación de Hipótesis", "Introduce la presión del refrigerante (psi):", 14, 0, 30, 1)
        if ok:
            return presion
        return 0

    def obtener_emisiones_CO(self):
        emisiones, ok = QInputDialog.getDouble(None, "Comprobación de Hipótesis", "Introduce las emisiones de CO (%):", 0.1, 0, 10, 1)
        if ok:
            return emisiones
        return 0

    def obtener_presion_transmision(self):
        presion, ok = QInputDialog.getDouble(None, "Comprobación de Hipótesis", "Introduce la presión de la transmisión (psi):", 100, 0, 200, 1)
        if ok:
            return presion
        return 0