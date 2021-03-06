# -*- coding: utf-8 -*-
{
    'name': "felix1.de Backend",

    'summary': """
        Migration der Access Datenbank""",

    'description': """
        Dieses Modul migriert die Tabellen der Access Datenbank.
        Auch Aenderungen oder Anpassungen an den Tabellen in Access koennen 
        hiermit fortlaufend aktuallisiert werden.
   """,

    'author': "hiyacoding ltd.",
    'website': "http://www.hiyacoding.co.uk",
    'icon': "/felix1de_backend/static/description/backend.png",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'felix1',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base','mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/backend.xml',
        'views/abrechnungszeitraeume.xml',
        'views/auftraege.xml',
        'views/berater.xml',
        'views/branchen.xml',
        'views/mandanten.xml',
        'views/kontakte.xml',
        'views/checklistentypen.xml',
        'views/checklistenvorlagen.xml'


       # 'views/templates.xml',
        
    ],
    # only loaded in demonstration mode
    'demo': [
    'demo/demo.xml',
    ],
    'application': True,
    'installable': True,
    'auto_install': True
}