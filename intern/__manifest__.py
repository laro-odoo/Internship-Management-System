{
    'name': 'Interns',
    'version': '1.0.0',
    'category': '',
    'summary': 'Complete profile of an intern',
    'description': "",
    'license': 'LGPL-3',
    # 'website': 'https://www.odoo.com/page/crm',
    'author': 'Lakshay Roopchandani',
    'depends': ['base'],
    #     # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'views/intern_profile_views.xml',
        'views/intern_menus.xml',
        # 'views/mymodule_view.xml',
    ],
    # # data files containing optionally loaded demonstration data
    # 'demo': [
    #     'demo/demo_data.xml',
    # ],
    'installable': True,
    'application': True,
    'auto_install': False,
}