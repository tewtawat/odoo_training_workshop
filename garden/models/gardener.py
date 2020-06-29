from odoo import models, fields


class Gardener(models.Model):
    _name = 'gardener'
    _description = 'Someone who works in a garden'

    name = fields.Char(string='Gardener Name')

    plot_ids = Many2many(
        'plot',
        string='Plot'
    )
