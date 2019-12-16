# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    #add many2many from accessors object
    product_accessories_ids = fields.Many2many('product.accessories',string='Accessories')
