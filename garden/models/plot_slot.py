from odoo import models, fields


class Slot(models.Model):
    _name = 'plot.slot'
    _description = 'Slot in plot\'s garden'

    name = fields.Char(string='Slot number')

    is_empty = fields.Boolean(
        string='Is Empty?',
        default=True
    )

    date_expire = fields.Date(
        string="Expire Date",
        readonly=True,
    )

    plot_id = fields.Many2one(
        comodel_name='plot',
        string="Plot"
    )

    plot_name = fields.Char(
        related='plot_id.name',
        string='Plot number'
    )

    is_blue = fields.Boolean(
        string='Blue',
        default=True
    )

    is_yellow = fields.Boolean(
        string='Yellow',
        default=True
    )

    is_green = fields.Boolean(
        string='Green',
        default=True
    )