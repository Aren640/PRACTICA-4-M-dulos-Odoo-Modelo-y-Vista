from odoo import api, fields, models


class HospitalMedico(models.Model):
    _name = 'hospital.medico'
    _description = 'Medico'
    _rec_name = 'nombre_completo'

    nombre = fields.Char(required=True)
    apellidos = fields.Char(required=True)
    numero_colegiado = fields.Char(required=True)

    consulta_ids = fields.One2many('hospital.consulta', 'medico_id', string='Consultas')

    nombre_completo = fields.Char(compute='_compute_nombre_completo', store=True)

    _sql_constraints = [
        ('numero_colegiado_uniq', 'UNIQUE (numero_colegiado)', 'El numero de colegiado debe ser unico.'),
    ]

    @api.depends('nombre', 'apellidos')
    def _compute_nombre_completo(self):
        for rec in self:
            rec.nombre_completo = ((rec.nombre or '') + ' ' + (rec.apellidos or '')).strip()
