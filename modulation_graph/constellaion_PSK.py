import numpy as np
import matplotlib.pyplot as plt
from pykat import finesse                  # Importing the pykat.finesse package
from pykat.commands import *               # Importing all packages in pykat.commands.
from IPython.display import display, HTML  # Allows us to display HTML.

pykat.init_pykat_plotting(dpi=90)  

M = 8

angles = np.linspace(0, 2*np.pi, M, endpoint=False)

I = np.cos(angles)
Q = np.sin(angles)

fig, ax = plt.subplots(figsize=(6,6))

# Light circle
circle = plt.Circle(
    (0, 0),
    1,
    fill=False,
    color='gray',
    linestyle='--',
    linewidth=1,
    # alpha=0.5      # makes it less visible
)
ax.add_artist(circle)

# Constellation points
ax.scatter(I, Q, s=100, color = 'darkblue')

# I-axis arrow
ax.arrow(
    -1.2, 0,
    2.4, 0,
    head_width=0.05,
    head_length=0.08,
    length_includes_head=True,
    color='black'
)

# Q-axis arrow
ax.arrow(
    0, -1.2,
    0, 2.4,
    head_width=0.05,
    head_length=0.08,
    length_includes_head=True,
    color='black'
)

ax.text(1.3, 0, 'I', fontsize=12)
ax.text(0, 1.3, 'Q', fontsize=12)

ax.set_aspect('equal')
ax.set_xlim(-1.4, 1.4)
ax.set_ylim(-1.4, 1.4)

# Hide the normal box axes
ax.axis('off')


plt.tight_layout()
plt.savefig("8PSK.jpg", dpi=300, bbox_inches="tight")