# StockControl
StockControl es un proyecto Django que proporciona funcionalidades para gestionar productos y proveedores.

Permite agregar nuevos productos y proveedores, listar todos los productos registrados en la base de datos y tener disponible en el Admin el modelo del producto y del proveedor.

## Requerimientos
`Python 3.x`

`Django`

## Pasos para configurar el proyecto
Clonar el repositorio:

`git clone https://github.com/tu_usuario/stockcontrol.git`
Instalar las dependencias del proyecto:

Una vez que clonamos el repositorio, abrimos el proyecto en VSCode y nos posicionamos en el proyecto StockControl

`cd StockControl`
pip install -r requirements.txt
Realizar migraciones para crear la base de datos:

Relizar Migraciones
`python manage.py makemigrations`
`python manage.py migrate`

Crear un superusuario para acceder al panel de administración:

`python manage.py createsuperuser`
Ingresamos las credenciales necesarias para crear el super usuario

jecutar el servidor de desarrollo:


`python manage.py runserver`
Acceder al panel de administración en `http://localhost:8000/admin/` e iniciar sesión con las credenciales del superusuario creado.

Pasos para crear una nueva app
Ejecutar el siguiente comando para crear una nueva app llamada "compra":

bash
Copy code
python manage.py startapp compra
Definir los modelos Producto y Proveedor con los campos requeridos dentro de la app compra/models.py.

Realizar las migraciones correspondientes:

bash
Copy code
python manage.py makemigrations compra
python manage.py migrate
Registrar los modelos en el archivo compra/admin.py para que sean visibles en el panel de administración.
