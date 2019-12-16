# -*- coding: utf-8 -*-
{
    'name' : 'Backend Custom',
    'version' : '1.0',
    'summary': '',
    'category': 'Backend',
    'sequence': 20,
    'description': """ """,
    'author': 'Zeinab Abdelmonem',
    'depends' : ['web','account_invoicing','sale_management'],
    'data': [
            'views/web_client_templete.xml',
            'views/res_partner_view.xml',
            'views/product_view.xml',
            'views/sale.xml',
            'wizard/general_ledger_report_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
