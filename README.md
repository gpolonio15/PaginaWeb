# PaginaWeb

 Web de ventas creada con flask.

Se ha planteado una web (pycharm-flask) con base de datos sql, donde todo tipo de proveedores de ropa pueden vender sus productos, de forma que los propietarios de la página web se quedan con un porcentaje de cada venta.


1.	Cliente: En este apartado están disponibles todos los productos que se pueden comprar, es necesario introducir los datos del comprador para el posterior envio (Dirección, nombre, código postal…) antes de poder realizar la compra, no existe la posibilidad de comprar una cantidad superior de productos disponibles en la base de datos, de todos modos, en las características del producto aparece la cantidad máxima de productos disponibles.


2.	Proveedor: Cuando pulsas el botón de proveedor tienes dos posibilidades, por un lado, rellenar un formulario para introducir todos los datos referidos al producto que se desea vender, estos van directos a la tabla de la base de datos producto, y otro, para en el caso de que el producto este ya registrado, introducir la referencia y una cantidad, la cual se suma directamente al stock ya disponible en la tabla de la base de datos, de modo que no nos encontremos productos repetidos de la misma empresa.


3.	Administrador: Para poder entrar en el apartado de administración de la web, lo primero es introducir un usuario y una contraseña, las cuales se encuentran en la tabla de la base de datos usuario (se encuentran encriptadas), si son correctas se accede al apartado de administración, en el cual te aparecen todos los productos con sus diferentes datos (empresa, cantidad, precio, CIF, Referencia…), una de las funciones que puedes realizar en administración es la de eliminar un producto, en el caso de que los datos introducidos no sean los correctos o detectes cualquier tipo de infracción (el proveedor para poder registrar el producto ha de rellenar todos los campos). En el apartado superior encontramos dos botones, uno que te direcciona a todas las ventas realizadas, así como el beneficio obtenido y otro con todas las gráficas para de manera visual ver número de productos en la web, las compras y las ventas.

Añadir que en el caso de que un producto se encuentre por debajo del 80% del stock inicial, se enviará automaticamente un correo del administrador de la web al proveedor dandole la posibilidad de añadir más productos a la web.
