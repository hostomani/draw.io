# -*- coding: utf-8 -*-
# from odoo import http


# class DemoDraw(http.Controller):
#     @http.route('/demo_draw/demo_draw', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/demo_draw/demo_draw/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('demo_draw.listing', {
#             'root': '/demo_draw/demo_draw',
#             'objects': http.request.env['demo_draw.demo_draw'].search([]),
#         })

#     @http.route('/demo_draw/demo_draw/objects/<model("demo_draw.demo_draw"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('demo_draw.object', {
#             'object': obj
#         })

