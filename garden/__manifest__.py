{
    'name': "Garden",
    'version': '1.0',
    'depends': ['base', 'mail', 'contacts'],
    'author': "Tewtawat C., Trinity Roots",
    'category': 'Tools',
    'description': """
    My Garden
    """,

    'data': [
        'security/garden_security.xml',
        'security/ir.model.access.csv',
        'views/plot_view.xml',
        'views/partner_form_view.xml',
        'wizard/plot_status_wizard.xml'
    ],

    'application': True,
}
