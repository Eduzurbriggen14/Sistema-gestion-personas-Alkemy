# StockControl
StockControl es un proyecto Django que proporciona funcionalidades para gestionar productos y proveedores.

Permite agregar nuevos productos y proveedores, listar todos los productos registrados en la base de datos y tener disponible en el Admin el modelo del producto y del proveedor.

## Requerimientos
`Python 3.x`

`Django`

## Pasos para configurar el proyecto
### Clonar el repositorio:

`git clone https://github.com/tu_usuario/stockcontrol.git`

### Instalar las dependencias del proyecto:

`pip install -r requirements.txt`

### Una vez que clonamos el repositorio, abrimos el proyecto en VSCode y nos posicionamos en el proyecto/carpeta StockControl

`cd StockControl`

### Realizar migraciones para crear la base de datos:

`python manage.py makemigrations`

`python manage.py migrate`

### Crear un superusuario para acceder al panel de administración:

`python manage.py createsuperuser`

Ingresamos las credenciales necesarias para crear el super usuario

### Ejecutamos el proyecto mediante el siguiente codigo

`python manage.py runserver`

Acceder al panel de administración, en la consola hacemos *"ctrl+click"* en `http://localhost:8000/admin/` e iniciamos sesión con las credenciales del superusuario creado.
