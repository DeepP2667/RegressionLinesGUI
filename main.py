import numpy as np
import PySimpleGUI as sg
import matplotlib as plt
"""Regression Line 
   Gui to enter the points and gives the best fit line for the points.
   Calculations will be added later"""

layout=[[sg.Text("How many points would you like to enter")],           #First window, enter # of points
        [sg.Input(key='points',size=(40,1))],
        [sg.Button('Enter'),sg.Button('Exit')]]

def layout2(value):                                                     #Second window, enter each point

    layout2=[[sg.Text("Enter points   Column 1: X   Column 2: Y")]]
    for i in range(value):
        layout2+=[[sg.Text("Point {}".format(i)), sg.Input(key='x{}'.format(i),size=(80,1)), sg.Input(key='y{}'.format(i),size=(80,1))]]
    layout2+=[[sg.Button('Enter'),sg.Button('Exit')]]
    return layout2

def insertscroll(layout2):                                              #Add a scroll for numbers not fitting on screen

    layout2_scroll=[[sg.Column(layout2,scrollable=True,size=(1500,1500))]]
    return layout2_scroll






window=sg.Window('Enter points',layout).Finalize()
while True:
    events, values = window.read()
    if(events==sg.WINDOW_CLOSED or events=='Exit'):
        break
    if(events=='Enter'):
        number_of_points=int(float(values['points']))
        layout2=layout2(number_of_points)
        layout2_scroll = insertscroll(layout2)
        window2=sg.Window("Enter points",layout2_scroll).Finalize()
        window2.maximize()
        events2, values2= window2.read()


        if(events2=='Exit' or events2==sg.WINDOW_CLOSED):
            window2.close()




window.close()

