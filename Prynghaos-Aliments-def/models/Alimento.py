# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date, timedelta



class Alimento(models.Model):
    #Nombre  del modelo
    _name = 'alimento'
    #Queremos que ordenen los alimentos por nombre
    _order = 'fecha_caducar'
    #Aqui indicamos que si en otra vista muestran un alimento,lo que se mostrará será nombre
    _rec_name = 'nombre'


    #Field en el que el usuario introducirá el nombre del alimento
    nombre = fields.Char('Nombre Alimento', required=True, index=True)
    #Field donde el usuario pongra cuantos alimentos han sido donado de x tipo(3 lechugas)
    num_alimento= fields.Integer('Numero de Alimentos donados', required=True, index=True)
    #El nombre de la persona que lo ha donado
    donador = fields.Char('Nombre Donador', required=True, index=True)
    #Creamos un fiels.Selecction que nos servirá para organizar una vista kanban donde mostraremos la localización de los alimentos,por defecto
    #Están en el almacen
    categoria_id = fields.Selection(
        [('1', 'En almacen'),
         ('2', 'Enviado'),
         ('3', 'Entregada'),
         ('4','Caducado')],
        'Estado', default="1")

    #Creamos un field `pará ver cuando caducan los alimentos
    fecha_caducar = fields.Date('Fecha Caducación')
    
    #Creamos una función la cual será llamada cada minuto
    def actualizar(self):
        #Le decimos que el modelo con el que trabajamos será alimento
        modelo=self.env['alimento'].search([])
        #Recorremos todos los alimentos
        for record in modelo:
            #Si la fecha del alimento de caducidad es antes que hoy
            if(record.fecha_caducar<fields.Date.today()):
                #Esta caducado así que le decimos que su fiels.Selection deberia ser caducado para que se actualice en la vista Kanban
                record.categoria_id='4'


    #ESto es por así decirlo una función que esta escuchando en el modelo
    @api.constrains('fecha_caducar')
    def _check_caducado2(self):
        #Recorre también todos sus campos de alimento
        for record in self:
            #Y si intenta guardar un alimento caducado
            if (record.fecha_caducar < fields.Date.today()):
                #Muestra un  aviso y no lo permite
                raise models.ValidationError('No me entregues cosas caducadas,ratilla')
