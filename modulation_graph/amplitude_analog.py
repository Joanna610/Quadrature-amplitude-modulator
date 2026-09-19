# inspo: https://github.com/gwoptics/learn_laser_interferometry/blob/784c23507742673062eca9f79c8e7ca125257b2f/02_Plane_waves/03_Optical_modulation/02_Amplitude_modulation.ipynb

import numpy as np                         # Importing numpy
import matplotlib                          # For plotting
import matplotlib.pyplot as plt                   
from pykat import finesse                  # Importing the pykat.finesse package
from pykat.commands import *               # Importing all packages in pykat.commands.
from IPython.display import display, HTML  # Allows us to display HTML.

# Telling the notebook to make plots inline.
# %matplotlib inline      
# Initialises the PyKat plotting tool. Change the dpi value 
# to adjust size of figures on your screen.
pykat.init_pykat_plotting(dpi=90)   

## Code for showing a phase modulated field ##

# Parameters
# --------------------------------------------------
t = np.linspace(0,1,2048)   # Time array
E0 = 1                      # Amplitude of the field.
fc = 20                     # Carrier freq
phi_c = 0                   # Phase of the field
fm = 2                      # Phase modulation freq
m = 0.9                     # Modulation index [0,1]
phi_m = 0                   # Modulation phase

# Computing the fields and signal arrays
# --------------------------------------------------
# Carrier field
E = E0*np.cos(fc*2*np.pi*t + phi_c)
# Signal 
x = m*np.sin(fm*2*np.pi*t + phi_m)
# Phase modulated field
E_m = E0*np.cos(fc*2*np.pi*t + phi_c)*(1 - (m/2)*(1-np.sin(fm*2*np.pi*t+phi_m) ))

# Plotting
# --------------------------------------------------
# fig = plt.figure(figsize=(10,3))

# # Axis for carrier and modulated field
# ax = plt.subplot(1,1,1)
# p1 = ax.plot(t,E,'0.7', label='$\mathrm{Carrier}\ E_c(t)$')
# p2 = ax.plot(t,E_m,'r',label='$\mathrm{Mod. field}\ E_m(t)$')
# ax.set_xlabel('t')
# ax.set_ylabel('E(t)')
# ax.set_title('Amplitude modulation')
# ax.set_xlim(-0.01,1.01)

# # Second y-axis for signal
# ax2 = ax.twinx()
# p3 = ax2.plot(t,x,'b', label='$\mathrm{Signal}\ x(t)$')
# ax2.set_ylabel('x(t)')

# # The legend
# plots = p1+p2+p3
# labs = [lab.get_label() for lab in plots]
# ax.legend(plots, labs, loc=1, fontsize=10)

# # Showing figure
# plt.show(fig)


fig1, ax1 = plt.subplots(figsize=(10,5))
ax1.plot(t, E, '0.7', label='$\mathrm{Carrier}\ E_c(t)$', lw=3)
ax1.set_xlabel('t')
ax1.set_ylabel('E(t)')
plt.tight_layout()
plt.savefig("amplitude_carrier.png", dpi=300, bbox_inches="tight")

fig2, ax2 = plt.subplots(figsize=(10,5))
ax2.plot(t, x,'b', label='$\mathrm{Signal}\ x(t)$', lw=3)
ax2.set_xlabel('t')
ax2.set_ylabel('E(t)')
plt.tight_layout()
plt.savefig("amplitude_signal.png", dpi=300, bbox_inches="tight")


fig3, ax3 = plt.subplots(figsize=(10,5))
ax3.plot(t, E_m,'darkblue',label='$\mathrm{Mod. field}\ E_m(t)$', lw=3)
ax3.set_xlabel('t')
ax3.set_ylabel('E(t)')
plt.tight_layout()
plt.savefig("amplitude_modulation.jpg", dpi=300, bbox_inches="tight")