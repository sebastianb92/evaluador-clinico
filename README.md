# Servicio de Predicción Clínica (Simulado) - Docker + Flask

## Descripción general
Este proyecto implementa un **servicio web médico simulado** que permite a un profesional ingresar variables clínicas básicas y obtener una predicción del estado de salud del paciente.

El sistema **no usa un modelo de machine learning real**, sino reglas determinísticas que simulan el comportamiento de un modelo predictivo.  
El propósito es **demostrar cómo desplegar un modelo o servicio de predicción dentro de un contenedor Docker**, exponiéndolo mediante una interfaz web o una API.


## Estados posibles
El servicio retorna uno de los siguientes estados clínicos:

- 🟢 **NO ENFERMO**  
- 🟡 **ENFERMEDAD LEVE**  
- 🟠 **ENFERMEDAD AGUDA**  
- 🔴 **ENFERMEDAD CRÓNICA**


---

## Estructura del proyecto

servicio_medico/
│
├── app.py           # Aplicación web: levanta el servidor Flask, recibe datos del usuario y muestra resultados.
├── model.py         # Lógica simulada de diagnóstico: función que evalúa los valores ingresados y retorna el estado clínico.
├── requirements.txt # Dependencias de Python necesarias (Flask, etc.).
├── Dockerfile       # Define la imagen Docker del servicio para correr la app en cualquier máquina.
├── templates/
│   └── index.html   # Interfaz web para que el médico ingrese los datos y vea el diagnóstico.
└── README.md        # Documentación del proyecto, instrucciones de uso, ejemplos y créditos.


---

## Ejecución con Docker

### 1. Construir la imagen

Desde la carpeta raíz del proyecto (donde está el `Dockerfile`):

bash
docker build -t servicio_medico:1.0 .


### 2. Ejecutar el contenedor

bash
docker run --rm -p 5000:5000 servicio_medico:1.0


### 3. Acceder a la aplicación

Abre tu navegador en:
http://localhost:5000

Allí podrás ingresar los valores requeridos (edad, PCR, frecuencia cardíaca) y obtener el diagnóstico correspondiente.

---

## Ejemplo de uso


| Variable                      | Descripción                  | Ejemplo |
| ----------------------------- | ---------------------------- | ------- |
| **Edad**                      | Años completos del paciente  | `45`    |
| **Proteína C Reactiva (PCR)** | Marcador inflamatorio (mg/L) | `8.5`   |
| **Frecuencia Cardíaca (FC)**  | Latidos por minuto           | `95`    |


Resultado esperado → ENFERMEDAD LEVE

---

## Interfaz Web

La aplicación incluye una interfaz médica limpia desarrollada con HTML y CSS:

Campos de entrada con descripciones y ejemplos.

Diagnóstico mostrado de forma clara y visual.

![Interfaz Web](./img/app_web.png)

---

## Tecnologías usadas

* Python 3.10

* Flask (microframework web)

* HTML5 / CSS3

* Docker

---

## Autores

* Josue Cobaleda

* Sebastián Bonilla

---

Este proyecto es demostrativo y no debe utilizarse para diagnósticos médicos reales.
