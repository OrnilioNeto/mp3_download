from processamento import ExportReport
from PySimpleGUI import PySimpleGUI as sg
from datetime import datetime, timedelta
import re

class Interface:
    def execute(self):
        sg.theme('Reddit')
        layout = [
            [sg.Text('Bandas', size=(7,1)),sg.Input(key='busca', size=(30,1))],
            [sg.Button(button_text='Baixar', key='next')]
        ]

        janela = sg.Window('Login', layout)  
        while True:
            eventos, valores = janela.read()
            if eventos == sg.WINDOW_CLOSED:
                break
            if eventos == 'next':
                bandas = valores['busca']
                print(bandas)
                seguir = ExportReport()
                seguir.processar(bandas)
                
                
                
            # if seguir:
            #     janela['busca'].set_focus()

        
        

    