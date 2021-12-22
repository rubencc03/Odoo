# -*- coding: utf-8 -*-
from odoo import models, fields, api
from datetime import datetime
#Definimos el modelo de datos
class pacientes(models.Model):
    #Nombre y descripcion del modelo de datos
    _name = 'pacientes'
    _description = 'Pacientes problematicos'

    _rec_name="name"


    name = fields.Char("Nombre del Paciente", required=True, index=True)
    apellido = fields.Char("Apellidos del Paciente", required=True, index=True)
    dni = fields.Char("DNI del Paciente", required=True, index=True)
    sintomas = fields.Text("Sintomas del Paciente", required=True, index=True)


    





