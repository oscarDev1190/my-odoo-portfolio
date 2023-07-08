# -*- coding: utf-8 -*-
{
    'name': "Pricelist Custom",
    'summary': """ Customizations in models and price list views. """,
    'description': """""",
    'author': "Oscar Llovera",
    'website': "https://github.com/oscarDev1190/my-odoo-portfolio/tree/V16",
    'category': 'Sales/Sales',
    'version': '16.0.1.0.0',
    'depends': [
        'sale_management',
    ],   
    'data': [
        'data/server_actions.xml',
        'views/product_pricelist_views.xml',
    ],
    'license': 'AGPL-3'
}
