# -*- coding: utf-8 -*-
from odoo import fields, models

class Website(models.Model):
    _inherit = 'website'

    #config access to smartystreet api
    auth_id = fields.Char('Auth Id', required=True)
    auth_token = fields.Char('Auth Token', required=True)
    validate_type = fields.Selection([('us','US'),('inter','International')], string="Validation Type", required=True)
    