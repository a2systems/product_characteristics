from odoo import fields, models, api, _
from odoo.exceptions import ValidationError
from datetime import date

class ProductCharacteristic(models.Model):
    _name = "product.characteristic"
    _description = "product.characteristic"

    name = fields.Char('Nombre')
