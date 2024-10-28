
# -*- coding: utf-8 -*-
###############################################################################
#
#    jeffery CHEN fan<jeffery9@gmail.com>
#
#    Copyright (c) All rights reserved:
#        (c) 2017  TM_FULLNAME
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses
#
#    Odoo and OpenERP is trademark of Odoo S.A.
#
###############################################################################
{
    'name': 'Hola Mundo',
    'summary': 'Este es mi hola mundo',
    'version': '1.0',

    'description': """
Este es mi primer modulo
==============================================


    """,

    'author': 'Matias',
    'maintainer': 'Matias',
    'contributors': ['MAtias <matiasjosafatv@gmail.com>'],

    'website': 'http://www.github.com/matiasjosafatv',

    'license': 'AGPL-3',
    'category': 'Capacitacion',

    'depends': [
        'base'
    ],
    'external_dependencies': {
        'python': [
        ],
    },
    'data': [
        'security/ir.model.access.csv',

        'data/automovil_data.xml',
        'views/automovil_views.xml',
        'views/automovil_color_views.xml',

        'views/automovil_modelo_views.xml',
        'views/automovil_brand_views.xml',
        'views/automovil_menu_views.xml',

    ],
    'demo': [
    ],
    'js': [
    ],
    'css': [
    ],
    'qweb': [
    ],
    'images': [
    ],
    'test': [
    ],

    'installable': True
}
