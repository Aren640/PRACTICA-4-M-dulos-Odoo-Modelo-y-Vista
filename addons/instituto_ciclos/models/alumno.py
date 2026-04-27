from odoo import api, fields, models


class InstitutoAlumno(models.Model):
    _name = "instituto.alumno"
    _description = "Alumno"
    _rec_name = "nombre_completo"

    nombre = fields.Char(required=True)
    apellidos = fields.Char(required=True)
    nombre_completo = fields.Char(compute="_compute_nombre_completo", store=True)
    modulo_ids = fields.Many2many(
        "instituto.modulo",
        "instituto_modulo_alumno_rel",
        "alumno_id",
        "modulo_id",
        string="Modulos matriculados",
    )

    @api.depends("nombre", "apellidos")
    def _compute_nombre_completo(self):
        for record in self:
            record.nombre_completo = " ".join(filter(None, [record.nombre, record.apellidos]))
