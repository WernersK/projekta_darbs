import PySimpleGUI as sg
import os.path

# Define the layout of the window
#add menu bar
#add sg theme for winodw

#add logo of image from computer


#add sg theme for winodw
sg.theme('DarkGreen')   # Add a touch of color
#All the stuff inside your window
#add menu bar categries: Norādes, Rediģēt, Palidzība
layout = [
    [sg.Menu([
        ['&Fails', ['&Atvērt', '&Saglabāt', 'Iziet']],
        ['&Rediģēt', ['&Iekopēt', ['Piekrītu', ], 'Atgriezt'], ],
        ['&Rīks', ['---', '&1', '&2',
                        '---', '&3', '&4']],
        ['&Palidzība', '&Par...'], ])],
    [sg.Text("Ievadiet lietotajvārdu: "), sg.InputText()],
    [sg.Text("Ievadiet vārdu: "), sg.InputText()],
    [sg.Text("Ievadiet uzvārdu: "), sg.InputText()],
    [sg.Text("Ievadiet paroli: "), sg.InputText()],
    [sg.Button("Ievadīt"), sg.Button("Atcelt")]
]
#add logo of image from computer in the window
#os.path.dirname(os.path.abspath(__file__))
#logo = os.path.join(os, 'logo.png')
#layout = [[sg.Image(logo)],
              #[sg.Text('Some text on Row 1')],
              #[sg.Text('Enter something on Row 2'), sg.InputText()],
              #[sg.Button('Ok'), sg.Button('Cancel')]]



# Create the window
window = sg.Window("Reģistrācija", layout)

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Atcelt":
        break
    print("Jūs ievadījāt ", values[0], values[1], values[2])

# Finish up by removing from the screen
window.close()


sg.theme('DarkAmber')   # Add a touch of color
#All the stuff inside your window.
layout = [  [sg.Text('Ievadiet lietotajvārdu: '), sg.InputText()],
             [sg.Text('Ievadiet paroli'), sg.InputText()],
             [sg.Button('Ok'), sg.Button('Atcelt')] ]

# # Create the Window
window = sg.Window('Ienākt', layout)
#Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()


