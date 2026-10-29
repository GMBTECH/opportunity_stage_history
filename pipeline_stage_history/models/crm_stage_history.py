from odoo import fields, models

class CrmStageHistory(models.Model):
    _name = "crm.stage.history"
    _description = "CRM Stage Change History"
    _order = "changed_on desc, id desc"
    _rec_name = "lead_id"

    lead_id = fields.Many2one(
        comodel_name="crm.lead",
        string="Lead / Opportunity",
        required=True,
        index=True,
        ondelete="cascade",
    )
    previous_stage_id = fields.Many2one(
        comodel_name="crm.stage",
        string="Previous Stage",
        ondelete="set null",
    )
    new_stage_id = fields.Many2one(
        comodel_name="crm.stage",
        string="New Stage",
        ondelete="set null",
    )
    changed_by = fields.Many2one(
        comodel_name="res.users",
        string="Changed By",
        required=True,
        readonly=True,
        ondelete="restrict",
        default=lambda self: self.env.user,
    )
    changed_on = fields.Datetime(
        string="Changed On",
        required=True,
        readonly=True,
        default=fields.Datetime.now,
        index=True,
    )
