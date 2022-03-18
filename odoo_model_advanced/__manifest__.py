# -*- coding: utf-8 -*-
{
    'name': "odoo_model_advanced",

    'summary': """
        Conceptos avanzados de modelos""",

    'description': """
        Curso de conceptos avanzados de modelos
    """,

    'author': "Hector Disla",
    'website': "https://www.dislatech.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Customizations',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
