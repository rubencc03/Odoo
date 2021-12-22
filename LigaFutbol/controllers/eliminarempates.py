# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json


#Clase del controlador web
class eliminarempates(http.Controller):
    @http.route('/ligafutbol/partido/eliminarempates', type='http', auth='none')
    def delete(self):
          #Obtenemos la referencia al modelo de Equipo
        partidos = request.env['liga.partido'].sudo().search([])
        
        #Generamos una lista con informacion que queremos sacar en JSON
        listaParticos=[]
        contador=0
        for partido in partidos:
            if(not partido.goles_casa == partido.goles_fuera):
                listaParticos.append(["Equipo Local:"+partido.equipo_casa.nombre, "Sus goles:"+ str(partido.goles_casa) ,
                 "Equipo Visitante: "+partido.equipo_fuera.nombre," Sus goles:"+str(partido.goles_fuera)])
            else:contador=contador+1

        #Convertimos la lista generada a JSON
        listaParticos.append(["Partidos empatados eliminados = " + str(contador)])
        json_result=json.dumps(listaParticos)

        return json_result
