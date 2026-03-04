## Sistema Para La Gestión de Inventarios con Django

Este proyecto es un sistema de gestión de inventarios básicos realizado con el framework de Django, SQLite para la BD, para el diseño de la interfaz
se uso la plantilla con Bootstrap SB Admin 2; este sistema permite la creación, edición y eliminación de productos y categorías, además de formularios
que permiten el registro de entradas y salidas de inventarios, guardando un historial de los registros de salidas/entradas, cuenta también con un dashboard 
para la visualización de métricas, como el total de salidas y entradas por día, el producto más vendido, una sección para visualizar un resumen de los productos 
del inventario, con su estatus para el stock, mostrando un mensaje cuando el stock es suficiente, esta por debajo del stock mínimo, o esta sin stock, esta ifnromación 
se puede filtrar por categoría de producto, facilitando la gestión de inventarios para la empresa. 

**Requisitos no funcionales:**
- Usabilidad:El usuario debe poder crear categorias y productos en menos de 2 min.
- Constencia: Si un producto es eliminado no puede registarse una entrada o salida de inventario de ese producto.
- Validaciones: El sistema no debe permitir SKU de productos repetidos, al registrar la salida de productos no puede ser una cantidad mayor
  al stock actual, el precio del producto no puede ser negativo. 

**Decisiones técnicas:** 
Se opto por el framework de Django ya que permite el desarrollo de manera rápida y segura, siendo una buena opción para un sistema básico de inventarios,mencionan que la
empresa es pequeña y actualmente maneja sus registros en Excel, por lo que considero que una solución que agilice la digitalización de sus procesos sin requerir una 
infraestructura compleja sería lo más optimo. Además, Django facilita la integración con bases de datos relacionales en este caso SQLite, manejo de formularios, autenticación de usuarios, 
facilita la creación de CRUDS lo que reduce significativamente el tiempo de desarrollo y permite entregar un sistema funcional en menor tiempo.

**Arquitectura:**
El proyecto esta basado en la arquitectura Modelo-Vista-Plantilla, que es un patrón de diseño de software dentro de Django que utiliza:

- Modelos para manejar la lógica y estructura de datos de su base de datos
- Vistas para manejar la lógica y funcionalidad de las aplicaciones
- Plantillas para gestionar el diseño y la estructura de la aplicación orientada al usuario
Además que lo estructure en apps independientes **productos**, **Categorías**, **Inventario**, **Generales** ( que gestiona el deshboard con las metricas),
así cada aplicación tiene su propio modelo, vista y template, lo que separa sus responsabilidades.
Se realizo un diagrama de casos de uso con dos actores principales administrador y empleado, la idea es que sólo el administrador pueda configurar las
categorías y crear productos, por cuestiones de tiempo aún no se configura completamente de esa manera.
<img width="420" height="400" alt="Casos de uso-GesInventario" src="https://github.com/user-attachments/assets/a3a3c7ec-71c7-4cfa-81d3-94839e62bf27" />

También se realizo el diagrama de clases para el diseño de la BD

<img width="426" height="967" alt="mermaid-diagram" src="https://github.com/user-attachments/assets/4f39d73a-42cf-4e7b-94d6-a9bfb1bd40d7" />

**Configuración del proyecto:**
1. Crear una carpeta para guardar el proyecto y el entorno
2. git clone https://github.com/Brismi03/Gestion_Inventarios.git
3. python -m venv miEntorno 
4. cd miEntorno
5. cd Scripts
6. Activate
7. Cd..
8. cd gesInventario
9. pip install -r requirements.txt
10. Crea un archivo .env en la raíz del proyecto (junto a manage.py) con:
  SECRET_KEY=tu_clave_secreta
  DEBUG=True
11. python manage.py migrate //Crea la BD y tablas
12. python manage.py createsuperuser //Ingresa un usuario y contraseña con ese vas a acceder
13. python manage.py runserver //Para ejecutar el servidor
14. Acceder con el navegador http://127.0.0.1:8000/

