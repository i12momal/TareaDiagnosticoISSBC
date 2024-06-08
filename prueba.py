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

# Vista de diagnóstico de fallos de coche
class VistaDiagnosticoCoche(QWidget):
    def __init__(self, modelo):
        super().__init__()
        self.modelo = modelo
        self.setWindowTitle("Diagnóstico de Fallos de Coche")
        self.componentes_a_comprobar = []  # Lista para mantener los componentes que se pueden comprobar
        
        # Crear barra de menú
        self.menu_bar = QMenuBar(self)
        self.menu_archivo = self.menu_bar.addMenu("Archivo")

        self.accion_nuevo_diagnostico = QAction("Nuevo Diagnóstico", self)
        self.accion_guardar_diagnostico = QAction("Guardar Diagnóstico", self)
        self.menu_archivo.addAction(self.accion_nuevo_diagnostico)
        self.menu_archivo.addAction(self.accion_guardar_diagnostico)

        self.accion_nuevo_diagnostico.triggered.connect(self.nuevo_diagnostico)
        self.accion_guardar_diagnostico.triggered.connect(self.guardar_diagnostico)
        
        # Lista de síntomas seleccionables
        self.label_sintomas_disponibles = QLabel("Fallos Disponibles:")
        self.lista_sintomas_disponibles = QListWidget()
        self.lista_sintomas_disponibles.addItems(self.modelo.obtener_sintomas())
        
        # Síntomas seleccionados
        self.label_sintomas_seleccionados = QLabel("Fallos Seleccionados:")
        self.lista_sintomas_seleccionados = QListWidget()

        self.label_resultado_diagnostico = QLabel("Resultado Diagnostico:")
        self.label_comprobacion_hipotesis = QLabel("Comprobación hipótesis:")
        
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


        # Listas y text area para mostrar las hipotesis
        self.texto_hipotesis = QTextEdit()
        self.texto_hipotesis.setReadOnly(True)
        
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
            self.texto_diagnostico.setPlainText("No se ha seleccionado ningún síntoma.")
            self.texto_hipotesis.clear()
            self.boton_comprobar_hipotesis.setEnabled(False)
            return

        sintomas_seleccionados = [self.lista_sintomas_seleccionados.item(i).text() for i in range(self.lista_sintomas_seleccionados.count())]
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
            self.texto_diagnostico.setPlainText(texto_diagnostico)
            self.componentes_a_comprobar = fallos_coincidentes
            self.boton_comprobar_hipotesis.setEnabled(True)
        else:
            self.texto_diagnostico.setPlainText("No se encontraron fallos coincidentes.")
            self.boton_comprobar_hipotesis.setEnabled(False)

        self.texto_hipotesis.clear()


   
    def comprobar_hipotesis(self):
        fallo_seleccionado, ok = QInputDialog.getItem(self, "Comprobación de Hipótesis", "Seleccione un componente:", self.componentes_a_comprobar, 0, False)
        
        if ok:
            resultado, descripcion = self.modelo.comprobar_hipotesis(fallo_seleccionado)
            if resultado:
                QMessageBox.information(self, "Comprobación de Hipótesis", descripcion)
            else:
                QMessageBox.information(self, "Comprobación de Hipótesis", descripcion)
            
            # Eliminar el componente comprobado de la lista
            self.componentes_a_comprobar.remove(fallo_seleccionado)
            
            # Mostrar el resultado en el cuadro de texto_hipotesis
            texto_actual = self.texto_hipotesis.toPlainText()
            texto_actual += f"- Comprobación de hipótesis, componente {fallo_seleccionado}\nResultado del análisis: {descripcion}\n\n"
            self.texto_hipotesis.setPlainText(texto_actual)

    def nuevo_diagnostico(self):
        # Limpiar las listas de síntomas seleccionados y el diagnóstico
        self.lista_sintomas_disponibles.clear()
        self.lista_sintomas_seleccionados.clear()
        self.texto_diagnostico.clear()
        self.texto_hipotesis.clear()
        self.boton_comprobar_hipotesis.setEnabled(False)
        # Re-poblar la lista de síntomas disponibles
        self.lista_sintomas_disponibles.addItems(self.modelo.obtener_sintomas())

    def guardar_diagnostico(self):
        if self.lista_sintomas_seleccionados.count() == 0 or not self.texto_diagnostico.toPlainText():
            QMessageBox.warning(self, "Guardar Diagnóstico", "No hay diagnóstico para guardar.")
            return
        
        opciones = QFileDialog.Options()
        archivo, _ = QFileDialog.getSaveFileName(self, "Guardar Diagnóstico", "", "Archivos de Texto (*.txt)", options=opciones)
        if archivo:
            with open(archivo, 'w') as file:
                file.write("FALLOS DETECTADOS:\n")
                for i in range(self.lista_sintomas_seleccionados.count()):
                    file.write(f"- {self.lista_sintomas_seleccionados.item(i).text()}\n")
                file.write("\nDESCRIPCIÓN DEL DIAGNÓSTICO:\n")
                file.write(self.texto_diagnostico.toPlainText())
                file.write("\nCOMPROBACIÓN DE LAS HIPÓTESIS:\n")
                file.write(self.texto_hipotesis.toPlainText())

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
