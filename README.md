# WebYoga
Web para Escuela de Yoga 
Luego de diagramar el esquema de la web, cree todo desde cero en Django.
Creo las vistas, los modelos, las url y los templates.
Pruebo con el servidor corriendo que todas las partes de la web funcionen correctamente.
El ingreso desde cada boton a las diferentes secciones, la carga de datos y la busqueda de los mismos en la BD.
Desde el superusuario chequeo que se haya cargado todo correctamente.
Partes de la web
Inicio: http://127.0.0.1:8000/AppYoga/
Tocando en cada boton lleva a la url correspondiente, en cada una un formulario de ingreso de datos
Para busqueda cree la siguiente url: http://127.0.0.1:8000/AppYoga/buscarAlumnos/
Se busca por apellido, por ejemplo, rivas
Al haber un alumno cargado con ese apellido, lo encuentra. Tambien se creo la url para que diga si no hay resultados. 