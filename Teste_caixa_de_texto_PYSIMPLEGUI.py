import PySimpleGUI as sg

layout = [[sg.Text('Jogar o dado? ')],
[sg.Button('Sim')], [sg.Button('Não')]]

window = sg.Window('Caixa de texto_teste', layout)

while True:
	event, values = window.read()
	if event == sg.WIN_CLOSED or event == 'Não':
		break
		print('You entered ', values[0])
window.close()
