from odoo import fields, models


class CrmLead(models.Model):
    _inherit = "crm.lead"

    stage_history_ids = fields.One2many(
        comodel_name="crm.stage.history",
        inverse_name="lead_id",
        string="Stage History",
        copy=False,
        readonly=True,
    )

    def write(self, vals):
        if "stage_id" not in vals or not self:
            return super().write(vals)

        target_stage_id = vals["stage_id"]

        previous_stages = {
            lead.id: lead.stage_id.id or False
            for lead in self
            if (lead.stage_id.id or False) != (target_stage_id or False)
        }

        result = super().write(vals)

        if previous_stages:
            changed_on = fields.Datetime.now()

            history_vals_list = [
                {
                    "lead_id": lead.id,
                    "previous_stage_id": previous_stage_id,
                    "new_stage_id": lead.stage_id.id or False,
                    "changed_by": self.env.uid,
                    "changed_on": changed_on,
                }
                for lead in self
                if (lead.id in previous_stages)
                for previous_stage_id in [previous_stages[lead.id]]
            ]

            self.env["crm.stage.history"].sudo().create(
                history_vals_list
            )

        return result
