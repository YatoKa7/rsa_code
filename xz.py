import PySimpleGUI as sg
import random

def update():

    text_elem = window['-text-']
    text_elem.update("Your random numbers: {}".format(r))
    update()