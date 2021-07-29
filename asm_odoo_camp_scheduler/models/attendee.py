from odoo import models, fields


class Attendee(models.Model):
    _name = 'attendee'

    name = fields.Char('Attendee Name', required=True)
    age = fields.Integer('Attendee Age', required=True)

    day_ids = fields.Many2many(
        'day', 'attendee_ids', string='Enrolled Day')

    # guardian = fields.Many2one('TBD', string="Attendee's Guardian")
