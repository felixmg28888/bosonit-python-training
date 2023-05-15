# **Bloque 10 <br> Pandas**

### **Nombre del proyecto:** block10-01-pandas

#

#### **Ejercicios con Series 1**
    brand = ['Camp', 'Camp', 'Petzl', 'Petzl', 'Edelrid', 'Edelrid', 'Edelrid’, 'Black Diamond', 'Black Diamond', 'Mammut']
    models = ['Energy', 'Jasper', 'Simba', 'Adjama New', 'Moe', 'Orion', 'Leaf','Xenes', 'Chaos', 'Ophir']
    prices = [39.90, 56.00, 45.00, 75.00, 49.90, 99.90, 65.00, 119.90, 99.90, 55.00]

1. Crea las listas brand, models y prices citadas anteriormente.
2. Define una Series en la que models sean los índices y prices los valores
3. Muestra los modelos con el precio menor que 70 euros.
4. Define una nueva Series que contenga el precio original para todos los productos excepto para la marca (brand) "Edelrid", a la que hay que realizarle el 10% de descuento.

#

#### **Ejercicios con DataFrames**
1. Usando las listas brands, models y prices del ejercio anterior. Crear un data_frame llamado que almacene toda esta información en tres columnas (brand, model y price) y los índices los genere automáticamente.
2. Mostrar la columna "Brand".
3. Muestra la quinta fila.
4. Modifica el precio del modelo "Energy" a 9999.
5. Crea una nueva columna “Discount” con el valor 50 para cada fila.
6. Usando el DataFrame del Ejercicio 5, crea un nuevo DataFrame que añada las columnas "Sales" y "Total".
7. Borra la primera y séptima fila.
8. Borra la primera y tercera columna.
9. Muestra la información para la marca "Edelrid".
10. Muestra todos los valores con un precio mayor que 70.
11. Cree una lista con 10 número aleatorios entre 0 y 500 y añadelo como valor de la columna "Sales".
12. Calcula el valor de la columna “Total” del resultado de multiplicar el precio y las ventas.
13. Muestra la información del DataFrame ordenado por ventas.
14. Usando la función apply cambia el formato a dos decimales.
15. Muestra la principal información de las variables estadísticas de las columnas de tipo numérico.
16. Muestra la principal información de las variables estadísticas de las columnas de tipo categórico.
17. Muestra si hay algún valor nulo.
18. Calcula el número de productos para cada marca.
19. Guarda la información del DataFrame en un fichero xlsx.