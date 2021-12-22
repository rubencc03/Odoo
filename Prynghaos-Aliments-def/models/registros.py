# -*- coding: utf-8 -*-

from odoo import models, fields, api

#Definimos el modelo de los registros
class registros(models.Model):
    _name = 'registros'
    _description = 'Modelo de la lista de tareas'

    _rec_name="info"
   
    info = fields.Char('Información registro')
    
    #Campo voluntario del registro,en un registro un solo voluntario recoge la comida  y un voluntario puede estar en muchos registros
    voluntarios = fields.Many2one('voluntario')
    #Campo alimento de los registros,en un registro pueden haber muchos alimentos y un alimento puede estar en muchos registros
    alimentos = fields.Many2many('alimento')
    #Numero identificativo del registro
    num_registro= fields.Integer("Numero de Registro")

    #Sentencia encargada de que no hayan dos registros con el mismo identificador,si no ,no los podemos identificar
    _sql_constraints = [
        ('registros_uniq', 'UNIQUE (num_registro)', 'El numero del Registro debe ser unico.')
    ]
    


    