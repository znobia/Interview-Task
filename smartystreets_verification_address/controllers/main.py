# -*- coding: utf-8 -*-

from odoo.addons.website_sale.controllers.main import WebsiteSale
from odoo import http, tools, _
from odoo.http import request
from urllib.parse import quote
import requests

class WebsiteSale(WebsiteSale):

    def checkout_form_validate(self, mode, all_form_values, data):
        #inhert method to check validate if addreess with smartystreets
        auth_id = request.env['ir.config_parameter'].sudo().get_param('smartystreets_verification_address.auth_id')
        auth_token = request.env['ir.config_parameter'].sudo().get_param('smartystreets_verification_address.auth_token')
        validate_type = request.env['ir.config_parameter'].sudo().get_param('smartystreets_verification_address.validate_type')
        error, error_message = super(WebsiteSale,self).checkout_form_validate(mode, all_form_values, data)
        country_obj = request.env['res.country']
        state_obj = request.env['res.country.state']
        country_name = ''
        address1 = ''
        address2 = ''
        city = ''
        zip_code = ''
        state = ''
        #check if exist data (country, street and city because required fields)
        if data.get("country_id") and data.get("street") and data.get("city"):
            country = country_obj.browse(int(data.get('country_id')))
            country_name = country.name
            if country_name:
                # using qute to convert string to used in url exmple: "South Sudan" to "South%20Sudan"
                country_name = quote(country.name)
            address1 = quote(data.get("street"))
            city = quote(data.get("city"))
            if data.get('state_id'):
                state_id = state_obj.browse(int(data.get('state_id')))
                state = quote(state_id.name)
            if data.get("street2"):
                address2 = quote(data.get("street2"))
            if data.get("zip"):
                zip_code = quote(data.get("zip"))

            if auth_id and auth_token:
                try:
                    req = ''
                    print (validate_type,"<<<<<<<<<<<<validate_type")
                    #check type of validation and get data
                    if validate_type == 'national':
                        req = requests.get('https://international-street.api.smartystreets.com/verify?auth-id='+auth_id+'&auth-token='+auth_token+'&country='+country_name+'&address1='+address1+'&address2='+address1+'&locality='+city+'&administrative_area=&postal_code='+zip_code+'&geocode=true"')
                    else:
                        req = requests.get('https://us-street.api.smartystreets.com/street-address?auth-id='+auth_id+'&auth-token='+auth_token+'&street='+address1+'&street2='+address2+'&city='+city+'&state='+state)
                    #check status_code of request and send error message to show in client
                    if req.status_code == 401:
                        error["address"] = 'error'
                        error_message.append(_('Auth Id or Auth Token not correct'))
                    if req.status_code == 402:
                        error["address"] = 'error'
                        error_message.append(_('There is no active subscription for the account associated .'))

                    if req.status_code == 200:
                        #if the not valid addres get reais massege 
                        if req.json() == []:
                            error["address"] = 'error'
                            error_message.append(_('Please Enter Valid Address'))

                        #if valid address create data in model(smartystreets.data)
                        else:
                            request.env['smartystreets.data'].create({
                                'name':data.get("name"),
                                'country': country_name,
                                'address1':address1,
                                'address2':address2,
                                'city':city, 'state':state,
                                'email':data.get("email"),
                                'phone':data.get("phone"),
                                'zip_code':zip_code,
                            })
                #using expect to get error in raise massege not show all detail to customer
                except requests.ConnectionError:
                        error["address"] = 'error'
                        error_message.append(_('Please check Internet connection'))

            else:                
                error["address"] = 'error'
                error_message.append(_('Please enter (Auth ID and Token) in config To validation address'))

        return error, error_message
