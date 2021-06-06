# -*- coding: utf-8 -*-
# from odoo import http


# class Odtry(http.Controller):
#     @http.route('/odtry/odtry/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odtry/odtry/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odtry.listing', {
#             'root': '/odtry/odtry',
#             'objects': http.request.env['odtry.odtry'].search([]),
#         })

#     @http.route('/odtry/odtry/objects/<model("odtry.odtry"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odtry.object', {
#             'object': obj
#         })
