from odoo import models, fields

class ProjectTemplate(models.Model):
    _name = 'ceeri.project.template'
    _description = 'Project Template'

    name = fields.Char(required=True)
    default_partner_id = fields.Many2one('res.partner')