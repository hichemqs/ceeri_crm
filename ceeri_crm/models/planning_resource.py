from odoo import models, fields

class PlanningSlot(models.Model):
    _inherit = 'planning.slot'

    employee_id = fields.Many2one(
        'hr.employee',
        string="Assigné à",
        help="L'employé responsable de cette ressource"
    )