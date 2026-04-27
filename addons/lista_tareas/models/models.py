# -*- coding: utf-8 -*-
from odoo import api, fields, models


class ListaTareas(models.Model):
    _name = 'lista_tareas.lista'
    _description = 'Modelo de la lista de tareas'
    _rec_name = 'tarea'

    tarea = fields.Char(string='Tarea')
    prioridad = fields.Integer(string='Prioridad')
    urgente = fields.Boolean(string='Urgente', compute='_compute_urgente', store=True)
    realizada = fields.Boolean(string='Realizada')
    fecha = fields.Date(string='Fecha')

    @api.depends('prioridad')
    def _compute_urgente(self):
        for record in self:
            record.urgente = record.prioridad > 10
