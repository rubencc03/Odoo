# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from PIL import Image
import random
#Necesario para trabajar con base64
import base64
#Biblioteca para guardar la imagen en memoria antes de pasarla a base64


# Clase del controlador web
class GenerarImg(http.Controller):
    
    '''
    Comprobar con url -> http://localhost:8069/generador/1
    '''

    @http.route('/generador/<codigo>', auth='public', cors='*', type='http')
    def crearImg(self, codigo, **kw):
       
        testImage = Image.new("RGB", (600,600), (255,255,255))
        pixel = testImage.load()

        for x in range(600):
             for y in range(600):
                red = random.randrange(0,255)
                blue = random.randrange(0,255)
                green = random.randrange(0,255)
                pixel[x,y]=(red,blue,green)

        testImage.save("xd.jpg")

        with open("xd.jpg", "rb") as img_file:
             xd= base64.b64encode(img_file.read()).decode('utf-8')

        return '<div><img src="data:image/png;base64,'+str(xd)+'"/></div>'