# -*- coding: utf-8 -*-
from odoo import http


class DscBrandmodule(http.Controller):
    @http.route('/dsc_brandmodule/dsc_brandmodule/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/dsc_brandmodule/dsc_brandmodule/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('dsc_brandmodule.listing', {
            'root': '/dsc_brandmodule/dsc_brandmodule',
            'objects': http.request.env['dsc_brandmodule.dsc_brandmodule'].search([]),
        })

    @http.route('/dsc_brandmodule/dsc_brandmodule/objects/<model("dsc_brandmodule.dsc_brandmodule"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('dsc_brandmodule.object', {
            'object': obj
        })
