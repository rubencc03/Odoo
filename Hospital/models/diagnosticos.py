# -*- coding: utf-8 -*-
from odoo import models, fields, api
from datetime import datetime
#Definimos el modelo de datos
class diagnosticos(models.Model):
    #nombre modelo
    _name = 'diagnosticos'
    #Descripcion
    _description = 'Espero que no tengas covid'
    
    _rec_name='veredicto'

    medicos = fields.Many2one('medicos', required=True, index=True)
    pacientes = fields.Many2one('pacientes', required=True, index=True)
    veredicto = fields.Text('Diagnostico del Medico' , required=True, index=True)

   





