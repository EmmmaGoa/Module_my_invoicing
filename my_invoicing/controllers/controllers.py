# -*- coding: utf-8 -*-
# from odoo import http


# class MyInvoicing(http.Controller):
#     @http.route('/my_invoicing/my_invoicing', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/my_invoicing/my_invoicing/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('my_invoicing.listing', {
#             'root': '/my_invoicing/my_invoicing',
#             'objects': http.request.env['my_invoicing.my_invoicing'].search([]),
#         })

#     @http.route('/my_invoicing/my_invoicing/objects/<model("my_invoicing.my_invoicing"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('my_invoicing.object', {
#             'object': obj
#         })
