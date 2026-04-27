from odoo import fields, models


class InstitutoCiclo(models.Model):
    _name = "instituto.ciclo"
    _description = "Ciclo Formativo"
    _rec_name = "nombre"

    nombre = fields.Char(required=True)
    descripcion = fields.Text()
    modulo_ids = fields.One2many("instituto.modulo", "ciclo_id", string="Modulos")
