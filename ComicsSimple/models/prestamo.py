# -*- coding: utf-8 -*-
from datetime import timedelta

from odoo import models, fields, api
from odoo.exceptions import ValidationError



#Definimos modelo Liga Equipo, que almacenara información de cada equipo
class prestamo(models.Model):

    #Nombre y descripcion del modelo
    _name = 'prestamo'

    _description = 'Modelo para organizar prestamos'

    #Parametros de ordenacion por defecto
    _order = 'socios'

    _rec_name = 'socios'

    #Atributo nombre
    socios = fields.Many2one('socio')
    comics = fields.Many2one('biblioteca.comic', required=True, index=True)
    fecha_salida = fields.Date('Fecha Prestamo Comic', required=True, index=True)
    fecha_entrada= fields.Date('Fecha Vuelta Comic', required=True, index=True)

    


    @api.constrains('fecha_salida')
    def _check_caducado(self):
        for record in self:
            
            if (record.fecha_salida > fields.Date.today()):
                raise models.ValidationError('La fecha de prestamo no puede ser posterior a hoy,bobo')


    @api.constrains('fecha_entrada')
    def _check_caducado2(self):
        for record in self:

            if (record.fecha_entrada < fields.Date.today()):
                raise models.ValidationError('Me lo pides hoy para devolvermelo ayer? Que velocidad')

                
                
            
                



