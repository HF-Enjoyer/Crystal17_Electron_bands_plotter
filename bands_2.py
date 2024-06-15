import numpy as np
import matplotlib.pyplot as plt

#-----------------------------------------------------------------------------------------------------------------------
# filename with extension:
filename = 'Example.BAND'

# SETUP
figsize = (10, 10) # size of the final bands plot figure
title = ('Band structure', 16) # title of the plot
y_title = ('Energy, eV', 14) # title of y-axis of the plot
labels = ['M', 'R', r'$\Gamma$', 'X', 'M'] # add BZ path!!!
bz_labels_size = 14 # fontsize for labels mentioned above
grid = 1 # leave 1 if you want grid. otherwise put 0

# Saving plot
save_fig = 0 # put 1 if you want to save image in png
png_name = 'your_bands1.png' # file name of the image
dpi = 720 # dpi

# OPTIONS
# custom limits of y-axis
custom_ylims = 0 # if 1, then ylims are adjustable below
custom_limits = (-10, 10) # set them in ev!

# PLOT FERMI LEVEL HORIZONTAL LINE, if 1, then it plots. if 0, it doesnot
plot_fermi = 0
fermi_level_color = 'blue' # e.g. in blue. you may set it to 'red', 'green' or whatsoever

# PLOT LINE CONNECTING the transition between valence band top and connection band bottom
plot_direct = 0 # I recommend not to use it because I have not figured out yet how to code it properly.
#  It works in simple cases with even number of bands

#-----------------------------------------------------------------------------------------------------------------------

def Fermi_level(filename): # to extract fermi energy in a.u.
    with open(filename, 'r') as inpf:
        for line in inpf:
            pass
        E_Fermi = float(line[-9:])
    return E_Fermi

def at_counter(filename):
    with open(filename, 'r') as inpf:
        nrows = 0
        for l in inpf:
            if '@' in l:
                nrows += 1
            elif '#' in l:
                nrows += 1
            else:
                pass
    return nrows

def Ticks_extractor(filename):
    with open(filename, 'r') as inpf:
        ticks = []
        ticklabels = []
        for line in inpf:
            if '@ XAXIS TICKLABEL    ' in line:
                ticklabels.append(line.split('"')[1])
            if '@ XAXIS TICK    ' in line:
                ticks.append(float(line[-8:-1]))
        return tuple(zip(ticks, ticklabels))
    
nrows = at_counter(filename) - 1

bands = np.loadtxt(filename, comments='#', skiprows=nrows)

# Plotting block

band_x = bands[:,0] # X axis range
xlims = (band_x[0], band_x[-1]) # X axis lims
nbands = bands.shape[1] # number of bands

band_y = (bands[:,1:nbands] + Fermi_level(filename))*27.2114
# limits of Y axis
if custom_ylims == 1:
    ylims = custom_limits
else:
    ylims = (np.amin(band_y), np.amax(band_y)) 

fig, ax = plt.subplots(figsize=figsize)
ax.set_title(title[0], fontsize=title[1])

ax.plot(band_x, band_y, color='black', linewidth=0.75) # here you can change linewidth, but i recommend to use current value
ax.set_ylabel(y_title[0], fontsize=y_title[1])
ax.set_xticks([Ticks_extractor(filename)[i][0] for i in range(len(Ticks_extractor(filename)))])
ax.set_xticklabels(labels, fontsize=bz_labels_size)

# зlots fermi level if 1
if plot_fermi == 1:
    plt.axhline(Fermi_level(filename)*27.2114, color='blue', linewidth=1.0)

if plot_direct == 1:
    Evb = (np.max(bands[:, nbands//2])+Fermi_level(filename))*27.2114
    Xvb = bands[:,0][np.argmax(bands[:, nbands//2])]
    Ecb = (np.min(bands[:, nbands//2 + 1])+Fermi_level(filename))*27.2114
    Xcb = bands[:,0][np.argmin(bands[:, nbands//2 + 1])]
    plt.plot([Xcb, Xvb], [Ecb, Evb], color='gray', ls='--', linewidth=0.95)

plt.xlim(Ticks_extractor(filename)[0][0], Ticks_extractor(filename)[-1][0])
plt.ylim(ylims)

if grid == 1:
    plt.grid()
    
if save_fig == 1:
    plt.savefig(png_name, dpi=dpi, bbox_inches="tight")
plt.show()
