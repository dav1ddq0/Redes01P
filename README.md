# <center>Proyecto de Redes Capa fisica<center>
### <center>David Orlando De Quesada Oliva C311</center>
### <center>Javier Dominguez C312</center>


##### De la forma en que decidimos modelar el proyecto consideramos hacer las colisiones de la siguiente manera:
##### Si el host va a enviar un bit de informacion y el no esta conectado a nadie entonces se entiende como un  intento fallido y se hace lo mismo que si hubiera una colision por estar el cable transmitiendo otro bit de informacion en en ese instante. Al detectar una colision procedemos a lo siguiente el host no transmite la informacion y decide en ponerse estado stopped dentre de un tiempo aleatorio el cual aumenta de rango en cada  intento fallido de poner ese bit a transmitir. Decidimos tener un maximo de 16 intentos fallidos luego de los cuales ese bit se pierde y no llega a transmitirse. Para modelar los host y los hust tenemos dos class Hub y Host que sirven para modelar estos objetos. la class Host tiene una propiedad port que representa el unico puerto que tiene un host port tambien esta representado como una class Port la cual tiene la propiedad cable que permite conocer si hay un cable conectado o no cable esta tambien representado por una class Cable la cual contiene. Un host siempre escucha antes de empezar a transmitir si al escuchar por el cable se esta transmitiendo informacion que  el mismo esta recibiendo entonces se produce una colision y se aplica el protocolo explicado previamente. En caso que por una desconexion conexion en medio de una transmision de dos o mas host se unan todas estas sennales a traves de un hub se manda una sennal a los host para que paren de mandar informacion y se le aplica el protocolo a estos. De la forma que esta pensado un host sabe si esta transmitiendo o esta interrumpido sin posibilidad de enviar informacion hasta que pasa el tiempo requerido de estado interrumpido. Puede darse el caso que se mande un send a un host que esta interrumpido en dicho caso la informacion se intenta mandar y al no tener un cable para el envio funciona como una colision aplico el protocolo y vuelvo a intentar luego de una cantidad random de tiempo. Todo cable sabe en caso que se este transmitiendo informacion desde que puerto proviene esto permite  en caso de una desconexion  saber que parte de la red fue la que perdio la informacion que se estaba transmitiendo en ese instante y mandar a poner todos los cables que pertenecen a la misma en Null. Para saber las conexiones se dispone de un diccionario conexions con el cual se sabe si en puerto esta conectado y con quien esta conectado en caso que lo este. En una lista guardamos cada host que se crea ms a ms y para actualizar el estado de la red recorremos esa lista constantemente para comprobar si un host esta transmitiendo o esta parado producto de una colision y del protocolo que aplicamos . Si luego de un recorrido por todos los hosts ninguno esta transmitiendo o esta esperando a transmitir producto de una colision entonces se puede decir que la red queda inactiva si no hay mas instrucciones por ejecutar.

#####
#####






