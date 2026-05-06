from odoo import models, fields

class SaleTemplate(models.Model):
    _name = 'ceeri.sale.template'
    _description = 'Sale Order Template'

    name = fields.Char(required=True)