# -*- coding: utf-8 -*-
{
    'name': "POS Pricelist Brand",
    'summary': """ POS apply discounts according to product brand  """,
    'description': """""",
    'author': "Oscar Llovera",
    'website': "https://github.com/oscarDev1190/my-odoo-portfolio/tree/V16",
    'category': 'Sales/Point of Sale',
    'version': '16.0.1.0.0',
    'depends': ['pricelist_brand', 'point_of_sale'],   
    'data': [],
    'assets': {
        'point_of_sale.assets': ['pos_pricelist_brand/static/src/js/models.js',],
    },
    'license': 'AGPL-3'
}
