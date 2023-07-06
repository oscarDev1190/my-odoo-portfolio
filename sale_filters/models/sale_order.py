# -*- coding: utf-8 -*-

from odoo import api, fields, models

from lxml import etree
import pprint


def create_filter_tag(name: str, label: str, domain: str) -> 'etree.Element':
    return etree.Element(
        'filter',
        name=name,
        string=label,
        domain=domain
    )


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.model
    def _insert_dynamic_filters(self, fieldname, doc):
        model_field = self._fields.get(fieldname)
        if not model_field or model_field.type != 'many2one':
            return
        records = self.env[model_field.comodel_name].search([])
        for record in records:
            pricelist_filter = create_filter_tag(
                name=record.display_name.lower().replace(' ', '_'),
                label=record.display_name,
                domain=f"[('{fieldname}', '=', {record.id})]"
            )
            doc.append(pricelist_filter)
        else:
            if len(records):
                doc.append(etree.Element('separator'))
    
    @api.model
    def _get_fields_for_dynamic_filters(self):
        return ['pricelist_id', 'payment_term_id', 'fiscal_position_id']

    @api.model
    def get_views(self, views, options=None):
        res = super().get_views(views, options)
        search_arch = res['views'].get('search')
        if search_arch:
            doc = etree.fromstring(search_arch['arch'])
            dynamic_filters_fields = self._get_fields_for_dynamic_filters()
            for fieldname in dynamic_filters_fields:
                self._insert_dynamic_filters(fieldname, doc)

            res['views']['search']['arch'] = etree.tostring(doc)

        return res