from odoo import models, fields

class PlanningPlanning(models.Model):
    _inherit = 'planning.planning'

    employee_id = fields.Many2one(
        'hr.employee',
        string="Assigné à",
    )