# -*- coding: utf-8 -*-
# from odoo import http


# class ViinVipAcademy(http.Controller):
#     @http.route('/viin_vip_academy/viin_vip_academy', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/viin_vip_academy/viin_vip_academy/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('viin_vip_academy.listing', {
#             'root': '/viin_vip_academy/viin_vip_academy',
#             'objects': http.request.env['viin_vip_academy.viin_vip_academy'].search([]),
#         })

#     @http.route('/viin_vip_academy/viin_vip_academy/objects/<model("viin_vip_academy.viin_vip_academy"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('viin_vip_academy.object', {
#             'object': obj
#         })
