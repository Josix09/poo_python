# poo en python
- El paradigma de POO está basado en una abstracción del mundo real que nos va a permitir desarrollar programas de forma más cercana a como vemos el mundo, pensando en objetos que tenemos delante y en acciones que podemos hacer con ellos

## clase
- una clase es un tipo de dato cuyas variables se laman objetos o instancias

- la clase es la definición de un objeto real y los objetos o instancias son el propio objeto del mundo real

- las clases están compuestas por 2 elementos: Atributos y Métodos.

### Atributos
-son información que almacena la clase

### Métodos
-son las operaciones que pueden realizar las clases

## Definición de una clase en Python

```Python
class NombreClase:
  def_init__(self, variable1, variable2):
    self.Atributo1=valor 1
    self.Atributo2=valor 2

  def nombremetodo(self): 
    bloqueCodigo


```

### Componentes
```class```: palabra seresvada en Python para definir una clase.

```NombreClase```:Nombre de la clase que quieres crear.

```def```:palabra reservada en python que se utiliza par definir tanto el constructor de la clase (método que se ejecuta la primera vez que usas una clase)como los diferentes métodos que tiene.

```_inint__```:palabra reservada en python para definir el método constructor de la clase. Es lo primero que se ejecuta cuando creas un objeto de una clase

```(self,variableX)```:parámetro del constructor de la clase. El parámetro self es obligatorio y despues puedes tener tantos parámetros como quieras. La forma de añadir parámetros es la misma que en las funciones.

```(self.AtributoX)```:forma de utilización y acceso a los atributos de la clase.

```nombremetodo```:nombre del método de la clase

```self```:parámetros de método. El parámetro self es obligatorio y despues puedes tener tantos parámetros como quieras.

```bloqueCodigo```:instrucciones que ejecutará el método.

- cuando defines una clase debes tener en cuenta los siguentes puntos:

- puedes tener tantos atributos como necesites
- puedes definir tantos métodos como necesites
- puedes definir tantos parámetros en el constructor y en los métodos como necesites.

## Composición
- consiste en la creación de nuevas clases a partir de otras clases ya existentes que actúan como elementos compositores de la nueva.
- las clases existentes serán atributos de la nueva clase.
- en POO la composición significa que entre las 2 clases existe una relación del tipo "tiene un".
- ejemplo:
  - una cordenada en 2 dimensiones está compuesta por 2 valores, el valor en el eje de las X y el valor en el eje de las Y, esto podría ser una clase. Un cuadrado está compuesto por 4 coordenadas que son los 4 vértices,esto podría ser una clase que está compuesta por 4 clases del objeto coordenada.




