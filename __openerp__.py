# -*- coding: utf-8 -*-
##############################################################################
#
#    payment_scheduled module for OpenERP, Allows customers to pay for a purchase in several instalments
#    Copyright (C) 2016 SYLEAM Info Services (<http://www.syleam.fr/>)
#              Sebastien LANGE <sebastien.lange@syleam.fr>
#
#    This file is a part of payment_scheduled
#
#    payment_scheduled is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    payment_scheduled is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

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

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
