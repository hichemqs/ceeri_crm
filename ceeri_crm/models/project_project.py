from odoo import models, fields

class ProjectProject(models.Model):
    _inherit = 'project.project'

    
    transport_mode = fields.Char()
    equipment = fields.Char()
    client_name = fields.Char()
    motif = fields.Char()
    date_start_custom = fields.Date()
    date_end_custom = fields.Date()