# -*- coding: utf-8 -*-
from odoo import fields, models, api

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    #config access to smartystreet api and related data with website
    auth_id = fields.Char('Auth Id', related='website_id.auth_id', required=True,readonly=False)
    auth_token = fields.Char('Auth Token', related='website_id.auth_token', required=True,readonly=False)
    validate_type = fields.Selection([('us','US'),('national','International')], related='website_id.validate_type', string="Validation Type", required=True)


    #get data from config
    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        params = self.env['ir.config_parameter'].sudo()

        res.update(
            auth_id=params.get_param('smartystreets_verification_address.auth_id'),
            auth_token=params.get_param('smartystreets_verification_address.auth_token'),
            validate_type=params.get_param('smartystreets_verification_address.validate_type'),
        )
        return res

    #set data in config
    def set_values(self):
        super(ResConfigSettings, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param('smartystreets_verification_address.auth_id', self.auth_id)
        self.env['ir.config_parameter'].sudo().set_param('smartystreets_verification_address.auth_token', self.auth_token)
        self.env['ir.config_parameter'].sudo().set_param('smartystreets_verification_address.validate_type', self.validate_type)
