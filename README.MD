# Calculadora de Prestaciones

### Nombre: Luis Gerardo Ramos Martinez
### Bootcamp: Data Analyst 10
### Actividad: Uso del lenguaje Python

Este es un proyecto Django para calcular prestaciones salariales usando python

## Descripción

Todo el codigo y logica de la app se encuentra en el directorio:
**calculdora_prestaciones/views.py**

## Requisitos

- Python 3.8+
- Django 3.2+

## USO
### Link de la aplicación
**https://djangocalculadoraprestaciones.azurewebsites.net/calculadora/**

# Tecnologías
- Python
- Django
- Azure
## Descripción del Proyecto

La Calculadora de Prestaciones es una aplicación web desarrollada con Django que permite a los usuarios calcular las prestaciones salariales de manera sencilla y rápida. La aplicación está desplegada en Azure y utiliza diversas tecnologías para ofrecer una experiencia de usuario eficiente y confiable.

## Instalación

1. Clona el repositorio:
    ```sh
    https://github.com/Ezzz-Lui/CalculadoraPrestacionesDjango.git
    ```

2. Crea y activa un entorno virtual:
    ```sh
    python -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    ```

3. Instala las dependencias:
    ```sh
    pip install -r requirements.txt
    ```

4. Realiza las migraciones de la base de datos:
    ```sh
    python manage.py migrate
    ```

5. Ejecuta el servidor de desarrollo:
    ```sh
    python manage.py runserver
    ```

## Despliegue en Azure

1. Inicia sesión en Azure:
    ```sh
    az login
    ```

2. Crea un grupo de recursos:
    ```sh
    az group create --name myResourceGroup --location eastus
    ```

3. Crea un plan de servicio de aplicaciones:
    ```sh
    az appservice plan create --name myAppServicePlan --resource-group myResourceGroup --sku FREE
    ```

4. Crea la aplicación web:
    ```sh
    az webapp create --resource-group myResourceGroup --plan myAppServicePlan --name myUniqueAppName --runtime "PYTHON|3.8"
    ```

5. Configura las variables de entorno:
    ```sh
    az webapp config appsettings set --resource-group myResourceGroup --name myUniqueAppName --settings DJANGO_SETTINGS_MODULE=calculadora_prestaciones.settings SECRET_KEY=tu_clave_secreta
    ```

6. Configura el despliegue desde Git local:
    ```sh
    az webapp deployment source config-local-git --name myUniqueAppName --resource-group myResourceGroup
    ```

7. Añade el remoto de Azure y realiza el push:
    ```sh
    git remote add azure <URL_de_Git_proporcionada_por_Azure>
    git push azure master
    ```