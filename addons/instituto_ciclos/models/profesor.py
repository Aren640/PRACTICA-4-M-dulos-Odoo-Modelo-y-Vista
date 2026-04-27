from odoo import api, fields, models


class InstitutoProfesor(models.Model):
    _name = "instituto.profesor"
    _description = "Profesor"
    _rec_name = "nombre_completo"

    nombre = fields.Char(required=True)
    apellidos = fields.Char(required=True)
    nombre_completo = fields.Char(compute="_compute_nombre_completo", store=True)
    numero_colegiado = fields.Char(required=True)
    modulo_ids = fields.One2many("instituto.modulo", "profesor_id", string="Modulos que imparte")

    @api.depends("nombre", "apellidos")
    def _compute_nombre_completo(self):
        for record in self:
            record.nombre_completo = " ".join(filter(None, [record.nombre, record.apellidos]))
