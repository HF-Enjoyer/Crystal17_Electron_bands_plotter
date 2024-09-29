#functions

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
    
