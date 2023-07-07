# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PosSession(models.Model):
    _inherit = 'pos.session'


    def _product_pricelist_item_fields(self):
        return ['product_brand_id'] + super()._product_pricelist_item_fields()
    
    def _loader_params_product_product(self):
        res = super()._loader_params_product_product()
        res['search_params']['fields'] = res['search_params']['fields'].append('product_brand_id')
        return res
