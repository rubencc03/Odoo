# -*- coding: utf-8 -*-
from odoo import models, fields, api
from datetime import datetime
#Definimos el modelo de datos
class medicos(models.Model):
    #Nombre y descripcion del modelo de datos
    _name = 'medicos'
    _description = 'Vivan los medicos'

    _rec_name="name"

    num_medico= fields.Integer("Numero de Medico", required=True, index=True)

    name = fields.Char("Nombre del Medico", required=True, index=True)
    apellido = fields.Char("Apellidos del medico", required=True, index=True)
   
   





