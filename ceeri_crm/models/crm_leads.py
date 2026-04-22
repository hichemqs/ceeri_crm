from odoo import models, fields,api

from datetime import timedelta



class CrmLead(models.Model):
    _inherit = 'crm.lead'

    reference_appel_offre = fields.Char(string="Tender Reference")  
    date_depot = fields.Date(string="Submission Date")
    lieu_depot = fields.Char(string="Submission Location")
    prestataire_id = fields.Many2one('res.partner', string="Supplier")

    date_verification = fields.Date(string="Verification Date")
    date_cloture_prevue = fields.Date(string="Expected Closing Date")

    project_id = fields.Many2one('project.project', string="Project")
    sale_id = fields.Many2one('sale.order', string="Sale Order")

    project_template_id = fields.Many2one('ceeri.project.template')
    sale_template_id = fields.Many2one('ceeri.sale.template')


    def action_open_validity_wizard(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Calculate Validity',
            'res_model': 'ceeri.validity.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_lead_id': self.id
            }
        }
    @api.model
    def check_depot_reminder(self):

        today = fields.Date.today()
        leads = self.search([('date_depot', '!=', False)])

        template = self.env.ref('ceeri_crm.email_template_depot_reminder')

        for lead in leads:
            if lead.date_depot:

                diff = (lead.date_depot - today).days

                if diff in [5, 2]:
                    template.send_mail(lead.id, force_send=True)     
                

    def action_open_conversion_wizard(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Convert Lead',
            'res_model': 'ceeri.conversion.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {
            'default_lead_id': self.id
        }
    }

  
    def action_open_project(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Project',
            'res_model': 'project.project',
            'view_mode': 'form',
            'res_id': self.project_id.id,
            'target': 'current',
        }    

    def action_open_sale(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Sale Order',
            'res_model': 'sale.order',
            'view_mode': 'form',
            'res_id': self.sale_id.id,
            'target': 'current',
        }    


    