{
    'name': "Garden",
    'version': '1.0',
    'depends': ['base', 'mail'],
    'author': "Tewtawat C., Trinity Roots",
    'category': 'Tools',
    'description': """
    My Garden
    """,

    'data': [
        'security/garden_security.xml',
        'security/ir.model.access.csv',
        'views/plot_view.xml',
    ],

    'application': True,
}
