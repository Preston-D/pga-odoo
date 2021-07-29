from odoo import models, fields, api
from datetime import timedelta

import logging

_logger = logging.getLogger(__name__)


class Camp(models.Model):
    _name = 'camp'
    _description = ""

    name = fields.Char('Name', required=True)
    start_date = fields.Date('Start Date', required=True)
    end_date = fields.Date('End Date', required=True)
    description = fields.Text('Description')
    age_min = fields.Integer('Minimum Age', required=True)
    age_max = fields.Integer('Maximum Age', required=True)

    location_id = fields.Many2one('location', string="Location", required=True)

    camp_type_id = fields.Many2one(
        'product.template', string="Camp Type", ondelete="set null")

    days_ids = fields.One2many('day', 'camp_id', string="Camps")

    @api.model
    def create(self, values):
        # create days
        delta = timedelta(days=1)
        date_index = fields.Date.from_string(values['start_date'])
        max_attendies = 2  # import this from the camp creatiion somehow later
        while date_index <= fields.Date.from_string(values['end_date']):
            _logger.critical(date_index)
            self.env['day'].sudo().create({
                'max_attendies': max_attendies,
                'date': date_index,
            })
            date_index += delta
        return super(Camp, self).create(values)

#     location = self.env['location'].search([('id', '=', 1)])
#     _logger.info(self.location_id)
#     values['name'] = "name placeholder"

#     # "{}, {} - {}".format(location['name'],self.start_date, self.end_date)


# extend the product template class from the inventory app (our app now depends on inventory (stock))
class ProductTemplate(models.Model):
    _inherit = 'product.template'

    camp_ids = fields.One2many('camp', 'camp_type_id', string="Camps",)
