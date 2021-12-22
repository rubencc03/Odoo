# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime

class profesores(models.Model):
    _name = 'alumnos'
    _description = 'alumnos'
    _rec_name="nombre"

    nombre = fields.Char('Nombre Alumno')
    apellido = fields.Char('Apellido Alumno')

    telefono = fields.Integer('Telefono Alumno')

    dni = fields.Char('DNI Alumno')

 
    sql_constraints = [('alumno_uniq', 'UNIQUE (dni)', 'El numero DNI del alumno debe ser Unico.')]




    



