import PySimpleGUI as sg


layout = [
    [sg.Text('Text', enable_events= True, key='-TEXT-'), sg.Spin(['item1', 'item 2'])],
    [sg.Button('Button', key='-BOTAO1-')],
    [sg.Input(key = '-INPUT-')],
    [sg.Text('Teste'), sg.Button('Teste2', key='-BOTAO2-')]
]

window = sg.Window('Conversor',layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == '-BOTAO1-':
        print(values['-INPUT-'])

    if event == '-BOTAO2-':
        print('Bitch!')

    if event == '-TEXT-':
        print('print')

window.close() 