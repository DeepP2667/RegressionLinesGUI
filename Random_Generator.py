import numpy as np
import PySimpleGUI as sg
import matplotlib.pyplot as plt
"""Regression Line 
   With random numbers generated instead up to 1000"""

sg.theme('darkgrey9')
layout =[[sg.Text("How many points would you like to enter")],           #First window, enter # of points
        [sg.Input(key='points',size=(40,1))],
        [sg.Button('Enter'),sg.Button('Exit')]]

window = sg.Window("Main Menu",layout).Finalize()

while True:
    events, values = window.read()

    if events == sg.WINDOW_CLOSED or events=='Exit':
        break

    if events=='Enter':
        x_values = []
        y_values = []
        for i in range(int(values['points'])):
            x_values.append(np.random.uniform(1000))
            y_values.append(np.random.uniform(1000))

        round_x = np.round(x_values, 2)                         #Round x and y to 2 decimals
        round_y = np.round(y_values, 2)
        window.close()

window.close()
plt.figure(figsize=(8.5,4.8), dpi=90)
plt.plot(round_x,round_y,'ro')

m , b = np.polyfit(round_x,round_y,1)
plt.plot(round_x,m*round_x+b,'k')
plt.show()




