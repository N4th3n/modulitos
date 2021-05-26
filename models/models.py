# -*- coding: utf-8 -*-

from odoo import models, fields, api

class second(models.Model):
    _name = 'segundo.second'
    _description = 'mi segundo intento'


    name = fields.Char("Nombre", required=True)
    description = fields.Text("Descripcion")
    postcode = fields.Char("Postcode")
    date_availability = fields.Date("Fecha de Disponibilidad")
    expected_price = fields.Float("Precio Esperado")
    selling_price = fields.Float("Precio de Venta")
    bedrooms = fields.Integer("Cuartos")
    living_area = fields.Integer("Sala de Estar")
    facedes = fields.Integer("Fachada")
    garage = fields.Boolean("Garage")
    garden = fields.Boolean("Jardin")
    garden_area = fields.Integer("Area del Jardin")
    garden_orientation = fields.Selection(selection=[("Izquierda", "Izq"), ("Derecha", "Der")])



# class second(models.Model):
#     _name = 'second.second'
#     _description = 'second.second'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
