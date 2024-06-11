#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 7 10:10:23 2024

@author: joaquin / luzmarina
"""

from PyQt5.QtWidgets import (QInputDialog)

class FallosOrdenador:
    def __init__(self):
        # Simulando una lista de fallos con síntomas asociados
        self.fallos = {
            'Placa base': ['El sistema no arranca', 'Pantalla azul de la muerte (BSOD)', 'Se apaga inesperadamente', 'Rendimiento lento', 'Errores de conexión'],
            'Memoria RAM': ['El sistema no arranca', 'Rendimiento lento', 'Pantalla azul de la muerte (BSOD)', 'Programas se cierran inesperadamente', 'Sobrecalentamiento', 'Errores de software'],
            'Disco Duro': ['Rendimiento lento', 'Archivos corruptos', 'El sistema no arranca', 'Ruido inusual', 'Programas no responden', 'Se apaga inesperadamente'],
            'Tarjeta Gráfica': ['Pantalla azul de la muerte (BSOD)', 'Problemas con la visualización de gráficos', 'Se apaga inesperadamente', 'Rendimiento lento', 'El sistema no arranca'],
            'Fuente de Alimentación': ['El sistema no arranca', 'Se apaga inesperadamente', 'Ruidos extraños', 'Sobrecalentamiento', 'Rendimiento lento'],
            'Sistema Operativo': ['Rendimiento lento', 'Errores de software', 'Programas no responden', 'Pantalla azul de la muerte (BSOD)', 'Archivos corruptos', 'Errores de conexión'],
            'Sistema de Refrigeración': ['Sobrecalentamiento', 'Se apaga inesperadamente', 'Ruido inusual', 'Rendimiento lento', 'El sistema no arranca'],
            'Periféricos': ['El dispositivo no se reconoce', 'Errores de conexión', 'Problemas de rendimiento', 'Programas no responden', 'Rendimiento lento']
        }


    def obtener_descripcion(self, fallo):
        # Devuelve una descripción detallada del fallo
        descripcion = {
            'Placa base': 'La placa base es el principal circuito de una computadora que conecta y permite la comunicación entre todos los componentes. Si falla, puede impedir que el sistema arranque o causar inestabilidad general.',
            'Memoria RAM': 'La memoria RAM almacena datos temporales que el sistema utiliza para procesar tareas. Fallos en la RAM pueden causar que el sistema no arranque, se ralentice, muestre errores como la pantalla azul de la muerte, o que los programas se cierren inesperadamente.',
            'Disco Duro': 'El disco duro es donde se almacenan los datos permanentemente. Problemas con el disco duro pueden resultar en rendimiento lento, archivos corruptos, fallos de arranque y ruidos inusuales indicando posibles fallos mecánicos.',
            'Tarjeta Gráfica': 'La tarjeta gráfica maneja la representación visual de datos. Problemas en este componente pueden causar la pantalla azul de la muerte, fallos en la visualización de gráficos y apagados inesperados debido al sobrecalentamiento.',
            'Fuente de Alimentación': 'La fuente de alimentación convierte la corriente alterna de la red eléctrica en corriente continua para los componentes de la computadora. Si falla, el sistema puede no arrancar, apagarse inesperadamente o generar ruidos inusuales.',
            'Sistema Operativo': 'El sistema operativo gestiona los recursos del hardware y el software. Problemas con el sistema operativo pueden causar un rendimiento lento, errores de software, falta de respuesta de los programas y la pantalla azul de la muerte.',
            'Sistema de Refrigeración': 'El sistema de refrigeración mantiene la temperatura adecuada para los componentes. Un fallo en este sistema puede provocar sobrecalentamiento, apagados inesperados y ruidos inusuales debidos a los ventiladores o a la falta de mantenimiento.',
            'Periféricos': 'Los periféricos son dispositivos externos como teclados, ratones y impresoras. Problemas con estos pueden causar que no sean reconocidos por el sistema, errores de conexión y problemas de rendimiento al intentar utilizarlos.'
        }
        return descripcion.get(fallo, 'Descripción no disponible')

    def comprobar_hipotesis(self, fallo):
        if fallo == 'Placa base':
            voltaje = self.obtener_voltaje_placa_base()
            if voltaje < 1.1 or voltaje > 1.3:
                return True, "El voltaje de la placa base está fuera del rango normal, indicando un posible fallo en la placa base."
            else:
                return False, "El voltaje de la placa base es adecuado."

        elif fallo == 'Memoria RAM':
            latencia = self.obtener_latencia_memoria()
            if latencia < 10 or latencia > 20:
                return True, "La latencia de la memoria RAM está fuera del rango normal, indicando un posible fallo en la memoria."
            else:
                return False, "La latencia de la memoria RAM es adecuada."

        elif fallo == 'Disco Duro':
            temperatura = self.obtener_temperatura_disco_duro()
            espacio_libre = self.obtener_espacio_libre_disco()
            if temperatura > 50 or espacio_libre < 10:
                return True, "La temperatura del disco duro es alta o el espacio libre es muy bajo, indicando un posible fallo en el disco duro."
            else:
                return False, "La temperatura y el espacio libre del disco duro son adecuados."

        elif fallo == 'Tarjeta Gráfica':
            temperatura = self.obtener_temperatura_tarjeta_grafica()
            fps = self.obtener_fps_juego()
            if temperatura > 80 or fps < 30:
                return True, "La temperatura de la tarjeta gráfica es alta o los FPS son bajos, indicando un posible fallo en la tarjeta gráfica."
            else:
                return False, "La temperatura y el rendimiento de la tarjeta gráfica son adecuados."

        elif fallo == 'Fuente de Alimentación':
            voltaje_salida = self.obtener_voltaje_salida_fuente()
            ruido_fuente = self.obtener_ruido_fuente()
            if voltaje_salida < 11 or voltaje_salida > 13 or ruido_fuente > 50:
                return True, "El voltaje de salida o el ruido de la fuente de alimentación están fuera del rango normal, indicando un posible fallo."
            else:
                return False, "El voltaje de salida y el ruido de la fuente de alimentación son adecuados."

        elif fallo == 'Sistema Operativo':
            tiempo_respuesta = self.obtener_tiempo_respuesta_so()
            errores_registro = self.obtener_errores_registro_so()
            if tiempo_respuesta > 2 or errores_registro > 5:
                return True, "El tiempo de respuesta del sistema operativo es alto o hay muchos errores en el registro, indicando posibles problemas con el sistema operativo."
            else:
                return False, "El tiempo de respuesta y la cantidad de errores del sistema operativo son adecuados."

        elif fallo == 'Sistema de Refrigeración':
            temperatura_cpu = self.obtener_temperatura_cpu()
            velocidad_ventilador = self.obtener_velocidad_ventilador()
            if temperatura_cpu > 70 or velocidad_ventilador > 3000:
                return True, "La temperatura de la CPU es alta o la velocidad del ventilador es excesiva, indicando un posible fallo en el sistema de refrigeración."
            else:
                return False, "La temperatura de la CPU y la velocidad del ventilador son adecuadas."

        elif fallo == 'Periféricos':
            conexion = self.obtener_estado_conexion_periferico()
            if conexion != 'estable':
                return True, "La conexión del periférico no es estable, indicando un posible fallo."
            else:
                return False, "La conexión del periférico es adecuada."

        return False, "No hay información disponible para la comprobación de este fallo."

    # Métodos para obtener valores simulados
    def obtener_voltaje_placa_base(self):
        voltaje, ok = QInputDialog.getDouble(None, "Comprobación de Hipótesis", "Introduce el voltaje de la placa base (V):", 1.2, 0, 2, 1)
        if ok:
            return voltaje
        return 0

    def obtener_latencia_memoria(self):
        latencia, ok = QInputDialog.getDouble(None, "Comprobación de Hipótesis", "Introduce la latencia de la memoria (ns):", 15, 0, 30, 1)
        if ok:
            return latencia
        return 0

    def obtener_temperatura_disco_duro(self):
        temperatura, ok = QInputDialog.getDouble(None, "Comprobación de Hipótesis", "Introduce la temperatura del disco duro (°C):", 40, 0, 100, 1)
        if ok:
            return temperatura
        return 0

    def obtener_espacio_libre_disco(self):
        espacio, ok = QInputDialog.getDouble(None, "Comprobación de Hipótesis", "Introduce el espacio libre en el disco duro (GB):", 20, 0, 1000, 1)
        if ok:
            return espacio
        return 0

    def obtener_temperatura_tarjeta_grafica(self):
        temperatura, ok = QInputDialog.getDouble(None, "Comprobación de Hipótesis", "Introduce la temperatura de la tarjeta gráfica (°C):", 70, 0, 100, 1)
        if ok:
            return temperatura
        return 0

    def obtener_fps_juego(self):
        fps, ok = QInputDialog.getDouble(None, "Comprobación de Hipótesis", "Introduce los FPS en un juego (fps):", 60, 0, 240, 1)
        if ok:
            return fps
        return 0

    def obtener_voltaje_salida_fuente(self):
        voltaje, ok = QInputDialog.getDouble(None, "Comprobación de Hipótesis", "Introduce el voltaje de salida de la fuente de alimentación (V):", 12, 0, 20, 1)
        if ok:
            return voltaje
        return 0

    def obtener_ruido_fuente(self):
        ruido, ok = QInputDialog.getDouble(None, "Comprobación de Hipótesis", "Introduce el nivel de ruido de la fuente de alimentación (dB):", 30, 0, 100, 1)
        if ok:
            return ruido
        return 0

    def obtener_tiempo_respuesta_so(self):
        tiempo, ok = QInputDialog.getDouble(None, "Comprobación de Hipótesis", "Introduce el tiempo de respuesta del sistema operativo (s):", 1, 0, 10, 1)
        if ok:
            return tiempo
        return 0

    def obtener_errores_registro_so(self):
        errores, ok = QInputDialog.getInt(None, "Comprobación de Hipótesis", "Introduce el número de errores en el registro del sistema operativo:", 0, 0, 100, 1)
        if ok:
            return errores
        return 0

    def obtener_temperatura_cpu(self):
        temperatura, ok = QInputDialog.getDouble(None, "Comprobación de Hipótesis", "Introduce la temperatura de la CPU (°C):", 60, 0, 100, 1)
        if ok:
            return temperatura
        return 0

    def obtener_velocidad_ventilador(self):
        velocidad, ok = QInputDialog.getInt(None, "Comprobación de Hipótesis", "Introduce la velocidad del ventilador (RPM):", 2000, 0, 6000, 1)
        if ok:
            return velocidad
        return 0

    def obtener_estado_conexion_periferico(self):
        estados = ["estable", "inestable"]
        estado, ok = QInputDialog.getItem(None, "Comprobación de Hipótesis", "Selecciona el estado de la conexión del periférico:", estados, 0, False)
        if ok:
            return estado
        return 0