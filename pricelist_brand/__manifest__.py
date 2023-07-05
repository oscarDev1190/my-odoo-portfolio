# -*- coding: utf-8 -*-
{
    'name': "Pricelist Brand",
    'summary': """ Apply discounts according to product brand """,
    'description': """""",
    'author': "Oscar Llovera",
    'website': "https://www.yourcompany.com",
    'category': 'Product',
    'version': '16.0.1.0.0',
    'depends': [
        'product_brand',    # The dependency product_brand belongs to the OCA: https://github.com/OCA/brand/tree/16.0
    ],   
    'data': [
        'views/product_pricelist_views.xml',
    ],
    'license': 'AGPL-3'
}
