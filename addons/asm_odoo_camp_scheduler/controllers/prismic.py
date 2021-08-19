from odoo import http
from odoo.http import request
import json
import time

import logging

_logger = logging.getLogger(__name__)


class Prismic(http.Controller):
    @http.route('/pga-manager/prismic', type='http', auth='none', cors='*', csrf='True')
    def prismic(self, **kw):
        result_size = 0
        results = []
        camps = request.env['camp'].sudo().search([])
        _logger.critical(camps)
        for camp in camps.read(['name', 'start_date', 'end_date', 'description', 'age_min', 'age_max']):
            _logger.critical(camp)
            camp_sku = {
                'id': str(camp['id']),
                'title': camp['name'],
                'description': str(camp['description']),
                'image_url': 'http://...',
                'last_update': int(time.time()),
                'blob': {
                    'sku': camp['id'],
                    'title': camp['name'],
                    'description': 'description of first item...',
                    'image_url': 'https://..'
                }
            }
            results.append(camp_sku)
            result_size += 1
        _logger.critical(results)
        result_json = {
            'results_size': result_size,
            'results': results
        }
        return json.dumps(result_json)
