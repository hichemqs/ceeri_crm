# from odoo import http


# class CeeriCrm(http.Controller):
#     @http.route('/ceeri_crm/ceeri_crm', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ceeri_crm/ceeri_crm/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ceeri_crm.listing', {
#             'root': '/ceeri_crm/ceeri_crm',
#             'objects': http.request.env['ceeri_crm.ceeri_crm'].search([]),
#         })

#     @http.route('/ceeri_crm/ceeri_crm/objects/<model("ceeri_crm.ceeri_crm"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ceeri_crm.object', {
#             'object': obj
#         })

