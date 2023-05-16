##se importa la libreria para el manejo de arreglos 'arrrays'
import numpy as np

##definicion de arreglos en 1 dimension o vectores

arr_id = np.array([2,5,9,20,30])

##se imprimen los datos del arreglo con numpy
##print(arr_id);


##se acceden a valores del arreglo

##print(arr_id[0:1])

##se acceden a los valores usando operadores relacionales
##se imprimen los valores mayores a 10
##print(arr_id[arr_id > 10])

###****Se Definene arreglos en 2 dimensiones o matrices

arr_2d = np.array([[2,5,9,20,30],[4,10,18,40,60]])
##se imprime el arreglo de dos dimensiones
##print(arr_2d);

##accedememos al arreglo multidimensional, 
# print(arr_2d[0,1]) ##accedemos al arreglo 1 y elemento segundo 
# print(arr_2d[1,2]) ##accedemos al arreglo 2 y elemento tercero


##realizamos un calculo con los varlores de un arreglo en dos dimensiones
sumaArreglo2D =  arr_2d[0] + arr_2d[1]
##sumamos cada posicion del arreglo de dos dimensiones y apartir de el, se crea un arreglo con la suma de la posiciones de los dos arreglos

##print(sumaArreglo2D) ##imprimimos el resultado de arriba

##*****Creamos un arreglo de dos dimensiones *****####

arr_3D = np.array([[2,5,9,20,30],[4,10,18,40,60],[0,1,0,0,1]])
##print(arr_3D)  ###imprimimos un arreglo en 3D


##Accedemos a los valores de un arreglo en 3D

##imprimimos los elementos del arreglo tercero
##print(arr_3D[2,:])
##print(arr_3D[1,0:2]) ##accedemos al arreglo 2 y traemos los elementos que hay entre la posicion del 0 a 2
##print(arr_3D[2,4]) ##accedemos el arreglo tercero y tomamos el elemento de la posicion 4
##print(arr_3D[0:2,])   ##tomamos todos los elementos que hay entre el arreglo 0 al 2
##print(arr_3D[0,1:3])  ##imprimimos todos los elementos que hay entre la posicion 1 al 3 del arreglo 0 



###Realizamos operaciones en nuestro arreglo de tercerra dimension


multiplicacion3rdArray =  arr_3D[0] * arr_3D[2]  ##se multiplica el arreglo de posicion 0 y el arreglo de posicion 2, se multiplica cada posicion

##print(multiplicacion3rdArray)  ##se imprime un array con la multiplicacion de la posicion de los arreglos


calculos3rdArray = (arr_3D[0] + arr_3D[1] * arr_3D[2])

print(calculos3rdArray)  

