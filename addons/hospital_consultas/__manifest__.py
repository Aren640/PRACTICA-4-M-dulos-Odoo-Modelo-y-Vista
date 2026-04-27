# -*- coding: utf-8 -*-
{
    'name': 'Hospital Consultas',
    'summary': 'Gestion simple de pacientes, medicos y consultas',
    'description': 'Actividad 03: modelos y vistas de hospital.',
    'author': 'Practica',
    'category': 'Tools',
    'version': '18.0.1.0.0',
    'license': 'LGPL-3',
    'application': True,
    'installable': True,
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/hospital_paciente_views.xml',
        'views/hospital_medico_views.xml',
        'views/hospital_consulta_views.xml',
        'views/hospital_menus.xml',
    ],
}