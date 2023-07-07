# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class ProductPricelist(models.Model):
    _inherit = 'product.pricelist'

    def _get_applicable_rules_domain(self, products, date, **kwargs):
        rules_domain = super()._get_applicable_rules_domain(products, date, **kwargs)
        brand_domain = [
            '|', 
            ('product_brand_id', '=', False), 
            ('product_brand_id', 'in', products.product_brand_id.ids),
        ]
        return [
            rules_domain[0],
            *brand_domain,
            *rules_domain[1:]
        ]


class ProductPricelistItem(models.Model):
    _inherit = 'product.pricelist.item'

    applied_on = fields.Selection(
        selection_add=[('4_product_brand', 'Product Brand'),],
        ondelete={'4_product_brand': 'set default'}
    )
    product_brand_id = fields.Many2one('product.brand', string='Brand')

    @api.depends('product_brand_id')
    def _compute_name_and_price(self):
        super()._compute_name_and_price()
        brand_items = self.filtered(lambda r: r.applied_on == '4_product_brand')
        for item in brand_items:
            item.name = _('Brand: %s') %(item.product_brand_id.name)
    
    @api.constrains('product_brand_id')
    def _check_product_brand_consistency(self):
        for item in self:
            if item.applied_on == '4_product_brand' and not item.product_brand_id:
                raise ValidationError(_("Please specify the producto brand for which this rule should be applied"))

    def _is_applicable_for(self, product, qty_in_product_uom):
        if (self.product_brand_id and self.product_brand_id == product.product_brand_id) and\
                (qty_in_product_uom > self.min_quantity):
            return True
        return super()._is_applicable_for(product, qty_in_product_uom)

    def write(self, values):
        if values.get('applied_on', False):
            applied_on = values['applied_on']
            if applied_on == '4_product_brand':
                values.update(dict(product_id=None, product_tmpl_id=None, categ_id=None))
            else:
                values['product_brand_id'] = False
        return super().write(values)
