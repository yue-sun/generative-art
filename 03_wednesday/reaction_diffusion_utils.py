import numpy as np
import matplotlib
import matplotlib.cm as cm
import matplotlib.pyplot as plt

def get_hex(name):
    ''' Return Hex color codes.'''
    if name == 'pastel rainbow':
        hex = ['#FF6663', '#FEB144', '#FDFD97', '#FFFFFF', '#9EE09E', '#9EC1CF', '#CC99C9']
    elif name == 'great wave':
        hex = ['#24476A', '#286991', '#ECBF9E', '#FFFFFF', '#EBD7B2', '#24476A', '#F6F4E7']
    elif name == 'girl pearl earring':
        hex = ['#211F2C', '#4366A3', '#E3A337', '#FFFAF5', '#F3CD89', '#6B8DAF', '#000000']
    elif name == 'starry night':
        hex = ['#DB901C', '#E1BC4F', '#D6D297', '#FFFFFF', '#ADC1D1', '#39648D', '#343564']
    elif name == 'water lilies':
        hex = ['#9F4640', '#FBCBCB', '#D09B66', '#5B764D', '#B49DEF', '#D3CDFB', '#395A92']
    elif name == 'sunset':
        hex = ['#FB92B8', '#A9A7EB', '#A9A7EB', '#7772B6', '#F98D94', '#16498A', '#08183A']
    # Add your own color palette here!
    else:
        raise NotImplementedError('Custom colormap name not implemented!')
    return hex

def custom_cmap(name):
    ''' Create a custom colormap.'''
    # Denote colorbar limits
    cmin, cmax = 0.2, 1.0

    # Set color intervals
    dc = cmax - cmin
    cvals = [cmin, cmin+dc/3., cmin+dc/3.+dc/12., cmin+dc/2., \
            cmin+dc/2.+dc/12., cmax-dc/3., cmax]
    norm = plt.Normalize(min(cvals), max(cvals))

    # Check if Hex color codes has the same length as cvals
    # You can modify cvals to use more colors
    hex = get_hex(name)
    if len(hex) != len(cvals):
        raise ValueError('Custom colormap needs to have the same length as cvals!')
    
    # Create custom colormap
    tuples = list(zip(map(norm, cvals), hex))
    cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", tuples)
    return cmap