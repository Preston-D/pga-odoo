from odoo import http
from odoo.http import request

import logging

_logger = logging.getLogger(__name__)


class Main(http.Controller):
    @http.route('/pga-manager/camps/json', type='json', auth='none', cors='*', csrf="False")
    def camps_json(self):
        camps = request.env['camp'].sudo().search([])
        return camps.read(['name', 'start_date', 'end_date', 'description', 'age_min', 'age_max'])

    @http.route('/pga-manager/locations/json', type='json', auth='none', cors='*', csrf="False")
    def locations_json(self):
        locations = request.env['location'].sudo().search([])
        return locations.read(['name', 'state', 'address', 'camp_ids'])

    @http.route('/pga-manager/camp/json', type='json', auth='none', cors='*', csrf="False")
    def camp_json(self, **kw):
        _logger.critical(kw)
        # to use pass the structure {'id': 'a_single_camp_id'} as a request parameter
        camps = request.env['camp'].sudo().search([('id', '=', kw['id'])])
        return camps.read(['name', 'start_date', 'end_date', 'description', 'age_min', 'age_max'])

    @http.route('/pga-manager/add-attendee/json', type='json', auth='none', cors='*', csrf="False")
    def add_attendee(self, **kw):
        _logger.critical(kw)
        attendee_id = kw['attendee_id']
        day_ids = kw['day_ids']
        attendee = request.env['attendee'].sudo().search(
            [('id', '=', attendee_id)])

        days = request.env['day'].sudo().search(
            [('id', 'in', day_ids)])

        for day in days:
            if not day['full']:
                day.write({'attendee_ids': [(4, attendee_id)]})
                attendee.write({'day_ids': [(4, day['id'])]})
        return True

        _logger.critical(attendee)
