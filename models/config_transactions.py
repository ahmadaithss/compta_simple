# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
class transaction_achat_category(models.Model):
    _inherit = 'product.category'
    _name = "transaction.config.category"
    compte_debit = fields.Many2one('account.account',
                                   string="compte de debit",
                                   required=True,
                                   help="le compte de débit qui sera utilisé lors de la génération de l'écriture comptable de la transaction.")
    parent_id = fields.Many2one('transaction.config.category', 'Parent Category', index=True, ondelete='cascade')
    child_id = fields.One2many('transaction.config.category', 'parent_id', 'Child Categories')

class transaction_achat_config(models.Model):
    _inherit = 'product.template'
    _name="transaction.config.achat"
    #les tva applicable sur une transactions
    tax_ids = fields.Many2many('account.tax', 'transaction_achat_config_tva_default_rel',
                                   'transaction_achat_config_id', 'tax_id', string='TVA par défaut',
                                    domain=[('type_tax_use', '=', 'purchase')],required=True)

    #définir la valeur par défaut a true parceque il s'agit d'un achat
    purchase_ok = fields.Boolean('transaction d\'achat', default=True)

    # définir la valeur par défaut a false il ne peut pas etre un achat parceque a ce stade on traite seulment les achats
    sale_ok = fields.Boolean('transaction de vente',defaut=False)

    #le compte de debit de la transaction
    compte_debit=fields.Many2one('account.account',
        string="compte de debit",
        required=True,
        help="le compte de débit qui sera utilisé lors de la génération de l'écriture comptable de la transaction.")

    #les categories des transactions
    categorie=fields.Many2one(
        'transaction.config.category', 'catégorie',
        required=True, help="Selectionner la categorie de la transaction")