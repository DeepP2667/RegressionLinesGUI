import numpy as np
import PySimpleGUI as sg
import matplotlib.pyplot as plt
"""Regression Line 
   Gui to enter the points and gives the best fit line for the points.
   Calculations will be added later"""

sg.theme('darkgrey9')
layout=[[sg.Text("How many points would you like to enter")],           #First window, enter # of points
        [sg.Input(key='points',size=(40,1))],
        [sg.Button('Enter'),sg.Button('Exit')]]

def layout2(value):                                                     #Second window, enter each point

    layout2=[[sg.Text("Enter points   Column 1: X   Column 2: Y")]]
    for i in range(1,value+1):
        layout2+=[[sg.Text("Point {}".format(i)), sg.Input(key='x{}'.format(i),size=(80,1)), sg.Input(key='y{}'.format(i),size=(80,1))]]
    layout2+=[[sg.Button('Enter'),sg.Button('Main Menu'),sg.Button('Exit')]]
    return layout2

def insertscroll(layout3):                                              #Add a scroll for numbers not fitting on screen

    layout2_scroll=[[sg.Column(layout3,scrollable=True,size=(1500,1500))]]
    return layout2_scroll



window=sg.Window('Main Menu',layout).Finalize()
x_values=[]
y_values=[]
while True:
    events, values = window.read()
    if(events==sg.WINDOW_CLOSED or events=='Exit'):
        break



    if(events=='Enter'):
        window.hide()                                                       #Hide window
        number_of_points=int((values['points']))
        layout3=layout2(number_of_points)                                   #Adds the rows and columns to input points
        layout3_scroll = insertscroll(layout3)                              #Adds scroll

        window2=sg.Window("Enter points",layout3_scroll).Finalize()
        window2.maximize()

        events2, values2= window2.read()

        if(events2=='Exit' or events2==sg.WINDOW_CLOSED):
            break

        if(events2=='Main Menu'):                                           #Return to main menu
            window.un_hide()
            window2.close()

        if(events2=='Enter'):
            for i in range(1,number_of_points+1):
                x_values.append(float(values2['x{}'.format(i)]))
                y_values.append(float(values2['y{}'.format(i)]))
            window2.close()                                                 #Close all windows
            window.close()
            break

window.close()

if(x_values!=[]):                           #Stops it from the error where x/y_values is set to [] when user clicks exit
    x = np.array(x_values)
    y = np.array(y_values)
    plt.plot(x, y, 'bo')

    zip_xy = zip(x, y)
    print("Points: ", list(zip_xy))

    m, b = np.polyfit(x, y, 1)
    plt.plot(x, m * x + b, 'r', label="Best Fit Line")

    plt.title("Regression Line")
    plt.legend()
    plt.show()

