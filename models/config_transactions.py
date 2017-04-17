# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
class transaction_achat_category(models.Model):
    _inherit = 'product.category'
    _name = "transactionconfig.category"


class transaction_achat_config(models.Model):
    _inherit = 'product.template'
    _name="transactioncofig.achat"
    #les tva applicable sur une transactions
    tax_ids = fields.Many2many('account.tax', 'transaction_achat_config_tva_default_rel',
                                   'transaction_achat_config_id', 'tax_id', string='TVA par défaut')
    purchase_ok = fields.Boolean('transaction d\'achat', default=True)
    sale_ok = fields.Boolean('transaction de vente',defaut=False)