# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime

class modulos(models.Model):
    _name = 'modulos'
    _description = 'modulos'
    _rec_name="nombre"
    
    nombre = fields.Char('Nombre Modulo')
    profesores = fields.Many2many('profesores')
    alumnos = fields.Many2many('alumnos')
    



