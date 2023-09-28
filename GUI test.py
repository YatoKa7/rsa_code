import PySimpleGUI as sg
import random
print("Hello world")
def update():
    r = random.randint(1,10)

    text_elem = window['-text-'] #

    text_elem.update("Your random numbers: {}".format(r))#

    

    
layout = [[sg.Button('Click!', enable_events=True, key='-FUNCTION-', font='Helvetica 16')],
              
        [sg.Text('Your numbers', size=(25, 1), key='-text-', font='Helvetica 16')]] #

window = sg.Window('Randomizer', layout, size=(350,100))

while True:

        event, values = window.read()

        if event in (sg.WIN_CLOSED, 'Hajox'):
            break

        if event == '-FUNCTION-':

            update()

window.close()