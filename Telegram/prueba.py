import telebot # Importamos las librería
import requests
import json




num=3
num2="Sergi"
num3="Garcia"
aver="http://localhost:8069/gestion/apirest/socio?data={\"num_socio\":\""+str(num)+"\", \"nombre\":\""+num2+"\",\"apellidos\":\""+num3+"\"}"

api = requests.put(aver,timeout=5) #Hacemos el request a la web para obtener toda la información
print(api)
print("xd")












#params = {"num_socio":"3", "nombre":"Sergi","apellidos":"Garcia"} 
#response = requests.post('http://pythonscraping.com/pages/processing.php', data = params)

    

