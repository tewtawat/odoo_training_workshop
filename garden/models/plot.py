from odoo import models, fields


class Plot(models.Model):
    _name = 'plot'
    _description = 'Garden plot'

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

    slot_ids = fields.One2many(
        comodel_name="plot.slot",
        inverse_name="plot_id",
        string="Slot",
    )

    gardener_ids = fields.Many2many(
        comodel_name='gardener',
        relation='plot_gardener_rel',
        column1='plot_id',
        column2='gardener_id',
        string='Gardener'
    )
