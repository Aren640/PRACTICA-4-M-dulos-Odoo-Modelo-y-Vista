from odoo import fields, models


class HospitalConsulta(models.Model):
    _name = 'hospital.consulta'
    _description = 'Consulta medica'
    _order = 'fecha_consulta desc, id desc'

    paciente_id = fields.Many2one('hospital.paciente', string='Paciente', required=True)
    medico_id = fields.Many2one('hospital.medico', string='Medico', required=True)
    diagnostico = fields.Text(required=True)
    fecha_consulta = fields.Date(default=fields.Date.today, required=True)
