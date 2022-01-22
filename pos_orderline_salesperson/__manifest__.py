# -*- coding: utf-8 -*-
{
    'name': 'POS Orderline Salesperson',
    'version': '13.1.1.0',
    'summary': 'POS Orderline Salesperson',
    'category': 'Sales/Point Of Sale',
    'author': 'Zeinab Abdelmonem',
    'email': 'zeinababdelmonem9@gmail.com',
    'depends': ['point_of_sale'],
    'data': [
        'views/pos_config_views.xml',
        'views/pos_template.xml',
        'views/pos_order_views.xml',
    ],
    'qweb': [
        'static/src/xml/salesperson_popup.xml',
        'static/src/xml/salesperson.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'application': True,
    'auto_install': False,
}
