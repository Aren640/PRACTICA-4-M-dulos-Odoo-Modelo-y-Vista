from odoo import api, fields, models


class HospitalPaciente(models.Model):
    _name = 'hospital.paciente'
    _description = 'Paciente'
    _rec_name = 'nombre_completo'

    nombre = fields.Char(required=True)
    apellidos = fields.Char(required=True)
    sintomas = fields.Text()

    consulta_ids = fields.One2many('hospital.consulta', 'paciente_id', string='Consultas')

    nombre_completo = fields.Char(compute='_compute_nombre_completo', store=True)

    @api.depends('nombre', 'apellidos')
    def _compute_nombre_completo(self):
        for rec in self:
            rec.nombre_completo = ((rec.nombre or '') + ' ' + (rec.apellidos or '')).strip()
