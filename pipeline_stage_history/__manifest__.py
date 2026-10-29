{
    'name': 'Opportunity Stage History',
    'version': '18.0.1.0',
    'summary': 'CRM Lead Stage History, Opportunity Stage History, CRM Stage History, Stage History, Stage Audit History, CRM Stage Audit History',
    'author': 'Tech GMB',
    # 'website': '',
    'category': 'Extra Tools',
    'license': 'LGPL-3',
    'depends': ['base', 'crm'],

    'data': [
        'security/ir.model.access.csv',
        'views/crm_lead_views.xml',
    ],
    'images': ['static/description/banner.png'],
    'installable': True,
    'auto_install': False,
    'application': True
}
