# -*- coding: utf-8 -*-
# Copyright 2016 SYLEAM Info Services
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Scheduled Payment',
    'version': '1.0',
    'category': 'Accounting',
    'description': """
Scheduled Payments allows customers to pay for a purchase in several instalments, instead of one single payment.
This is usually done for large amounts, so that the customer doesn't have to spend too much at once for an order.
The scheduling and amount calculation is done entirely by the merchant.
    """,
    'author': 'SYLEAM',
    'website': 'http://www.syleam.fr/',
    'depends': [
        'base',
        'account',
        'payment',
    ],
    'data': [
        'views/payment_acquirer.xml',
    ],
    'installable': True,
    'license': 'AGPL-3',
}

