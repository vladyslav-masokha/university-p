import random
import string
import PySimpleGUI as sg

custom_theme = {
    'BACKGROUND': '#FFFFFF',
    'TEXT': '#000000',
    'INPUT': '#FFFFFF',
    'TEXT_INPUT': '#000000',
    'SCROLL': '#FFFFFF',
    'BUTTON': ('#FFFFFF', '#000000'),
    'PROGRESS': ('#FFFFFF', '#000000'),
    'BORDER': 1,
    'SLIDER_DEPTH': 0,
    'PROGRESS_DEPTH': 0
}

sg.theme_add_new('CustomTheme', custom_theme)
sg.theme('CustomTheme')
    
layout = [
    [sg.Text('Uppercase: '), sg.Push(), sg.Input(key='-UP-')],
    [sg.Text('Lowercase: '), sg.Push(), sg.Input(key='-LOW-')],
    [sg.Text('Digits: '), sg.Push(), sg.Input(key='-DIT-')],
    [sg.Text('Characters: '), sg.Push(), sg.Input(key='-CHR-')],
    [sg.Button('Generate'), sg.Button('Cancel')],
    [sg.Text('Password: '), sg.Push(), sg.Multiline(no_scrollbar=True, disabled=True, key='-PASS-')]
]

windows = sg.Window('Password generator', layout)

while True:
    event, values = windows.read()
    
    if event == 'Cancel' or event == windows.was_closed:
        break
    
    if event == 'Generate':
        try:
            user_upper = int(values['-UP-'])
            user_lower = int(values['-LOW-'])
            user_digits = int(values['-DIT-'])
            user_characters = int(values['-CHR-'])
            
            upper = random.sample(string.ascii_uppercase, user_upper)
            lower = random.sample(string.ascii_lowercase, user_lower)
            digits = random.sample(string.digits, user_digits)
            characters = random.sample(string.punctuation, user_characters)
            
            password = lower+upper+digits+characters
            password = random.sample(password, len(password))
            password = ''.join(password)
            windows['-PASS-'].update(password)
        except ValueError:
            windows['-PASS-'].update('No Valid Number')
