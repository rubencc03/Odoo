import telebot # Importamos las librería
import requests
import json

bot = telebot.TeleBot("5049617253:AAEQK--OfT18eidw6e2VCARhsyJd7xXcfcA")  #Creamos nuestra instancia "bot" a partir de ese TOKEN


#Si el bot detecta el comando Consultar
@bot.message_handler(commands=['Consultar'])
#Ejecuta esta función
def send_user(message):
    lista=[]
    lista = message.text.split() #Creamos una lista para separar el comando de la información adicional del mensaje

    url="http://localhost:8069/gestion/apirest/socio?data={\"num_socio\":\""+ str(lista[1])+"\"}" #Incluimos el numero que nos ha pasado el usuario en la url

    api = requests.get(url) #Cargamos la informaición de la url
    json_data= json.loads(api.content) #Cargamos la informacion en un json

    bot.reply_to(message, "El usuario que querias consultar es: " + str(json_data) ) #Devolvemos el json convertido a string 




#Si el bot detecta el comando Borrar
@bot.message_handler(commands=['Borrar'])
#Ejecuta esta función
def delete_user(message):
    lista=[]
    lista = message.text.split() #Creamos una lista para separar el comando de la información adicional del mensaje

    url="http://localhost:8069/gestion/apirest/socio?data={\"num_socio\":\""+ str(lista[1])+"\"}" #Incluimos el numero que nos ha pasado el usuario en la url

    api = requests.delete(url,timeout=5) #Borramos el usuario 

    bot.reply_to(message, "El usuario "+lista[1]+" ha sido borrado correctamente"  ) #Devolvemos mensaje informativo
    
























#Si el bot detecta el comando Crear
@bot.message_handler(commands=['Crear'])
#Ejecuta esta función
def delete_user(message):
    lista=[]
    lista = message.text.split() #Creamos una lista para separar el comando de la información adicional del mensaje

    url="http://localhost:8069/gestion/apirest/socio?data={\"num_socio\":\""+str(lista[1])+"\", \"nombre\":\""+lista[2]+"\",\"apellidos\":\""+lista[3]+"\"}"    

    api = requests.post(url,timeout=5) #Borramos el usuario 

    bot.reply_to(message, "El usuario "+lista[1]+ " " + lista[2] + " " + lista[3]+ " ha sido creado correctamente"  ) #Devolvemos mensaje informativo


#Si el bot detecta el comando Modificar
@bot.message_handler(commands=['Modificar'])
#Ejecuta esta función
def delete_user(message):
    lista=[]
    lista = message.text.split() #Creamos una lista para separar el comando de la información adicional del mensaje

    url="http://localhost:8069/gestion/apirest/socio?data={\"num_socio\":\""+str(lista[1])+"\", \"nombre\":\""+lista[2]+"\",\"apellidos\":\""+lista[3]+"\"}"  #Modifica por num_socio   

    api = requests.put(url,timeout=5) #Borramos el usuario 

    bot.reply_to(message, "El usuario "+lista[1]+ " " + lista[2] + " " + lista[3]+ " ha sido creado modificado"  ) #Devolvemos mensaje informativo




bot.polling()
