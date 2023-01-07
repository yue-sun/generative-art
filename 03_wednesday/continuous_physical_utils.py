import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
import matplotlib.animation as animation

def get_colors_alpha(theta, colormap='hsv'):
    ''' Calculate RGB colors from a matplotlib colormap by
        mapping an array of periodic values (0 to 2*pi) to
        RGBA color channels of a matplotlib colormap; also
        change alpha values based on the trail index.
        Inputs:
            theta - the array of values in trail (N, ntrail)
            colormap - the name of the colormap to use
        Outputs:
            colors - RGB colors
    '''
    N, ntrail = theta.shape                 # extract the trail dimensions
    theta = np.mod(theta.ravel(), 2*np.pi)  # shift all theta to [0,2*pi], since all values are cyclic
    norm = Normalize(vmin=0., vmax=2*np.pi) # set the color range from [0,2*pi]
    cmap = plt.get_cmap(colormap)           # get the colormap object
    colors = cmap(norm(theta))              # evaluate the colormap to get color channels (RGBA)   
    # Gradually decrease the opacity
    for i in range(ntrail):
        colors[N*i:N*(i+1), -1] = 0.8 - (0.8-0.1)/ntrail*i
    return colors
    
def plot_trail(x, y, theta, trail, colormap, ax):
    ''' Plot the trail of the swarmalators.'''
    colors = get_colors_alpha(theta, colormap)
    scat = ax.scatter(x[:,-trail:],y[:,-trail:], color=colors, s=110)
    return scat

def update_scatter(scat, x, y, theta, colormap):
    ''' Take an existing scatter object and update positions
        and colors (used for animation).'''
    scat.set_offsets(np.stack((x,y), axis=-1))
    colors = get_colors_alpha(theta, colormap)
    scat._facecolors = colors
    scat._edgecolors = colors

def animate_swarm_trail(out, ntrail, colormap='hsv'):
    ''' Animate the Swarmalator model over time with trail.'''
    fr = 2
    trail = min([ntrail,fr])
    frames = out.shape[-1]

    # Initialize trail plot
    fig, ax = plt.subplots(1, 1, figsize=(6,6))
    x, y, theta = out[0,:,:fr], out[1,:,:fr], out[2,:,:fr]
    swarm_trail = plot_trail(x, y, theta, trail, colormap, ax)
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    fig.tight_layout()

    def animate(i):
        '''Plot updates for animation.'''
        fr = i+2
        trail = min([ntrail,fr])
        
        x, y, theta = out[0,:,fr-trail:fr], out[1,:,fr-trail:fr], out[2,:,fr-trail:fr]
        update_scatter(swarm_trail, x.ravel(), y.ravel(), theta, colormap)
        
        return swarm_trail

    ani = animation.FuncAnimation(fig, animate, frames=frames-2, interval=20, blit=False)
    plt.close(fig)
    return ani