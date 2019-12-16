# -*- coding: utf-8 -*-
import json
from odoo import api, fields, models
from lxml import etree

class ResPartner(models.Model):
    _inherit = 'res.partner'

    #add state to customer 
    state = fields.Selection([('draft','Draft'),
    						('approved','Approved')],'State',default='draft')

    
    #change state to approved and update contex to make fields readonly
    @api.one
    def action_approve(self):
        self.state = 'approved'
        context = self.env.context.copy()
        context.update({'read_only': 'true'})
        self.env.context = context
        return self.fields_view_get(view_id=None, view_type='form', toolbar=False, submenu=False)


    #inherit function to make all fields readonly 
    @api.model
    def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False):
        res = super(ResPartner, self).fields_view_get(view_id=view_id, view_type=view_type, toolbar=toolbar, submenu=submenu)
        partner_id = self.env.context.get('params', {}).get('id')
        read_only = self.env.context.get('read_only',False)
        doc = etree.XML(res['arch'])
        if view_type == 'form':
            partner_obj = self.browse(partner_id)
            for node in doc.xpath("//field"):
                if partner_obj.state == 'approved' or read_only == 'true':
                    node.set('readonly', '1')
                    modifiers = json.loads(node.get("modifiers"))
                    modifiers['readonly'] = True
                    node.set("modifiers", json.dumps(modifiers))
        res['arch'] = etree.tostring(doc, encoding='unicode')
        return res