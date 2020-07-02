from odoo import fields, models, api


class PlotStatusWizard(models.TransientModel):
    _name = "plot.status.wizard"
    _description = "Set plot status"

    plot_id = fields.Many2one(
        comodel_name='plot',
        string="Plot"
    )

    wiz_slot_ids = fields.One2many(
        comodel_name='plot.slot.wizard',
        inverse_name="wiz_plot_id",
        string="Slot Wizard"
    )

    def button_setstatus(self):
        return True


class PlotSlotWizard(models.TransientModel):
    _name = "plot.slot.wizard"
    _description = "Set plot slot"

    wiz_plot_id = fields.Many2one(
        comodel_name='plot.status.wizard',
        string="Plot Wizard"
    )

    slot_id = fields.Many2one(
        comodel_name='plot.slot',
        string="Plot Slot Wizard"
    )

    is_blue = fields.Boolean(
        related='slot_id.is_blue',
        readonly=False,
        string='Blue',
    )

    is_yellow = fields.Boolean(
        related='slot_id.is_yellow',
        readonly=False,
        string='Yellow',
    )
