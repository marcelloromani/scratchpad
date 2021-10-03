import PySimpleGUI as sg

layout = [
    [sg.Text('My one-shot window.')],
    [sg.InputText(key='test-input')],
    [sg.Submit(), sg.Cancel()]
]

window = sg.Window('Window Title', layout)

event, values = window.read()
window.close()

text_input = values['test-input']
sg.popup('You entered', text_input)
