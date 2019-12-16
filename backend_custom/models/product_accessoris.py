# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ProductAccessories(models.Model):
    _name = "product.accessories"
    _description = "Product Accessories"

    #new object to set sub prodects 
    product_id = fields.Many2one('product.product',string='Product')
    qty = fields.Float('Qty', default=1)
