# -*- coding: utf-8 -*-
from odoo import fields, models

class SmartystreetsData(models.Model):
    _name = 'smartystreets.data'

    name = fields.Char('Name', required=True)
    country = fields.Char('Country')    
    address1 = fields.Char('Address1')    
    address2 = fields.Char('Address2')    
    email = fields.Char('Email')    
    city = fields.Char('City')    
    state = fields.Char('State')    
    phone = fields.Char('Phone')
    zip_code = fields.Char("Zip Code")  