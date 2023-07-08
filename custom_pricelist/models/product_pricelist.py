# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class ProductPricelist(models.Model):
    _inherit = 'product.pricelist'

    # actions

    def action_view_rules_from_pricelist(self):
        self.ensure_one()
        ctx = self._context.copy()
        ctx.update({
            'default_pricelist_id': self.id,
            'default_base': 'list_price',
        })
        return {
            'name': _(f'{self.name}: rules'),
            'type': 'ir.actions.act_window',
            'res_model': 'product.pricelist.item',
            'view_mode': 'tree,form',
            'domain': [('pricelist_id', 'in', self.ids)],
            'context': ctx,
        }
    
    def action_view_pricelist_rule_list(self):
        return {
            'name': _('Pricelist Rules'),
            'type': 'ir.actions.act_window',
            'res_model': 'product.pricelist.item',
            'domain': [('pricelist_id', 'in', self.ids)],
            'context': {'default_order': 'pricelist_id'},
            'view_mode': 'tree',
        }


class ProductPricelistItem(models.Model):
    _inherit = 'product.pricelist.item'

    code = fields.Char(string='Code', help='Code used to identify the rule.')
