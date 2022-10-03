from FileHelpers import csv_helpers
import matplotlib.pyplot as plt
import numpy as np

def line_plot(list1,list2):
    #define data
    x = np.array(list1)
    y = np.array(list2)

    #find line of best fit
    a, b = np.polyfit(x, y, 1)

    #add points to plot
    plt.scatter(x, y)

    #add line of best fit to plot
    plt.plot(x, a*x+b)
    plt.show()

def plot_relation(csv_file:str,x_loc=0,y_loc=1):
    x_axis = []
    y_axis = []
    lists = csv_helpers.read_csv(file_path=csv_file)
    for list in lists:
        x_axis.append(list[x_loc])
        y_axis.append(list[y_loc])
    line_plot(x_axis,y_axis)