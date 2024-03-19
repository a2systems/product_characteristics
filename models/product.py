from odoo import fields, models, api, _
from odoo.exceptions import ValidationError
from datetime import date

class ProductTemplate(models.Model):
    _inherit = "product.template"

    characteristic_ids = fields.Many2many(
            comodel_name='product.characteristic',
            relname='characteristic_rel',
            col1='tmpl_id',
            col2='char_id',
            string='Caracteristicas')
