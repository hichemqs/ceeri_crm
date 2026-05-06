from odoo import models, fields
from datetime import timedelta

class ValidityWizard(models.TransientModel):
    _name = 'ceeri.validity.wizard'
    _description = 'Validity Calculator Wizard'

    validity_days = fields.Selection([
        ('30', '30 Days'),
        ('90', '90 Days'),
        ('180', '180 Days')
    ], string="Validity")

    lead_id = fields.Many2one('crm.lead')

    def action_compute_validity(self):
        self.ensure_one()
        days = int(self.validity_days)
        new_date = fields.Date.today() + timedelta(days=days)
        self.lead_id.date_cloture_prevue = new_date