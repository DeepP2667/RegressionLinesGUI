import numpy as np
import PySimpleGUI as sg
import matplotlib.pyplot as plt


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
    options = [[sg.Text("Pick a calculation you would like to see")]]

    options += [[sg.Button('Mean'), sg.Button('Standard Deviation'), sg.Button('Z Scores'), sg.Button('Residuals'), sg.Button('Correlation Coefficient')]]

    options += [[sg.Button('Show graph'), sg.Button('Back'), sg.Button('Exit')]]

    return sg.Window('Different Options', options, finalize=True)


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

def slope_intercept(x_values,y_values):            #Plotting the regression line
    x = np.array(x_values)
    y = np.array(y_values)

    m, b = np.polyfit(x, y, 1)

    return x, y, m, b


def zscores(x_values, y_values):
    x_mean = np.mean(x_values)
    y_mean = np.mean(y_values)
    x_std = np.std(x_values)
    y_std = np.std(y_values)
    x_zscore = (x_values - x_mean) / x_std
    y_zscore = (y_values - y_mean) / y_std


    return x_zscore , y_zscore



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
                window2_clear(window2,number_of_points)             #Clear all inputs in window2


            if (events2 == 'Enter'):
                x_values, y_values = ([] for i in range(2))                 # Sets x and y values back to [], avoid replotting the same points
                window2.hide()
                x_label = values2['xlabel']                      #Asks for x and y label
                y_label = values2['ylabel']
                for i in range(1, number_of_points + 1):
                    x_values.append(float(values2['x{}'.format(i)]))    #Appends all user inputed valeus to x and y lists
                    y_values.append(float(values2['y{}'.format(i)]))

                window3 = options_layout()                         #Creates window3
                window3.maximize()

                plot(x_values, y_values, x_label, y_label)          #Plots it



                while True:
                    events3 , values3 = window3.read()

                    if events3 == 'Show graph':
                        plot(x_values, y_values, x_label, y_label)  #Show graph/fixed where you cannot see graph when clicking options

                    if events3 == 'Back':                   #Goes back to window2
                        window2.un_hide()
                        window3.close()
                        break

                    if events3 == 'Exit' or events3 == sg.WINDOW_CLOSED:    #Exit
                        window.close()
                        window2.close()
                        window3.close()
                        break

                    if events3 == 'Mean':                       #Popup of Means
                        sg.popup_scrolled("X mean: {}".format(np.mean(x_values)),
                                 "Y mean: {}".format(np.mean(y_values)),
                                          title='Means',
                                          image='C:/Users/deepp/Desktop/Python/RegressionGUI_Images/mean_orig.png',
                                          size=(44,1))

                    if events3 == 'Standard Deviation':         #Popup of Standard Dev.
                        sg.popup_scrolled("X Standard Deviation: {}".format(np.std(x_values)),
                                 "Y Standard Deviation: {}".format(np.std(y_values)),
                                          title='Standard Deviation',
                                          image='C:/Users/deepp/Desktop/Python/RegressionGUI_Images/StandardDeviation.png')

                    if events3 == 'Z Scores':                   #Popup for Z Scores
                        x_zscores , y_zscores = zscores(x_values,y_values)
                        sg.popup_scrolled("Z Scores (X): {}".format(x_zscores),
                                 "Z Scores (Y): {}".format(y_zscores),
                                          title='Z Scores',
                                          image='C:/Users/deepp/Desktop/Python/RegressionGUI_Images/ZScore.png')

                    if events3 == 'Residuals':                  #Popup for Residuals
                        x, y, m, b = slope_intercept(x_values,y_values)
                        residual = y - (m*x+b)
                        sg.popup_scrolled("Residuals: {}".format(residual),
                                          title='Residuals',
                                          image='C:/Users/deepp/Desktop/Python/RegressionGUI_Images/Residuals.png')

                    if events3 == 'Correlation Coefficient':            #Popup for Correlation Coefficient
                        r=np.corrcoef(x_values,y_values)
                        sg.popup_scrolled("Correlation Coefficient: {}".format(r),
                                          title='Correlation Coefficient',
                                          image='C:/Users/deepp/Desktop/Python/RegressionGUI_Images/Correlation_Coefficient.png')


window.close()






