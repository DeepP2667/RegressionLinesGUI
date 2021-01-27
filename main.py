import numpy as np
import PySimpleGUI as sg
import matplotlib.pyplot as plt
import time

"""Regression Line 
   Gui to enter the points and gives the best fit line for the points.
   Calculations will be added later"""

sg.theme('darkgrey9')

layout = [[sg.Text("How many points would you like to enter")],           #window, enter # of points
        [sg.Input(key='points',size=(40,1))],
        [sg.Button('Enter'),sg.Button('Exit')]]


def layout2(value):                                                       #window2, enter each point

    layout2 = [[sg.Text("Column 1: X   Column 2: Y")],
              [sg.Text("X Label: "),sg.Input(size = (40,1),key = 'xlabel')],
              [sg.Text("Y Label: "),sg.Input(size = (40,1),key = 'ylabel')]]
    for i in range(1,value+1):
        layout2 += [[sg.Text("Point {}".format(i)), sg.Input(key='x{}'.format(i),size=(80,1)), sg.Input(key='y{}'.format(i),size=(80,1))]]
    layout2 += [[sg.Button('Enter'), sg.Button('Clear'), sg.Button('Main Menu'), sg.Button('Exit')]]

    layout2_scroll = [[sg.Column(layout2, scrollable=True, size=(1500, 1500))]]         #Adds scroll
    return sg.Window("Points", layout2_scroll, finalize=True)


def window2_clear(window2,number_of_points):              #To clear window2
    for i in range(1, number_of_points + 1):
        window2['x{}'.format(i)].update('')
        window2['y{}'.format(i)].update('')
    window2['xlabel'].update('')                          #Updates with blank
    window2['ylabel'].update('')
    return window2


def options_layout():                           #All different calculations with regression, window3
    stat_options = [[sg.Text("Pick a calculation you would like to see")]]

    #All buttons for calculations

    stat_options += [[sg.Button('Back'), sg.Button('Exit')]]

    return sg.Window('Different Options', stat_options, finalize=True)


def plot(x_values,y_values,x_label,y_label):            #Plotting the regression line
    x = np.array(x_values)
    y = np.array(y_values)
    plt.plot(x, y, 'bo')

    zip_xy = zip(x, y)
    print("Points: ", list(zip_xy))                   #Prints each point coordinate

    m, b = np.polyfit(x, y, 1)
    plt.plot(x, m * x + b, 'r', label="Best Fit Line")

    plt.title("Regression Line")
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend()
    plt.show()
                        #Clearing plot
    plt.clf()
    plt.cla()
    plt.close()





window=sg.Window('Main Menu',layout).Finalize()             #First window
x_values = []                                         #X and Y values list
y_values = []

while True:             #First event loop
    events, values = window.read()

    if(events==sg.WINDOW_CLOSED or events=='Exit'):     #Exit
        window.close()
        break


    if(events=='Enter'):
        window.hide()                                                    #Hide window
        number_of_points = int((values['points']))                       #Get number of points
        window2 = layout2(number_of_points)                              #Creates window2
        window2.maximize()

        while True:
            events2, values2 = window2.read()

            if (events2 == 'Exit' or events2 == sg.WINDOW_CLOSED):      #Exit
                window.close()
                window2.close()
                break

            if (events2 == 'Main Menu'):  # Return to main menu/window 1
                window.un_hide()
                window2.close()
                break

            if events2 == 'Clear':
                window2=window2_clear(window2,number_of_points)    #Clear all inputs in window2
                break

            if (events2 == 'Enter'):
                window2.hide()
                x_label = values2['xlabel']                      #Asks for x and y label
                y_label = values2['ylabel']
                for i in range(1, number_of_points + 1):
                    x_values.append(float(values2['x{}'.format(i)]))    #Appends all user inputed valeus to x and y lists
                    y_values.append(float(values2['y{}'.format(i)]))

                window3 = options_layout()                         #Creates window3
                window3.maximize()
                plot(x_values, y_values, x_label, y_label)          #Plots it

                x_values, y_values = ([] for i in range(2))       #Sets x and y values back to [], avoid replotting the same points

                while True:
                    events3 , values3 = window3.read()

                    if events3 == 'Back':                   #Goes back to window2
                        window2.un_hide()
                        window3.close()
                        break

                    if events3 == 'Exit' or events3 == sg.WINDOW_CLOSED:    #Exit
                        window.close()
                        window2.close()
                        window3.close()
                        break

window.close()






