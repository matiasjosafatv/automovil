
# -*- coding: utf-8 -*-
###############################################################################
#    License, author and contributors information in:                         #
#    __manifest__.py file at the root folder of this module.                  #
###############################################################################

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError


class Automovil(models.Model):
    _name = 'automovil'
    _description = 'Automobile Catalog'

    _rec_name = 'name'
    _order = 'name ASC'

    name = fields.Char(
        string='Name',
        required=True,
        default=lambda self: _('New'),
        copy=False
    )


    tires = fields.Integer(string='Tires Number',default = 4, help = """Normalmente los carros van con 4 llantas
                           indique cuantas llantas sin contar la llanta de refaccion""" ,required=True)



    color = fields.Selection(string='Color', required=True,
        selection=[
        ('white', 'White'),
        ('blue', 'Blue'),
        ('red', 'Red'),
        ('orange', 'Orange')
        ],help="""Select Your Color Car
        It amazing.
        Ok?
        """)

    air = fields.Boolean(string='A/C',default=False,help="""Check Ture if your automovil has Air Conditioner
                         """)


    tank_combustible = fields.Float(string='Combustible')

    purchase_date = fields.Date(string='Purchase Date')
    change_driver_date = fields.Datetime('Driver Change')

    driver = fields.Char(string='')

    description = fields.Text(string='')


    automovil_color_id = fields.Many2one('automovil.color', string='Automovil Color')

    year = fields.Char(string='Year')


    engine_number = fields.Char(string='Engine Number')

    automovil_modelo_id = fields.Many2one('automovil.modelo',string='Automovil Modelo')

    automovil_brand_id = fields.Many2one('automovil.brand',string='Automovil Brand')

    foto = fields.Binary(string='')

    signature = fields.Binary(string='')

    contract = fields.Binary(string='')

    email = fields.Char(string='Email Car Owner',index = True)
