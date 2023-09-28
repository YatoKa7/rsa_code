# подключаем библиотеки
import PySimpleGUI as sg
import random

# обрабатываем нажатие на кнопку
def update():
    # получаем новое случайное число
    r = random.randint(1,100)
    # получаем доступ к текстовому элементу
    text_elem = window['-text-']
    # выводим в него текст с новым числом
    text_elem.update("Your random numbers: {}".format(r))

# что будет внутри окна
# первым описываем кнопку и сразу указываем размер шрифта
layout = [[sg.Button('Новое число',enable_events=True, key='-FUNCTION-', font='Helvetica 16')],
        # затем делаем текст
        [sg.Text('Результат:', size=(25, 1), key='-text-', font='Helvetica 16')]]

# рисуем окно
window = sg.Window('Генератор случайных чисел', layout, size=(350,100))

# запускаем основной бесконечный цикл
while True:
    # получаем события, произошедшие в окне
    event, values = window.read()
    # если нажали на крестик
    if event in (sg.WIN_CLOSED, 'Exit'):
        # выходим из цикла
        break
    # если нажали на кнопку
    if event == '-FUNCTION-':
        # запускаем связанную функцию
        update()

# закрываем окно и освобождаем используемые ресурсы
window.close()