# -*- coding: utf-8 -*-
{
    'name' : 'Smartystreets Verification Address',
    'version' : '1.0',
    'summary': 'Validation Address',
    'category': 'Website',
    'sequence': 20,
    'description': """ Verification addresses in checkout form when customer shop products """,
    'author': 'Zeinab Abdelmonem',
    'depends' : ['website_sale'],
    'data': [
            'views/res_config_settings.xml',

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
