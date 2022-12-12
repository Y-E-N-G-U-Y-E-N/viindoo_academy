# -*- coding: utf-8 -*-
# from odoo import http


# class ViindooAcademy(http.Controller):
#     @http.route('/viindoo_academy/viindoo_academy', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/viindoo_academy/viindoo_academy/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('viindoo_academy.listing', {
#             'root': '/viindoo_academy/viindoo_academy',
#             'objects': http.request.env['viindoo_academy.viindoo_academy'].search([]),
#         })

#     @http.route('/viindoo_academy/viindoo_academy/objects/<model("viindoo_academy.viindoo_academy"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('viindoo_academy.object', {
#             'object': obj
#         })
