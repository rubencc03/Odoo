# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime

class ciclos(models.Model):
    _name = 'ciclos'
    _description = 'ciclos formativos'
    _rec_name="instituto"

    modulos = fields.Many2many('modulos')
    instituto = fields.Char("Instituto")
    nombre = fields.Char("Nombre Ciclo")

    



