# -*- coding: utf-8 -*-
{
    "name": "Instituto Ciclos Formativos",
    "summary": "Actividad 04: modelos, relaciones, vistas y seguridad",
    "description": "Gestion simple de ciclos, modulos, alumnos y profesores.",
    "author": "Practica",
    "category": "Education",
    "version": "18.0.1.0.0",
    "license": "LGPL-3",
    "depends": ["base"],
    "data": [
        "security/groups.xml",
        "security/users.xml",
        "security/ir.model.access.csv",
        "views/ciclo_views.xml",
        "views/modulo_views.xml",
        "views/alumno_views.xml",
        "views/profesor_views.xml",
        "views/menus.xml",
    ],
    "installable": True,
    "application": True,
}