# -*- coding: utf-8 -*-
from odoo import fields, models


class BaseArchive(models.AbstractModel):
    _name = 'base.archive'
    _description = 'Fichero abstracto'

    activo = fields.Boolean(default=True)

    def archivar(self):
        for record in self:
            record.activo = not record.activo


class BibliotecaComic(models.Model):
    _name = 'biblioteca.comic'
    _inherit = ['base.archive']
    _description = 'Comic de biblioteca'
    _order = 'fecha_publicacion desc, nombre'
    _rec_name = 'nombre'

    nombre = fields.Char('Titulo', required=True, index=True)
    estado = fields.Selection(
        [
            ('borrador', 'No disponible'),
            ('disponible', 'Disponible'),
            ('perdido', 'Perdido'),
        ],
        'Estado',
        default='borrador',
    )
    descripcion = fields.Html('Descripcion', sanitize=True, strip_style=False)
    portada = fields.Binary('Portada Comic')
    fecha_publicacion = fields.Date('Fecha publicacion')
    precio = fields.Float('Precio')
    paginas = fields.Integer('Numero de paginas')
    valoracion_lector = fields.Float('Valoracion media lectores', digits=(14, 4))
    autor_ids = fields.Many2many('res.partner', string='Autores')

    ejemplar_ids = fields.One2many(
        'biblioteca.ejemplar.prestamo',
        'comic_id',
        string='Ejemplares prestables',
    )

    _sql_constraints = [
        ('name_uniq', 'UNIQUE (nombre)', 'El titulo Comic debe ser unico.'),
        ('positive_page', 'CHECK(paginas>0)', 'El comic debe tener al menos una pagina'),
    ]
