# -*- coding: utf-8 -*-
{
    'name': 'Lista de tareas',
    'summary': 'Modulo educativo para lista de tareas',
    'description': 'Lista de tareas con vista lista, formulario, kanban y calendario.',
    'author': 'Practica',
    'category': 'Productivity',
    'version': '18.0.1.0.0',
    'license': 'LGPL-3',
    'application': True,
    'installable': True,
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
}
