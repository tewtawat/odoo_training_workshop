from odoo import models, fields


class Plot(models.Model):
    _name = 'plot'
    _decription = 'Garden plot'

    name = fields.Char(string='Plot number')

    is_organic = fields.Boolean(
        string='Is Organic Garden',
        default=False
    )

    cycle_count = fields.Integer(
        string="Cycle",
        readonly=True,
        default=0,
    )

    slot_count = fields.Integer(
        string="Slot Count",
        default=0,
    )
