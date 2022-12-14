# -*- coding: utf-8 -*-
{
    'name': "Training",

    'summary': """
        Module for the management and monitoring of employee training actions""",

    'description': """
        Module for the management and monitoring of employee training actions
    """,

    'author': "Àlex Milan",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Specific Industry Applications',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base','hr'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'data/data.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/hr.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        'report/formative_action_report.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml'
    ],
    'installable': True,
    'application': True,
}