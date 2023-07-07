odoo.define('pos_pricelist_brand', require => {
    'use strict';

    const Registries = require('point_of_sale.Registries');
    const { Product } = require('point_of_sale.models');


    const ProductWithRuleBrand = (Product) => class ProductWithRuleBrand extends Product {

        isPricelistItemUsable(item, date) {
            return (
                ((!item.product_brand_id || !this.product_brand_id) || 
                (item.product_brand_id[0] === this.product_brand_id[0])) &&
                super.isPricelistItemUsable(...arguments)
            );
        }
    }

    Registries.Model.extend(Product, ProductWithRuleBrand)
});