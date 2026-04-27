# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.exceptions import ValidationError


class BibliotecaEjemplarPrestamo(models.Model):
    _name = 'biblioteca.ejemplar.prestamo'
    _description = 'Ejemplar prestable de comic'

    comic_id = fields.Many2one('biblioteca.comic', string='Comic', required=True)
    socio_id = fields.Many2one('biblioteca.socio', string='Socio')
    fecha_inicio_prestamo = fields.Date(string='Fecha inicio prestamo')
    fecha_fin_prevista = fields.Date(string='Fecha fin prevista')

    @api.constrains('fecha_inicio_prestamo')
    def _check_fecha_inicio_no_futura(self):
        today = fields.Date.today()
        for record in self:
            if record.fecha_inicio_prestamo and record.fecha_inicio_prestamo > today:
                raise ValidationError('La fecha de prestamo no puede ser posterior al dia actual.')

    @api.constrains('fecha_fin_prevista')
    def _check_fecha_fin_no_pasada(self):
        today = fields.Date.today()
        for record in self:
            if record.fecha_fin_prevista and record.fecha_fin_prevista < today:
                raise ValidationError('La fecha prevista de devolucion no puede ser anterior al dia actual.')
