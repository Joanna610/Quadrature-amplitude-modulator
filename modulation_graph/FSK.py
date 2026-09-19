import numpy as np
import matplotlib.pyplot as plt
from pykat import finesse                  # Importing the pykat.finesse package
from pykat.commands import *               # Importing all packages in pykat.commands.
from IPython.display import display, HTML  # Allows us to display HTML.

pykat.init_pykat_plotting(dpi=90)   


# Time parameters
fs = 1000
Tb = 0.2
bits = np.array([1,0,1,1,0,0,1])

# Frequencies
f0 = 5
f1 = 10

# Generate FSK signal
t_total = []
s_total = []

for i, bit in enumerate(bits):
    t = np.arange(0, Tb, 1/fs)

    if bit == 0:
        s = np.cos(2*np.pi*f0*t)
    else:
        s = np.cos(2*np.pi*f1*t)

    t_total.extend(t + i*Tb)
    s_total.extend(s)

t_total = np.array(t_total)
s_total = np.array(s_total)

# Time axis for bits
bit_t = np.arange(len(bits)+1) * Tb

# Two graphs
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

# FSK signal
axs[1].plot(t_total, s_total,'darkblue', linewidth=3)
axs[1].set_xlabel("t")
axs[1].set_ylabel("E(t)")
axs[1].grid(True)

plt.tight_layout()
plt.savefig("FSK.jpg", dpi=300, bbox_inches="tight")