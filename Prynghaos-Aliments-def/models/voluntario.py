# -*- coding: utf-8 -*-
from datetime import timedelta

from odoo import models, fields, api
from odoo.exceptions import ValidationError



#Definimos modelo Voluntario, que almacenara información de cada voluntario
class voluntario(models.Model):

    #Nombre y descripcion del modelo
    _name = 'voluntario'
    _description = 'Modelo par almacenar voluntarios'

    #Parametros de ordenacion por defecto
    _order = 'nombre'

    #Cuando en una vista superior muestren un voluntario se verá el nombre del voluntario
    _rec_name = 'nombre'


    num_voluntario= fields.Integer("Numero de Voluntario")
    #Atributo nombre
    nombre = fields.Char('Nombre Voluntario', required=True, index=True)
    apellidos = fields.Char('Apellidos Voluntario', required=True, index=True)
    #Imagen (indicaremos en la vista como mostrarlo)
    foto = fields.Image('Foto voluntario',max_width=100,max_height=100)

    #Imagen (indicaremos en la vista como mostrarlo)
    barcode_carnet = fields.Image('Barcode carnet',max_width=100,max_height=100)

    #Constraints de SQL del modelo
    _sql_constraints = [
        ('voluntario_uniq', 'UNIQUE (num_voluntario)', 'El numero de Voluntario debe ser unico.')
    ]
