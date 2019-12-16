# -*- coding: utf-8 -*-
from odoo import api, fields, models


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    #add sequene to numbered sequential to perant and sub products
    number = fields.Char('No')
    
    @api.multi
    @api.onchange('product_id')
    def product_id_change(self):
    	result = super(SaleOrderLine, self).product_id_change()
    	print (self.product_id,"<<<<<<<<<<<<<<<<<<<<<number = fields.Char('No')")
    	# if not self.order_line:
    	# 	self.number = 1
    	if self.product_id.product_accessories_ids:
    		print ("insssssssssssssssssss")
    		for accessory in self.product_id.product_accessories_ids:
    			print (accessory,">>>>>>>>><<<<<<<<<mm")
    			

    	return result

