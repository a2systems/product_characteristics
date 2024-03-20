# -*- coding: utf-8 -*-
{
    'name': "Product Characteristics",

    'summary': """
        Product Characteristics""",

    'description': """
        Product Characteristics
    """,

    'category': 'Sales',
    'version': '0.1',

    'depends': ['product'],

    'data': [
        'security/ir.model.access.csv',
        'views/characteristics_view.xml',
        'views/product_view.xml',
    ],
    'assets': {
    },
}
