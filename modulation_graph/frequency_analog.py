# inspo: https://github.com/gwoptics/learn_laser_interferometry/blob/784c23507742673062eca9f79c8e7ca125257b2f/02_Plane_waves/03_Optical_modulation/01_Phase_and_frequency_modulation.ipynb

import numpy as np                         # For numbers, arrays, matrices
import matplotlib                          # For plotting
import matplotlib.pyplot as plt                   
from pykat import finesse                  # Importing the pykat.finesse package
from pykat.commands import *               # Importing all packages in pykat.commands.
from IPython.display import display, HTML  # Allows us to display HTML.

# Telling the notebook to make plots inline.
# matplotlib inline      
# Initialises the PyKat plotting tool. Change the dpi value to adjust size 
# of figures on your screen.
pykat.init_pykat_plotting(dpi=90)    

## Code for showing a phase modulated field ##

# Parameters
# --------------------------------------------------
t = np.linspace(0,1,2048)   # Time array
E0 = 1                      # Amplitude of the field.
fc = 20                     # Carrier freq
phi_c = 0                   # Phase of the field
fm = 2                      # Phase modulation freq
m = 5                       # Modulation index
phi_m = 0                   # Modulation phase

# Computing the fields and signal arrays
# --------------------------------------------------
# Carrier field
E = E0*np.cos(fc*2*np.pi*t + phi_c)
# Signal 
x = m*np.sin(fm*2*np.pi*t + phi_m)
# Phase modulated field

# Frequency modulation
beta = 5
E_m = E0*np.cos(2*np.pi*fc*t + beta*np.cos(2*np.pi*fm*t))




# fig, axs = plt.subplots(3, 1, figsize=(10, 8), sharex=True)

# axs[0].plot(t, E, '0.7', label='$\mathrm{Carrier}\ E_c(t)$')
# axs[0].set_title("Carrier field")
# axs[0].set_xlabel('t')
# axs[0].set_ylabel('E(t)')

# axs[1].plot(t, x,'b', label='$\mathrm{Signal}\ x(t)$')
# axs[1].set_title("Signal")
# axs[1].set_xlabel('t')
# axs[1].set_ylabel('x(t)')

# axs[2].plot(t, E_m,'r',label='$\mathrm{Mod. field}\ E_m(t)$')
# axs[2].set_title("Phase-modulated field")
# axs[2].set_xlabel('t')
# axs[2].set_ylabel('E(t)')

# plt.tight_layout()
# plt.savefig("frequency_modulation.png", dpi=300, bbox_inches="tight")





# Plotting
# --------------------------------------------------
# fig = plt.figure(figsize=(10,3))

# Axis for carrier and modulated field
# ax = plt.subplot(1,1,1)
# p1 = ax.plot(t,E,'0.7', label='$\mathrm{Carrier}\ E_c(t)$')
# p2 = ax.plot(t,E_m,'r',label='$\mathrm{Mod. field}\ E_m(t)$')
# ax.set_xlabel('t')
# ax.set_ylabel('E(t)')
# ax.set_title('Phase modulation')
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
# plt.savefig("phase_modulation.png", dpi=300, bbox_inches="tight")

fig1, ax1 = plt.subplots(figsize=(10,5))
ax1.plot(t, E, '0.7', label='$\mathrm{Carrier}\ E_c(t)$', lw=3)
ax1.set_xlabel('t')
ax1.set_ylabel('E(t)')
plt.tight_layout()
plt.savefig("frequency_carrier.png", dpi=300, bbox_inches="tight")

fig2, ax2 = plt.subplots(figsize=(10,5))
ax2.plot(t, x,'b', label='$\mathrm{Signal}\ x(t)$', lw=3)
ax2.set_xlabel('t')
ax2.set_ylabel('E(t)')
plt.tight_layout()
plt.savefig("frequency_signal.png", dpi=300, bbox_inches="tight")


fig3, ax3 = plt.subplots(figsize=(10,5))
ax3.plot(t, E_m,'darkblue',label='$\mathrm{Mod. field}\ E_m(t)$', lw=3)
ax3.set_xlabel('t')
ax3.set_ylabel('E(t)')
plt.tight_layout()
plt.savefig("frequency_modulation.jpg", dpi=300, bbox_inches="tight")


# axs[0].plot(t, E, '0.7', label='$\mathrm{Carrier}\ E_c(t)$')
# axs[0].set_title("Carrier field")
# axs[0].set_xlabel('t')
# axs[0].set_ylabel('E(t)')

# axs[1].plot(t, x,'b', label='$\mathrm{Signal}\ x(t)$')
# axs[1].set_title("Signal")
# axs[1].set_xlabel('t')
# axs[1].set_ylabel('x(t)')

# axs[2].plot(t, E_m,'r',label='$\mathrm{Mod. field}\ E_m(t)$')
# axs[2].set_title("Phase-modulated field")
# axs[2].set_xlabel('t')
# axs[2].set_ylabel('E(t)')

# plt.tight_layout()
# plt.savefig("frequency_modulation.png", dpi=300, bbox_inches="tight")