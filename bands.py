from helps import *

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import sys


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python main.py <inp filename>')

    # filename with extension:
    filename = Path(__file__).with_name(sys.argv[1])

    # SETUP
    figsize = tuple([int(i) for i in input('size of the figure <x y>: ').split()])
    if len (figsize) != 2:
        print('size: <x y>')
    title = tuple(input('Title of the graph, fontsize <title, number>: ').split(', ')) #e.g. Band structure 16
    y_title = tuple(input('Title of y axis, fontsize e.g. <Energy, ev; 16>: ').split('; ')) #e.g. Energy 16
    labels = [str(i) for i in input('add BZ path  e.g. <M, Gamma, X, K, M>: ').split(', ')] # add BZ path
    for i in labels:
        if i == 'Gamma':
            labels[labels.index('Gamma')] = '$\\Gamma$'
    bz_labels_size = int(input('fontsize for BZ labels: ')) # fontsize for labels mentioned above
    grid = str(input('plot grid? <y/n>: ')) # leave 1 if you want grid. otherwise put 0

    #saving plot
    #save_fig = 0 # put 1 if you want to save image
    png_name = f'{title[0]}.png'
    dpi = 400

    #OPTIONS
    #custom limits on y axis
    custom_ylims = 0 # if 1, then ylims are adjustable below
    custom_limits = (-10, 10) # in ev!

    #PLOT FERMI LEVEL HORIZONTAL LINE, if 1, then it plots. if 0, it doesnot
    plot_fermi = str(input('Plot Fermi level? <y/n>: '))
    fermi_level_color = 'blue' # e.g. in blue. you may set it to 'red' or whatsoever

    #PLOT LINE CONNECTING the transition between valence band top and connection band bottom
    plot_direct = 0 # i recommend not to use it because i did not figure out how to code it properly

    nrows = at_counter(filename) - 1

    bands = np.loadtxt(filename, comments='#', skiprows=nrows)


    #plotting block

    band_x = bands[:,0] # X axis range
    xlims = (band_x[0], band_x[-1]) # X axis lims
    nbands = bands.shape[1] # number of bands

    band_y = (bands[:,1:nbands] + Fermi_level(filename))*27.2114
    # limits of Y axis
    if custom_ylims == 1:
        ylims = custom_limits
    else:
        ylims = (np.amin(band_y), np.amax(band_y)) 

    fig, ax = plt.subplots(figsize = figsize)
    ax.set_title(title[0], fontsize=int(title[1]))

    ax.plot(band_x, band_y, color='black', linewidth=0.75) # here you can change linewidth, but i recommend to use current value
    ax.set_ylabel(y_title[0], fontsize=y_title[1])
    ax.set_xticks([Ticks_extractor(filename)[i][0] for i in range(len(Ticks_extractor(filename)))])
    ax.set_xticklabels(labels, fontsize=bz_labels_size)

    #plots fermi level if 1
    if plot_fermi == 'y':
        plt.axhline(Fermi_level(filename)*27.2114, color='blue', linewidth=1.0)

    if plot_direct == 1:
        Evb = (np.max(bands[:, nbands//2 + 1])+Fermi_level(filename))*27.2114
        Xvb = bands[:,0][np.argmax(bands[:, nbands//2 + 1])]
        Ecb = (np.min(bands[:, nbands//2 + 2])+Fermi_level(filename))*27.2114
        Xcb = bands[:,0][np.argmin(bands[:, nbands//2 + 2])]
        plt.plot([Xcb, Xvb], [Ecb, Evb], color='gray', ls='--', linewidth=0.95)


    plt.xlim(Ticks_extractor(filename)[0][0], Ticks_extractor(filename)[-1][0])
    plt.ylim(ylims)

    if grid == 'y':
        plt.grid()

    plt.savefig(png_name, dpi=dpi, bbox_inches="tight")
    plt.show()
