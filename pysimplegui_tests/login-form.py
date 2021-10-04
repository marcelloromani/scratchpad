import PySimpleGUI as sg

layout = [
    [sg.Text('Username:'), sg.InputText(key='username')],
    [sg.Text('Password:'), sg.InputText(key='password')],
    [sg.Submit(), sg.Cancel()]
]

window = sg.Window('Login', layout)

event, values = window.read()
window.close()

username = values['username']
password = values['password']
sg.popup(f'Your credentials:\n{username}\n{password}\n\nEvent: {event}')
