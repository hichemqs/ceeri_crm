from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    firstname = fields.Char(compute="_compute_name_parts", store=True)
    lastname = fields.Char(compute="_compute_name_parts", store=True)

    @api.depends('name')
    def _compute_name_parts(self):
        for rec in self:
            if rec.name:
                parts = rec.name.split(' ')
                rec.firstname = parts[0]
                rec.lastname = ' '.join(parts[1:]) if len(parts) > 1 else ''
            else:
                rec.firstname = ''
                rec.lastname = ''