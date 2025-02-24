# Importación de librerías necesarias
import network  # Manejo de la conexión WiFi en la Raspberry Pi Pico W
import urequests  # Permite realizar peticiones HTTP para enviar datos a ThingSpeak
from machine import ADC, Pin  # Manejo de pines y convertidores analógico-digitales (ADC)
import time  # Para manejar pausas y tiempos de espera

# 🔹 CONFIGURACIÓN WiFi
SSID = "Colocar_SSID_DEL_WIFI"  # Nombre de la red WiFi
PASSWORD = "Contraseña_del_wifi"  # Contraseña de la red WiFi

# 🔹 CONFIGURACIÓN THINGSPEAK
API_KEY = "639WYS3QCL49XPO0"  # API Key de escritura para enviar datos a ThingSpeak
URL = "https://api.thingspeak.com/update"  # URL de la API de ThingSpeak

# 🔹 Configurar el LED interno de la Raspberry Pi Pico W
led = Pin("LED", Pin.OUT)  # Configuración del LED integrado como salida

# 🔹 Conectar a WiFi
wlan = network.WLAN(network.STA_IF)  # Se crea un objeto para manejar la conexión WiFi en modo estación
wlan.active(True)  # Se activa el adaptador WiFi
wlan.connect(SSID, PASSWORD)  # Se intenta conectar a la red WiFi especificada

# 🔹 Encender LED fijo mientras se conecta a WiFi
led.value(1)  # Enciende el LED para indicar que se está conectando
timeout = 30  # Tiempo máximo de espera para la conexión (30 segundos)

# Bucle de espera para la conexión WiFi
while not wlan.isconnected() and timeout > 0:
    print(f"Conectando a WiFi... ({timeout}s restantes)")  # Mensaje en la consola con el tiempo restante
    time.sleep(1)  # Espera 1 segundo antes de volver a intentar
    timeout -= 1  # Reduce el tiempo restante en 1 segundo

# Verificar si se logró la conexión
if wlan.isconnected():
    print(f"✅ Conectado a WiFi. IP: {wlan.ifconfig()[0]}")  # Muestra la IP asignada
else:
    print("❌ No se pudo conectar a WiFi. Verifica SSID y contraseña.")  # Mensaje de error
    # 🔴 Parpadeo rápido si no hay conexión WiFi
    while True:
        led.value(1)
        time.sleep(0.2)
        led.value(0)
        time.sleep(0.2)  # LED parpadea indicando error de conexión

# 🔹 Configurar los sensores
sensor_pico = ADC(4)  # Se configura el sensor de temperatura interno del RP2040 (canal 4 del ADC)
lm35 = ADC(Pin(26))   # Se configura el sensor LM35 en el pin GP26 (ADC0)

# 🔹 Factor de conversión del ADC (16 bits a voltaje)
CONVERSION_FACTOR = 3.3 / 65535  # El ADC tiene una resolución de 16 bits (65535 valores posibles)

def leer_temperatura_pico():
    """Leer temperatura interna de la Raspberry Pi Pico W"""
    lectura = sensor_pico.read_u16()  # Se obtiene la lectura del sensor (valor entre 0 y 65535)
    voltaje = lectura * CONVERSION_FACTOR  # Se convierte a voltaje (0V a 3.3V)
    return 27 - (voltaje - 0.706) / 0.001721  # Se usa la fórmula oficial para convertir voltaje a temperatura en °C

def leer_temperatura_lm35(muestras=10):
    """Leer la temperatura del LM35 con un promedio de varias mediciones"""
    suma_temperaturas = 0  # Variable para acumular las lecturas
    for _ in range(muestras):
        lectura = lm35.read_u16()  # Se obtiene la lectura del sensor LM35
        voltaje = lectura * CONVERSION_FACTOR  # Se convierte a voltaje
        temperatura = voltaje * 100  # LM35 entrega 10mV/°C, por lo que se multiplica por 100
        suma_temperaturas += temperatura  # Se acumula la temperatura medida
        time.sleep(0.05)  # Pequeña pausa entre mediciones para evitar ruido

    return suma_temperaturas / muestras  # Se retorna el promedio de las mediciones

# 🔹 Bucle infinito para lectura y envío de datos
while True:
    # 🔹 Leer sensores
    temperatura_chip = leer_temperatura_pico()  # Se obtiene la temperatura interna de la Pico W
    temperatura_lm35 = leer_temperatura_lm35()  # Se obtiene la temperatura del sensor LM35
    diferencia = abs(temperatura_lm35 - temperatura_chip)  # Se calcula la diferencia entre ambas temperaturas

    # Mostrar en consola las lecturas obtenidas
    print(f"🌡️ LM35: {temperatura_lm35:.2f}°C | RP2040: {temperatura_chip:.2f}°C | Diferencia: {diferencia:.2f}°C")

    # 🔹 Enviar datos a ThingSpeak cada 180 segundos (3 minutos)
    try:
        # Se realiza una petición HTTP GET a ThingSpeak con los valores de temperatura
        response = urequests.get(f"{URL}?api_key={API_KEY}&field1={temperatura_lm35}&field2={temperatura_chip}&field4={diferencia}")
        print(f"✅ Datos enviados a ThingSpeak. Respuesta: {response.text}")  # Se imprime la respuesta del servidor
        response.close()  # Se cierra la conexión HTTP
        led.value(1)  # 🔵 LED ENCENDIDO si el envío es exitoso
    except Exception as e:
        print(f"❌ Error al enviar datos: {e}")  # Mensaje de error si la petición falla
        # 🔴 Parpadeo rápido si hay error en el envío
        for _ in range(5):
            led.value(1)
            time.sleep(0.2)
            led.value(0)
            time.sleep(0.2)  # LED parpadea indicando error en la transmisión de datos

    time.sleep(180)  # Esperar 180 segundos (3 minutos) antes de la próxima medición
