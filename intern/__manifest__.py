{
    'name': 'Interns',
    'version': '1.0.0',
    'category': '',
    'summary': 'Complete profile of an intern',
    'description': "",
    'license': 'LGPL-3',
    'author': 'Lakshay Roopchandani',
    'depends': ['base'],
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        
        'views/intern_profile_views.xml',
        'views/intern_mentor_profile_views.xml',
        'views/intern_project_views.xml',
        'views/intern_assignment_views.xml',
        'views/intern_report_views.xml',
        'views/intern_menus.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
