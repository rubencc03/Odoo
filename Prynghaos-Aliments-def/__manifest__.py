# -*- coding: utf-8 -*-
{   
    #Nombre del archivo
    'name': "Recogida ALimentosVDef",

    #Summary
    'summary': """
    La mejor aplicacion de Recogida de alimentos""",

    #Descripción
    'description': """
    Sencillo modulo encargado de gestionar los alimentos de una empresa muy maja
    """,

    #Autor del modulo del año
    'author': "Prynghaos:)",

    #Indicamos que es una aplicación
    'application': True,

    #Indicamos en que apartado de Odoo estara mas su versión
    'category': 'Productivity',
    'version': '0.1',

    # Indicamos lista de modulos necesarios para que este funcione correctamente
    # En este ejemplo solo depende del modulo "base"
    'depends': ['base'],

    #Datos que debe cargar
    'data': [
        #fichero seguridad
        'security/ir.model.access.csv',
        #Cargamos las vistas y las plantillas   
        'views/registros.xml',
        'views/voluntario.xml',
        'views/alimento.xml',
        'report/registrospdf.xml',
        'cron/cron_data.xml' 


        
    ]
}
