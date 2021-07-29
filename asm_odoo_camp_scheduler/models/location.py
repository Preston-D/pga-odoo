from odoo import models, fields


class Location(models.Model):
    _name = 'location'
    _description = ""

    name = fields.Char('Name', required=True)
    state = fields.Char('State', required=True)
    address = fields.Char('Address', required=True)

    camp_ids = fields.One2many('camp', 'location_id', string="Camps")
