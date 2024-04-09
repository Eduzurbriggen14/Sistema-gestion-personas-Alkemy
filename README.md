# StockControl
StockControl es un proyecto Django que proporciona funcionalidades para gestionar productos y proveedores.

Permite agregar nuevos productos y proveedores, listar todos los productos registrados en la base de datos y tener disponible en el Admin el modelo del producto y del proveedor.

# Credenciales del superUser

`Username: eduardo`

`Password: 123456`

## Requerimientos
- `Python 3.x`

- `Django`

Para verificar si tenemos instalado Python debero ejercutar `python --version` en la terminal

Si tenemos instalado Phyton nos saldra un cartel como este **Python 3.11.3** donde nos indica la version instalada

Para verificar si tenemos instalado Django debero ejercutar `django-admin --version` en la terminal, si tenemos instalado Django nos dira la version instalada

Si no tenemos instalados los programas debemos dirigirnos a [Python.dowloads](https://www.python.org/downloads/)

Una vez instalado Python debemos agregarlo al Phat en Editar Variables de Entorno del Sistema

Instalado y configurado Python debemos instalar Django mediante `django-admin --version` en la terminal

Luego verificamos la instalacion de Python y Django mediante los comando descriptos arriba

## Pasos para configurar el proyecto

### Clonar el repositorio:

[`link-repositorio`](https://github.com/Eduzurbriggen14/Sistema-gestion-personas-Alkemy.git)

### Crear un Entorno Virtual

Crear un entorno virtual es una práctica recomendada en el desarrollo de aplicaciones Python, incluyendo proyectos de Django. Un entorno virtual proporciona un espacio aislado donde puedes instalar paquetes específicos para un proyecto sin interferir con otros proyectos o con el sistema operativo. Esto es útil porque diferentes proyectos pueden requerir diferentes versiones de las mismas bibliotecas, y un entorno virtual te permite gestionar estas dependencias de manera efectiva

- Instalar Virtualenv

  `virtualenv` es una herramienta que te permite crear entornos virtuales fácilmente. Si aún no lo tienes instalado, puedes hacerlo ejecutando en la terminal:

  `pip install virtualenv`

- Dirigirnos a la carpeta del proyecto StockControl

  `cd StockControl`

- Dentro de la carpeta StockControl o del proyecto ejecutamos en la temrinal

  `virtualenv venv`. Esto instala el entorno virtual en nuestro proyecto, *venv* se refiere al nombre que se le dara al entorno virtual. Esto nos crea una carpeta *venv* en nuestro proyecto

- Activar el entorno virtual, ejecutamos en la terminal lo siguiente
  
  `source venv/Scripts/activate`

- Desactivar el entorno virtual, ejecutamos en la terminal lo siguiente
  
  `source venv/Scripts/desactivate`

### Instalar las dependencias del proyecto:

`pip install -r requirements.txt`

### Realizar migraciones para crear la base de datos:

`python manage.py makemigrations`

`python manage.py migrate`

### Crear un superusuario para acceder al panel de administración:

`python manage.py createsuperuser`

Ingresamos las credenciales necesarias para crear el super usuario

### Ejecutamos el proyecto mediante el siguiente codigo

`python manage.py runserver`

Acceder al panel de administración, en la consola hacemos *"ctrl+click"* en `http://localhost:8000/admin/` e iniciamos sesión con las credenciales del superusuario creado.
