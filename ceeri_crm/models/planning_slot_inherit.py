from odoo import models, fields

class PlanningSlot(models.Model):
    _inherit = 'planning.slot'

    employee_id = fields.Many2one(
        'hr.employee',
        string="Assigned Employee"
    )