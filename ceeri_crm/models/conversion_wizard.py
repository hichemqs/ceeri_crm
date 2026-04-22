from odoo import models, fields

class CrmConversionWizard(models.TransientModel):
    _name = 'ceeri.conversion.wizard'
    _description = 'CRM Conversion Wizard'

    lead_id = fields.Many2one('crm.lead', required=True)

    create_project = fields.Boolean(default=True)
    create_sale = fields.Boolean(default=True)

    project_template_id = fields.Many2one('ceeri.project.template')
    sale_template_id = fields.Many2one('ceeri.sale.template')

    def action_convert(self):
        self.ensure_one()
        lead = self.lead_id

        project = False
        sale = False

        if self.create_project:

            project_vals = {
                'name': lead.name,
                'partner_id': lead.partner_id.id,
                'date_verification': lead.date_verification,
            }

            if self.project_template_id and self.project_template_id.default_partner_id:
                project_vals['partner_id'] = self.project_template_id.default_partner_id.id

            project = self.env['project.project'].create(project_vals)

        if self.create_sale:

            sale_vals = {
                'partner_id': lead.partner_id.id,
                'origin': lead.name,
            }

            sale = self.env['sale.order'].create(sale_vals)

        
        if sale and project:
            sale.project_id = project.id

        lead.project_id = project.id if project else False
        lead.sale_id = sale.id if sale else False