from odoo import models, fields


class Day(models.Model):
    _name = 'day'
    _description = ""

    max_attendies = fields.Integer('Aximum attendies per day', required=True)
    date = fields.Date('Date', required=True)

    camp_id = fields.Many2one(
        'camp', string="Camp", ondelete="set null")

    attendee_ids = fields.Many2many(
        'attendee', 'day_ids', string='Attendees')

    full = fields.Boolean(compute='_compute_full')

    def _compute_full(self):
        for day in self:
            day.full = day.max_attendies <= len(day.attendee_ids)
