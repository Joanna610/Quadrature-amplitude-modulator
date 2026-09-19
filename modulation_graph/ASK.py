import numpy as np
import matplotlib.pyplot as plt
from pykat import finesse                  # Importing the pykat.finesse package
from pykat.commands import *               # Importing all packages in pykat.commands.
from IPython.display import display, HTML  # Allows us to display HTML.

# Telling the notebook to make plots inline.
# %matplotlib inline      
# Initialises the PyKat plotting tool. Change the dpi value 
# to adjust size of figures on your screen.
pykat.init_pykat_plotting(dpi=90) 

# Time parameters
fs = 1000
Tb = 0.2
bits = np.array([1,0,1,1,0,0,1])

# Carrier
fc = 10
A = 1

# Generate ASK signal
t_total = []
s_total = []

for i, bit in enumerate(bits):
    t = np.arange(0, Tb, 1/fs)

    # Amplitude according to bit
    if bit == 0:
        amplitude = 0.2
    else:
        amplitude = A

    s = amplitude * np.cos(2*np.pi*fc*t+np.pi/2)

    t_total.extend(t + i*Tb)
    s_total.extend(s)

t_total = np.array(t_total)
s_total = np.array(s_total)

# Time axis for bits
bit_t = np.arange(len(bits)+1) * Tb

# Plot
fig, axs = plt.subplots(2, 1, figsize=(12, 10), sharex=True)

# Bit stream
axs[0].step(
    bit_t,
    np.r_[bits, bits[-1]],
    where='post',
    color='gray',
    linewidth=4
)
axs[0].set_ylabel("Bits")
axs[0].set_ylim(-0.2, 1.2)
axs[0].set_yticks([0, 1])

# ASK signal
axs[1].plot(
    t_total,
    s_total,
    color='darkblue',
    linewidth=3
)
axs[1].set_xlabel("t")
axs[1].set_ylabel("E(t)")
axs[1].grid(True)

plt.tight_layout()
plt.savefig("ASK.jpg", dpi=300, bbox_inches="tight")