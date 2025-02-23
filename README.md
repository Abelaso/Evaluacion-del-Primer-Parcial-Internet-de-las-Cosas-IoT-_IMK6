# 📡 Evaluación del Primer Parcial - Internet de las Cosas (IoT)

##  Descripción
Este proyecto implementa un **sistema de monitoreo de temperatura** utilizando una **Raspberry Pi Pico W**, un **sensor LM35**, y la plataforma **ThingSpeak** para el análisis y visualización de datos en tiempo real. También se utiliza **MATLAB Analysis** para calcular promedios y enviar alertas cuando la temperatura supera los **50°C**.

---

##  Requisitos
✅ **Raspberry Pi Pico W**  
✅ **Sensor de temperatura LM35**  
✅ **Conexión WiFi**  
✅ **Computadora con Windows, Mac o Linux**  
✅ **Cable micro-USB**  
✅ **Cuenta en ThingSpeak**  
✅ **Instalación de Thonny**  

---

##  Contenido del Repositorio
 **Código en MicroPython** → Código bien documentado para la Raspberry Pi Pico W.  
 **Archivo README.md** → Descripción del proyecto e instrucciones de instalación y uso.  
 **Capturas de Pantalla** → Imágenes del código, ThingSpeak y MATLAB Analysis en funcionamiento.  

---

##  Instrucciones de Instalación y Configuración

### 🔹 Instalación de Thonny
1️⃣ **Descarga** Thonny desde [thonny.org](https://thonny.org/).  
2️⃣ **Instala** el programa en tu computadora.  
3️⃣ **Abre Thonny** y selecciona **"Herramientas" → "Opciones"**.  
4️⃣ En la pestaña **"Interprete"**, selecciona **MicroPython (Raspberry Pi Pico)**.  
5️⃣ **Conecta la Raspberry Pi Pico W** con un cable **micro-USB** y selecciona el puerto correcto.  
6️⃣ **Verifica que el intérprete de MicroPython esté funcionando** escribiendo:  
   ```python
   print("Hola desde la Raspberry Pi Pico W!")
   ```  
7️⃣ Si ves el mensaje en la consola, **Thonny está correctamente configurado**.  

---

### 🔹 Creación de una cuenta en ThingSpeak
1️⃣ **Ve a** [ThingSpeak](https://thingspeak.com/) y crea una cuenta gratuita.  
2️⃣ **Inicia sesión** y ve a **"My Channels"**.  
3️⃣ **Crea un nuevo canal** y configura los siguientes campos:  
   - **Field 1:** Temperatura del sensor LM35  
   - **Field 2:** Temperatura del chip de la Raspberry Pi Pico W  
   - **Field 3:** Promedio de temperatura  
   - **Field 4:** Diferencia entre LM35 y el chip interno  
4️⃣ **Guarda el Channel ID y las API Keys (Read y Write)** para usarlas más adelante.  

---

### 🔹 Configuración del Hardware
 **Conexiones del sensor LM35:**  
1️⃣ **VCC** del LM35 a **3.3V** de la Raspberry Pi Pico W.  
2️⃣ **GND** del LM35 a **GND** de la Raspberry Pi Pico W.  
3️⃣ **OUT** del LM35 a **GP26 (ADC0)** de la Raspberry Pi Pico W.  
(Apóyate en la imagen **"Raspberry pinout"** para ver las conexiones del microcontrolador).  

 **Conexión de la Raspberry Pi Pico W:**  
1️⃣ **Conéctala a la computadora** con un cable **micro-USB**.  

---

### 🔹 Programación en MicroPython
1️⃣ **Abre Thonny IDE** y crea un nuevo archivo `main.py`.  
2️⃣ **Copia y pega** el código de MicroPython para conectarse a WiFi y enviar datos a ThingSpeak.  
3️⃣ **Guarda el archivo** como `main.py` en la **Raspberry Pi Pico W** para que se ejecute automáticamente.  
4️⃣ **Desconéctala de la PC** y conéctala a una **fuente de energía externa**.  

---

### 🔹 Creación de MATLAB Analysis en ThingSpeak
1️⃣ **Ve a** **Apps → MATLAB Analysis** en ThingSpeak.  
2️⃣ **Crea un nuevo script** y **borra el código predeterminado**.  
3️⃣ **Copia y pega** el código ubicado en el archivo **"MATLAB Analysis code"**.  
4️⃣ **Guarda y ejecuta el script**.  
5️⃣ **Configura TimeControl** para ejecutar este script automáticamente cada **5 minutos**.  

---

##  **Tu sistema ahora enviará datos automáticamente a ThingSpeak y calculará el promedio de temperatura sin intervención manual**

(Si necesitas ayuda, revisa las capturas de pantalla incluidas en este repositorio).  

---

##  Información del Autor
📍 **Autor:** *Rodriguez Guerrero Abel Israel*  
📍 **Universidad:** *Universidad Modelo*  
📍 **Materia:** *Internet de las Cosas*  
📍 **Evaluación:** *Primer Parcial*  
📍 **Fecha:** *23/02/2025*  








