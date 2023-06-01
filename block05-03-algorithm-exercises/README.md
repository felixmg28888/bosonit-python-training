# **Bloque 05 <br> Clases y objetos <br> Ejercicios de Algoritmia**

### **Nombre del proyecto:** block05-03-algorithm-exercises

#

#### **01. Llenando cubos <br> Nombre del proyecto:** block05-03-01-cubes
Dado un conjunto de cubos llenos de distintas cantidades de agua, se pide calcular la cantidad mínima de agua necesaria para nivelar los cubos de forma que todos ellos acaben teniendo la misma cantidad.<br>

Consideraciones:
- El nivel de agua de un cubo no puede decrecer, sólo aumentar.
- Los cubos se nivelarán respecto al cubo más lleno.

**Input**
- Un conjunto de números enteros especificando la cantidad de agua de la que dispone cada cubo.

**Output**
- Imprimir por la salida estándar la cantidad mínima de agua necesaria para nivelar los cubos.

<style>
    table, th, td {
        border: 1px solid black;
    }
</style>

<table style="width:100%">
    <thead>
        <tr>
            <th>Sample Input 1</th>
            <th>Sanple Output 1</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td align="center">10 8 7</td>
            <td align="center">5</td>
        </tr>
    </tbody>
</table>
<br>
<table style="width:100%">
    <thead>
        <tr>
            <th>Sample Input 2</th>
            <th>Sanple Output 2</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan=4 align="center">8 8 8</td>
            <td rowspan=4 align="center">0</td>
        </tr>
    </tbody>
</table>
<br>

#

#### **02. Validación de paréntesis <br> Nombre del proyecto:** block05-03-02-parentheses
Dada una cadena que contiene únicamente los caracteres ’(’, ’)’, ’{’, ’}’, ’[’ y ’]’, determinar si la cadena de entrada es válida.

**Input**
- Los paréntesis abiertos deben cerrarse con el mismo tipo de paréntesis.
- Los paréntesis abiertos deben cerrarse en el orden correcto.

**Output**
- Imprimir por la salida estándar "true" si la cadena es válida, "false" en caso contrario.

<table> <table style="width:100%">    <thead>
        <tr>
            <th>Sample Input 1</th>
            <th>Sanple Output 1</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td align="center">( )</td>
            <td align="center">true</td>
        </tr>
    </tbody>
</table>
<br>
<table style="width:100%">
    <thead>
        <tr>
            <th>Sample Input 2</th>
            <th>Sanple Output 2</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td align="center">( ) [ ] { }</td>
            <td align="center">true</td>
        </tr>
    </tbody>
</table>
<br>
<table style="width:100%">
    <thead>
        <tr>
            <th>Sample Input 3</th>
            <th>Sanple Output 3</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td align="center">( }</td>
            <td align="center">false</td>
        </tr>
    </tbody>
</table>
<br>

#

#### **03. Atrapando lluvia <br> Nombre del proyecto:** block05-03-03-rain
Dados N números enteros no negativos representando un mapa de elevación, calcular cuál es el volumen de
agua que queda atrapada después de llover.

**Input**
- Una lista de números enteros en el rango 0 ≤ N ≤ 1000000 que definen la elevación del terreno en cada unidad del eje horizontal.

**Output**
- Imprimir por la salida estándar las unidades de agua que quedan atrapadas según el mapa de elevación.

<table style="width:100%">
    <thead>
        <tr>
            <th>Sample Input 1</th>
            <th>Sanple Output 1</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td align="center">4,2,0,3,2,5</td>
            <td align="center">9</td>
        </tr>
    </tbody>
</table>
<br>
<table style="width:100%">
    <thead>
        <tr>
            <th>Sample Input 2</th>
            <th>Sanple Output 2</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td align="center">0,1,0,2,1,0,1,3,2,1,2,1</td>
            <td align="center">6</td>
        </tr>
    </tbody>
</table>
<br>

# 

#### **04. Juego de saltos <br> Nombre del proyecto:** block05-03-04-jumps
Dada una lista de enteros no negativos de longitud L, comienzas en la posición del primer índice de la lista. Cada elemento de la lista, con valor N, representa la longitud máxima de salto en esa posición. Tu objetivo es llegar al último índice en el mínimo número de saltos.

Nota: Puedes asumir que siempre es posible llegar al último índice.

**Input**
- 1 <= L <= 100000
- 1 <= N <= 1000

**Output**
- Imprimir por la salida estándar el mínimo numero de saltos necesarios para llegar al último índice.

<table style="width:100%">
    <thead>
        <tr>
            <th>Sample Input 1</th>
            <th>Sanple Output 1</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td align="center">[2,3,1,1,4]</td>
            <td align="center">2</td>
        </tr>
    </tbody>
