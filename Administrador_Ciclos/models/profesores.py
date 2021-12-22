# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime

class profesores(models.Model):
    _name = 'profesores'
    _description = 'profesores'
    _rec_name="nombre"

    nombre = fields.Char('Nombre Profesor')
    apellido = fields.Char('Apellido Profesor')

    telefono = fields.Integer('Telefono Profesor')

    dni = fields.Char('DNI profesor')

 
    sql_constraints = [('profesores_uniq', 'UNIQUE (dni)', 'El numero DNI del profesor debe ser Unico.')]




    



