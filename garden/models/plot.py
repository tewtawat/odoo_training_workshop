from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Plot(models.Model):
    _name = 'plot'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Garden plot'

    _sql_constraints = [
        ('name_unique',
         'UNIQUE(name)',
         "The plot number must be unique"),
    ]

    name = fields.Char(
        string='Plot number',
        track_visibility='onchange',
    )

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
        compute='_compute_slot_count',
        inverse='_inverse_slot',
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

    @api.depends('slot_ids')
    def _compute_slot_count(self):
        for rec in self:
            rec.slot_count = len(rec.slot_ids.filtered('is_empty'))

    def _inverse_slot(self):
        slot_id = self.env['plot.slot']
        for rec in self:
            slot_count = len(rec.slot_ids.filtered('is_empty'))
            if rec.slot_count > slot_count:
                rec.slot_ids = [
                    slot_id.create({'name': 'n/a'}).id
                    for i in range(rec.slot_count - slot_count)
                ]

    @api.constrains('name')
    def _check_name(self):
        for rec in self:
            if rec.name and rec.name[:1] in ('A', 'E', 'I', 'O', 'U'):
                raise ValidationError(
                    "Plot Number can't not start with vowels."
                )
