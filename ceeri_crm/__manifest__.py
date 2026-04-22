{
    'name': "ceeri_crm",

    'summary': "CEERI CRM Project",

    'licence': 'LGPL-3',
    'author': "CEERI",
    'website': "https://www.ceeri.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'CRM',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'crm',
    'project',
    'sale_management',
    'mail',
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/crm_lead_view.xml',
        'wizard/validity_wizard_view.xml',
        'data/email_template.xml',
        'data/cron.xml',
        'data/sequence.xml',
        'report/layout_ceeri.xml',
        'report/report_rapport.xml',
        'report/report_action.xml',
        'server_action.xml',
        'views/task_view.xml',
        'views/conversion_wizard.xml',
        'views/project_template_views.xml',
        'views/sale_template_views.xml'
    ],
   'installable': True,
   'application': True,
}

