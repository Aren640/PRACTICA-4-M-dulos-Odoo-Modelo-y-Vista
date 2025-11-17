# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ListaTareas(models.Model):
    _name = 'lista_tareas.lista_tareas'
    _description = 'Lista de tareas'

    tarea = fields.Char(string="Tarea")
    prioridad = fields.Integer(string="Prioridad")
    urgente = fields.Boolean(compute="_value_urgente", store=True, string="Urgente")
    realizada = fields.Boolean(string="Realizada")
    # Miss nuevos cambios
    descripcion = fields.Text(string="Descripción")
    fecha_limite = fields.Date(string="Fecha límite")

    @api.depends('prioridad')
    def _value_urgente(self):
        for record in self:
            if record.prioridad and record.prioridad > 10:
                record.urgente = True
            else:
                record.urgente = False





