# **Bloque 10 <br> Pandas**

### **Nombre del proyecto:** block10-03-review-pandas

#

#### **Ejercicios de repaso**
    lst1 = ['gato', 'perro', 'ratón', 'elefante', 'rinoceronte']
    lst2 = [x for x in range(1,6)]
1. Convierte lst1 a un Series y lst2 a otro Series. Una vez creados, combinar los Series para crear un DataFrame.
2. Renombra la columna basada en lst1 creada previamente a "animales".
3. Crea dos series de tamaño 10 con valores entre 1 y 10. Elimina del series1 los elementos que aparezcan en Series2.
4. Obtén los elementos no comunes en ambas series.
5. Obtén el mínimo y los percentiles 25, 50, 75 y 80 de la primera serie.
6. Obtén la frecuencia con la que se repite cada valor.
7. Mantén el valor de los dos elementos más repetidos y al resto asignale el valor "Otros".
8. Crea un Series de tamaño 35 con valores aleatorios. Crea un DataFrame basado en este Series de dimensión 7 filas y 5 columnas.
9. Partiendo de las series creadas en el *Ejercicio 1* apilar las dos series verticalmente.
10. Ahora apila horizontalmente.
11. Cómo convertir en mayúscula el primer caracter de Series de animales.
12. Calcula el número de caracteres de cada elemento.
13. Calcula la diferencia entre los valores de cada elemento consecutivo del Series numérico.
14. Dada la lista siguiente de fechas, carga un Series de string a datetime
['2015-08-06T12:20', '2012-04-02', '2021/01/03', '20191121', '01-12-2015', '04 Jan 2007'].
15. Obtén el día del año del Series anterior.
16. Obtén el día de la semana.
17. Crea un DataFrame basado en un Series de 10 elementos que se genere aleatoriamente entre "manzana", "plátano", "zanahoria" y pesos que sea un Series de 10 elementos aleatorios entre 1 y 10. Calcula la media del peso por fruta.
18. Crea un Series que contenga los 10 primeros lunes de 2022 como índice y un número aleatorio como valor.
19. Crea un DataFrame basado en el Series del *Ejercicio 18* con las columnas llamadas fecha y precio.
20. Genera un DataFrame de 5x5 y posteriormente invierte el orden de los valores de sus filas.
21. Añade una nueva columna que sea el máximo entre el mínimo de cada fila.