from odoo import models, fields, api

class ProjectTask(models.Model):
    _inherit = 'project.task'


    date_aller = fields.Datetime(string="Date Start")

    mission_number = fields.Char(string="Mission Number", readonly=True, copy=False)

    @api.model_create_multi
    def create(self, vals_list):

        seq_model = self.env['ir.sequence']

        for vals in vals_list:
            seq = seq_model.next_by_code('ceeri.mission') or '000'
            today = fields.Date.today()

            vals['mission_number'] = f"{seq}-{today.strftime('%d/%m/%Y')}"

        return super().create(vals_list)

    def get_followers_partners(self):
        return self.message_follower_ids.mapped('partner_id')    