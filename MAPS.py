import urllib.parse, requests, json, time,msvcrt #importar librerias

main_api = "https://www.mapquestapi.com/directions/v2/route?" # url para ver las rutas
key = "aj6Aaq3npYUQY4vx1jmn89xlzpy8ohBQ"  # clave de la API de MapQuest

orig = input("Ingrese la ubicación de origen: ")  # Solicitar origen al usuario
dest = input("Ingrese la ubicación de destino: ")  # Solicitar destino al usuario

url = main_api + urllib.parse.urlencode({"key": key, "from": orig, "to": dest, "locale": "es_ES"}) #crea la solicitud
json_data = requests.get(url).json() #realiza una solicitud get

# Tiempo de viaje
tiempo = json_data["route"]["formattedTime"] # Obtiene el tiempo de viaje
horas, minutos, segundos = map(int, tiempo.split(":"))  # Convertir el tiempo a horas, minutos y segundos

# Kilómetros
distancia = json_data["route"]["distance"]  # obtiene distancia
distancia_km = round(distancia * 1.60934, 2)  # Conversión de millas a kilómetros y solo muestra 2 decimales

print("Instrucciones de viaje:") #muestra las intrucciones obtenidas
for leg in json_data["route"]["legs"]:
    for maneuver in leg["maneuvers"]:
        narrative = maneuver["narrative"]
        linea = narrative.split(". ") #muestra la narrativa de dos lineas a la vez
        for i in range(0, len(linea), 2):
            linea1 = linea[i]
            linea2 = linea[i + 1] if i + 1 < len(linea) else ""
            print(linea1)
            print(linea2)
            if msvcrt.kbhit(): #verifica que se presione la tecla s
                key = msvcrt.getch().decode()
                if key == 's': #termina el codigo y muestra un mensaje
                    print("Se detuvo el programa con exito.")
                    exit(0)
            time.sleep(2) #tiempo de espera para mostrar las lineas

print(f"\nDistancia: {distancia_km} km")  # Imprimir kilómetros
print(f"Duración del viaje: {horas} horas, {minutos} minutos, {segundos} segundos")  # Mostrar tiempo de viaje