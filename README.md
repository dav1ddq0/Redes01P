# <center>Proyecto de Redes Capa fisica<center>
### <center>David Orlando De Quesada Oliva C311</center>
### <center>Javier Dominguez C312</center>


##### De la forma en que decidimos modelar el proyecto consideramos hacer las colisiones de la siguiente manera:
##### Si el host va a enviar un bit de informacion y el no esta conectado a nadie entonces se entiende como un  intento fallido y se hace lo mismo que si hubiera una colision por estar el cable transmitiendo otro bit de informacion en en ese instante. Al detectar una colision procedemos a lo siguiente el host no transmite la informacion y decide en ponerse estado stopped dentre de un tiempo aleatorio el cual aumenta de rango en cada  intento fallido de poner ese bit a transmitir. Decidimos tener un maximo de 16 intentos fallidos luego de los cuales ese bit se pierde y no llega a transmitirse.
#####
#####






