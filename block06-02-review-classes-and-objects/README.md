# **Bloque 06 <br> Clases y objetos <br> Ejercicios de  repaso**

### **Nombre del proyecto:** block06-02-review-classes-and-objects

#

#### **Ejercicio 1**

Crea una clase vehículo que al instanciarse se le pase la información la potencia y su consumo a los 100 km. Además, crea un método que nos devuelva el consumo por kilómetro.

#

#### **Ejercicio 2**

Crear una clase coche que herede de la clase vehículo. Se añaden los atributos numero de puertas y tipo de gasolina.

#

#### **Ejercicio 3**

Crear mediante la utilización de clases un sistema capaz de lidiar con vectores en 2D, es decir, con el que podamos calcular el producto escalar de dos vectores, el coseno del ángulo entre dos vectores y con el que podamos sumar y restar vectores (además de compararlos entre sí en términos de módulo). Definir las funciones de producto como métodos de un vector al que se le pasa otro vector.

(Se pueden definir las funciones \_ \_lt\_ \_ y \_ \_gt\_ \_ ).

#

#### **Ejercicio 4**

Crear un objeto de tipo rectángulo, que tenga la posibilidad de devolver el area y el perímetro. Además, tendrá que poder comparar rectángulos entre sí (la igualdad será igualdad total y las comparaciones se realizarán en términos de área). Tambien implementar si un rectángulo está contenido en otro.

Para hacerlo más sencillo, definir el rectángulo como un origen en el plano x e y , la longitud del lado horizontal y la longitud del lado vertical (es decir, no trabajaremos con rectángulos que no tengan un lado paralelo al eje X. Además, supondremos que el origen dado es la esquina inferior izquierda.

    class rectangulo:
        def __init__(self, origen_x, origen_y, lado_h, lado_v):
            self.x1 = origen_x

#

#### **Ejercicio 5**

Crear una clase de tipo círculo dando el centro y el radio. Crear los métodos necesarios para calcular el area, el perímetro, un método para poder comprobar si un punto está en su interior y un método que modifique el círculo para introducir un punto en su interior.