from odoo import models, fields


class Gardener(models.Model):
    _inherit = 'res.partner'
    _description = 'Someone who works in a garden'

    plot_ids = fields.Many2many(
        'plot',
        'plot_partner_rel',
        'partner_id',
        'plot_id',
        string='Plot'
    )

    is_gardener = fields.Boolean(
        string='Is Gardener'
    )
