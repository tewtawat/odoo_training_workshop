from odoo import models, fields, api


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
    )

    is_yellow = fields.Boolean(
        string='Yellow',
    )

    is_green = fields.Boolean(
        compute='_compute_is_green',
        string='Green',
        store=True
    )

    @api.depends('is_yellow', 'is_blue')
    def _compute_is_green(self):
        for rec in self:
            rec.is_green = rec.is_blue and rec.is_yellow
