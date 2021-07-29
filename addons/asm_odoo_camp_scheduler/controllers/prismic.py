from odoo import http
from odoo.http import request
import json

import logging

_logger = logging.getLogger(__name__)


class Prismic(http.Controller):
    @http.route('/pga-manager/prismic', type='json', auth='none', cors='*', csrf="False")
    def prismic(self, **kw):
        result_json = {
            'results_size': 144,
            'results': [
                {
                    "id": "my_item_id",
                    "title": "Item Title",
                    "description": "Description of the item.",
                    "image_url": "http://...",
                    "last_update": 1509364426938,
                    "blob": {
                          "sku": "1",
                          "title": "first item",
                          "description": "description of first item...",
                          "image_url": "https://.."
                    }
                },
            ]
        }
        return json.dumps(result_json)
