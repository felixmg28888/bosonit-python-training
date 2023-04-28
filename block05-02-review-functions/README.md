# **Bloque 05 <br> Funciones <br> Ejercicios de repaso**

### **Nombre del proyecto:** block05-02-review-basics

#

#### **Ejercicio 1**

Define una función que devuelva las palabras de entre 3 y 5 letras que no tienen la letra o. Úsala con la variable texto.

#

#### **Ejercicio 2**

Crea una función que devuelva el porcentaje de elementos únicos de una lista.

#

#### **Ejercicio 3**

La serie de Fibonacci es una conocida serie en la que cada elemento se calcula como la suma de los dos anteriores, empezando por 1 1, es decir:
$$1, 1, 2, 3, 5, 8, 13, 21, ...$$

Programar una función que calcule el n-ésimo término de la serie de forma recursiva

#

#### **Ejercicio 4**

Dada una lista con listas anidadas en su interior, devolver una lista que no esté anidada.

#

#### **Ejercicio 5**

Implementar una función que lleve a cabo el cifrado César de una frase. El cifrado se lleva a cabo de la siguiente manera:

+ Para cada letra de la palabra (sin distinguir mayúsculas y minúsculas) obtenemos su orden dentro del alfabeto.
+ A ese valor le sumaremos el valor de la *clave* dada por el usuario.
+ Sustituiremos la letra original por la que esté en esta nueva posición calculada dentro de nuestro alfabeto.

#

#### **Ejercicio 6**

Calcular la desviación estándar de una lista que será nuestra población. La desviación estandar ($\sigma$) se puede calcular mediante la expresión

$$\sigma^2 = \frac{\sum_{i=1}^n{(x-\bar{x})^2}}{n},$$
donde $\bar{x}$ es la media de la población. Hacerlo utilizando *map* y *reduce*.