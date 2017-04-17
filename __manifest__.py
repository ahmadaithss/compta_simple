# -*- coding: utf-8 -*-
{
    'name': "Comptabilité simplifié",

    'summary': """Générer des écritures comptables a partir des données simple""",

    'description': """
        le module comptabilité simplifié gére :
        Génération de différents écritures comptable a partir des données simple:
        Ce module gére:
        -factures d'achat,vente,immobilisation
        -écriture d'abonnement: loyer,salaires,mouvement de fond
        ---
        -récuperer le journal de Banque (rapprochement bancaire )
        ---
    """,

    'author': "AgilOrg",
    'website': "http://www.agilorg.com/",
    'category': 'Accounting & Finance',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account'],

    # always loaded
    'data': [
        'views/transaction_achat_view.xml',
        'views/simple_compta_menuitem.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
