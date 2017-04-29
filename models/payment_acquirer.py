# -*- coding: utf-8 -*-
# Copyright 2016 SYLEAM Info Services
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields


class PaymentAcquirer(models.Model):
    _inherit = 'payment.acquirer'

    payment_term_id = fields.Many2one('account.payment.term', string='Payment Term')

