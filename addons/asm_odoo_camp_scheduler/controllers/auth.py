from odoo import http
from odoo.http import request
import json
import time

import logging

_logger = logging.getLogger(__name__)


class Auth(http.Controller):
    @http.route('/auth/csrf', type='http', auth='public', website=True, sitemap=False, csrf=False)
    def auth_csrf(self, *args, **kw):
        token = request.csrf_token()
        _logger.critical(token)
        return token
        
