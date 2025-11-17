# -*- coding: utf-8 -*-
{
    'name': "Lista de tareas",
    'summary': """
Sencilla Lista de tareas
""",
    'description': """
Sencilla lista de tareas utilizada para crear un nuevo módulo con un nuevo
modelo de datos.

#Añadi los campos de descripción y fecha límite
""",
    'author': "Sergi García",
    'website': "https://apuntesfpinformatica.es",

    'application': True,

    'category': 'Productivity',
    'version': '0.2',

    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
        'views.xml',
    ],
}


