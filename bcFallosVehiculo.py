#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 18:13:31 2024

@author: joaquin / luzmarina
"""

class FallosVehiculo:
    def __init__(self):
        # Simulando una lista de fallos con síntomas asociados
        self.fallos = {
            'Batería': ['El coche no arranca'],
            'Bujía': ['El coche no arranca', 'Pérdida de potencia'],
            'Motor': ['Sobrecalentamiento de motor', 'Pérdida de potencia', 'Ruidos extraños', 'Emisiones de humo extrañas', 'Consumo elevado de combustible'],
            'Radiador': ['Sobrecalentamiento de motor'],
            'Chasis': ['Vibraciones anormales', 'Ruidos extraños', 'Problemas de dirección'],
            'Filtro de Aceite': ['Sobrecalentamiento de motor'],
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
