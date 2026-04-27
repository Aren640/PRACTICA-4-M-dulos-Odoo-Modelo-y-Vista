# -*- coding: utf-8 -*-
from odoo import fields, models


class BibliotecaSocio(models.Model):
    _name = 'biblioteca.socio'
    _description = 'Socio de biblioteca'
    _rec_name = 'identificador'

    nombre = fields.Char(required=True)
    apellido = fields.Char(required=True)
    identificador = fields.Char(required=True)

    ejemplar_ids = fields.One2many(
        'biblioteca.ejemplar.prestamo',
        'socio_id',
        string='Ejemplares prestados actuales',
    )

    _sql_constraints = [
        ('identificador_uniq', 'UNIQUE (identificador)', 'El identificador del socio debe ser unico.'),
    ]
