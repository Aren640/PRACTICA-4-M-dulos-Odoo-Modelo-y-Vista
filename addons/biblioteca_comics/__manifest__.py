# -*- coding: utf-8 -*-
{
    'name': 'Biblioteca Comics',
    'summary': 'Gestion de comics, socios y ejemplares prestables',
    'description': 'Actividad 02: modelos y vistas de prestamos actuales de comics.',
    'application': True,
    'author': 'Practica',
    'category': 'Tools',
    'version': '18.0.1.0.0',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/biblioteca_comic.xml',
        'views/biblioteca_socio.xml',
        'views/biblioteca_ejemplar_prestamo.xml',
    ],
    'installable': True,
}
