import os as os
from tkinter import *
import matplotlib
#matplotlib.use("agg")
matplotlib.use("TkAgg") # sudo apt-get install python3-tk
import matplotlib.pyplot as plt
from matplotlib import rcParams
from pylab import figure
import numpy as np

rcParams['axes.labelsize'] = 14
rcParams['xtick.labelsize'] = 14
rcParams['ytick.labelsize'] = 14
rcParams['legend.fontsize'] = 12

rcParams['font.family'] = "Dejavu Sans"
rcParams['font.serif'] = ["Computer Modern Roman"]

rcParams['xtick.major.pad'] = 12
rcParams['ytick.major.pad'] = 12


def simple_bar(y_data):
    # https://python-graph-gallery.com/12-stacked-barplot-with-matplotlib/
    # y-axis in bold

    print("\ny_data\n", y_data)
    # Heights (sums) of all
    summed_bars = []
    for idx, values in enumerate(y_data[0]):
        summer = 0
        for jdx in range(len(y_data)):
            summer = summer + y_data[jdx][idx]
            print("x", y_data[jdx][idx], summer)
        print()
        summed_bars.append(summer)

    print("\n\nsummed_bars", summed_bars)

    # The position of the bars on the x-axis
    r = list(np.arange(0, len(y_data[0]), 1))

    print("\n\nr", r)

    # Names of group and bar width
    names = ['A','B','C','D','E']
    barWidth = 1

    # Create brown bars
    plt.bar(r, summed_bars, color='green', edgecolor='white', width=barWidth)
    # # Create green bars (middle), on top of the firs ones
    # plt.bar(r, bars2, bottom=bars1, color='#557f2d', edgecolor='white', width=barWidth)
    # # Create green bars (top)
    # plt.bar(r, bars3, bottom=bars, color='#2d7f5e', edgecolor='white', width=barWidth)

    # Custom X axis
    plt.xticks(r, names, fontweight='bold')
    plt.xlabel("group")
    plt.tight_layout(pad=0.9, w_pad=0.5, h_pad=1.0)

    # Show graphic
    plt.show()



def test_plot(x_data=None,
              y_data=None,
              ls_var="--",
             col_var="RAND",
             lw_var=1.0,
             alpha1_var=0.5,
             title_var="null",
             fig_name="null.png",
             ylim_var=False,
             xlim_var=False,
             main_label=None,
             labels=None):

    fig = figure()
    plt.xticks(rotation=15)
    plt.title(title_var)

    axhell = plt.subplot(1, 1, 1)

    axhell.grid(True)
    axhell.set_title(title_var)
    #axhell.axhline(y=2.0, color="grey", linestyle='dashed', lw=1.5)

    for idx, values in enumerate(x_data):
        print()
        print(labels[idx])
        print(x_data[idx])
        print(y_data[idx])

        axhell.plot(x_data[idx],
                    y_data[idx],
                    ls=ls_var,
                    lw=1.0,
                    alpha=1.0,
                    label=labels[idx])

    plt.tight_layout(pad=0.9, w_pad=0.5, h_pad=1.0)
    plt.show()

    return