</table>
<br>
<table style="width:100%">
    <thead>
        <tr>
            <th>Sample Input 2</th>
            <th>Sanple Output 2</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td align="center">[2,3,0,1,4]</td>
            <td align="center">2</td>
        </tr>
    </tbody>
</table>
<br>

#

#### **05. Matriz Espiral <br> Nombre del proyecto:** block05-03-05-spiral-matrix
Dada una matriz m x n, devuelve todos los elementos de la matriz ordenados en forma de espiral.

**Input**
- m == matriz.length
- n == matriz[i].length
- 1 <= m, n <= 10
- -100 <= matriz[i][j] <= 100

**Output**
-  Imprimir por la salida estándar el array resultante.

<table style="width:100%">
    <thead>
        <tr>
            <th>Sample Input 1</th>
            <th>Sanple Output 1</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td align="center">[[1,2,3],[4,5,6],[7,8,9]]</td>
            <td align="center">[1,2,3,6,9,8,7,4,5]</td>
        </tr>
    </tbody>
</table>
<br>
<table style="width:100%">
    <thead>
        <tr>
            <th>Sample Input 2</th>
            <th>Sanple Output 2</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td align="center">[[1,2,3,4],[5,6,7,8],[9,10,11,12]]</td>
            <td align="center">[1,2,3,4,8,12,11,10,9,5,6,7]</td>
        </tr>
    </tbody>
</table>
<br>

# 

#### **06. Subiendo escaleras <br> Nombre del proyecto:** block05-03-06-stairs
Estás subiendo una escalera de N escalones.<br>
Con cada paso puedes subir 1 o 2 escalones. ¿De cuántas maneras diferentes puedes subir la escalera?

**Input**
- Un número entero 1 ≤ N ≤ 45 indicando el número de escalones de la escalera.

**Output**
- Imprimir por la salida estándar el número de formas diferentes que existen para subir la escalera.

<table style="width:100%">
    <thead>
        <tr>
            <th>Sample Input 1</th>
            <th>Sanple Output 1</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td align="center">2</td>
            <td align="center">2</td>
        </tr>
    </tbody>
</table>
<br>
<table style="width:100%">
    <thead>
        <tr>
            <th>Sample Input 2</th>
            <th>Sanple Output 2</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td align="center">3</td>
            <td align="center">3</td>
        </tr>
    </tbody>
</table>
<br>

#

#### **07. Máximo beneficio <br> Nombre del proyecto:** block05-03-07-max-benefit
Se proporciona una lista de precios de stock en días consecutivos, de manera que el elemento
en posición i es el precio del stock en el día i.<br>
Calcular el máximo beneficio resultado de comprar un stock en un único día del listado y venderlo en un día posterior.

**Input**
-  Una lista de números enteros 0 ≤ N ≤ 1000 que define el precio del stock en cada día.

**Output**
-  Imprimir por la salida estándar el máximo beneficio que puede obtenerse con la transacción. Si no es posible obtener beneficio, imprimir 0.

<table style="width:100%">
    <thead>
        <tr>
            <th>Sample Input 1</th>
            <th>Sanple Output 1</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td align="center">7,1,5,3,6,4</td>
            <td align="center">5</td>
        </tr>
    </tbody>
</table>
<br>
<table style="width:100%">
    <thead>
        <tr>
            <th>Sample Input 2</th>
            <th>Sanple Output 2</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td align="center">7,6,4,3,1</td>
            <td align="center">0</td>
        </tr>
    </tbody>
</table>

#

#### **08. Cables <br> Nombre del proyecto:** block05-03-08-cables
El problema consiste en comprobar si es posible encontrar una ordenación de cables en la cual todos ellos están conectados formando un círculo.<br>
Cada cable tiene dos extremos y cada extremo puede ser un conectar macho (M) o hembra (H).<br>
La conexión de un cable con otro sólo es posible juntando conectores diferentes.

**Input**
- Un conjunto desordenado de cables representados mediante parejas de letras haciendo referencia al conector de sus extremos.

**Output**
- Imprimir por la salida estándar "true" si es posible conectar todos los cables, "false" en caso contrario.

<table style="width:100%">
    <thead>
        <tr>
            <th>Sample Input 1</th>
            <th>Sanple Output 1</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td align="center">HM</td>
            <td align="center">true</td>
        </tr>
    </tbody>
</table>
<br>
<table style="width:100%">
    <thead>
        <tr>
            <th>Sample Input 2</th>
            <th>Sanple Output 2</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td align="center">HH</td>
            <td align="center">false</td>
        </tr>
    </tbody>
</table>
<br>
<table style="width:100%">
    <thead>
        <tr>
            <th>Sample Input 3</th>
            <th>Sanple Output 3</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td align="center">HM HH MM</td>
            <td align="center">true</td>
        </tr>
    </tbody>
</table>

#

