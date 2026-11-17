#====MINI BASE DE DATOS====#

+===DESCRIPCION===+
Es una mini base de datos importando la biblioteca de sqlite3 de python3, lo que se usa, para hacer un registro que cumple con "CRUD" de una base de datos
Se usan otras librerias como datetime para usar el tiempo en operaciones y math para lo mismo, a su vez se usa Path, unicamente al inicio para validar
Si el archivo ya existe.

###COMO USAR###
Copia y pega el archivo en tu terminal o en tu aplicacion para editar codigo de confianza, tienes que tener python3 unicamente, las demas librerias ya vienen
Incluidas con pyhton3

--------COMO FUNCIONA---------
Al momento de ejecutar el programa te pedira que ingreses el nombre del archivo en el que quieres trabajar, si ya existe te avisara y trabajara en el inmediatamente
Si no, creara uno nuevo y creara un tabla, despues tiene la consola interactiva que te dara a escojer entre registrar un nuevo vehiculo, ver los vehiculos, registrar una salida, borrar un vehiculo y salir, el registro es facil.

1.-Registrar vehiculo: Presionas 1 para entrar ala consola para registrar un vehiculo, te pedira confirmacion, despues ingresas el nombre del vehiculo, luego placas y despues color, la hora
de entrada se registra sola con la libreria datetime, asi que no te preocupes por eso.

2.-Ver vehiculo: Puedes ver el vehiculo por varias formas, ver el registro completo de todos lo vehiculos, o buscarlo por nombre o por placas, la verdad no es complicado.

3.-Registrar salida: Al salir te mostrara una lista de los carros que no han salido usando la validacion si la columna hora_salida ya ha sido llenada, despues los enumerara para que ingrese el
numero de la lista del carro que va a salir, usando datetime haremos una operacion en la que es 15 pesos la hora o fraccion, de este modo se cobrara el tiempo usando de igual forma el tiempo en
modo real de igual forma como se registro al inicio

4.-Borrar vehiculo: aparecera una tabla con todos los vehiculos que han sido registrados, util para que puedas ver que carro deseas borrar, despues ingresas el numero con el que se registro
ese numero representa la posicion de la tabla (id), de esta forma evitamos posibles errores y confusiones, ya que si se hace por el puro nombre o matricula se podria borrar carros con el mismo
mismo nombre o placas.

5.- Salir: Salimos del programa y cerramos los cursores y la conexion con el archivo de forma segura.
