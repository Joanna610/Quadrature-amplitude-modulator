import numpy as np
import matplotlib.pyplot as plt
from pykat import finesse                  # Importing the pykat.finesse package
from pykat.commands import *               # Importing all packages in pykat.commands.
from IPython.display import display, HTML  # Allows us to display HTML.

pykat.init_pykat_plotting(dpi=90)  

M = 4

N = int(np.sqrt(M))

levels = np.arange(-(N-1), N, 2)

I, Q = np.meshgrid(levels, levels)

I = I.flatten()
Q = Q.flatten()

fig, ax = plt.subplots(figsize=(6,6))

# Constellation points
for i in range(len(I)):
    ax.text(
        I[i],
        Q[i] + 0.25,      # move text slightly above point
        format(i, '02b'), # 4-bit binary label
        ha='center',
        fontsize=10
    )
ax.scatter(I, Q, s=100, color = 'darkblue')

limit = np.max(np.abs(levels)) + 1

ax.arrow(
    -limit, 0,
    2*limit, 0,
    head_width=0.15,
    head_length=0.25,
    length_includes_head=True,
    color='black'
)

ax.arrow(
    0, -limit,
    0, 2*limit,
    head_width=0.15,
    head_length=0.25,
    length_includes_head=True,
    color='black'
)

ax.text(limit+0.2, 0, 'I', fontsize=12)
ax.text(0, limit+0.2, 'Q', fontsize=12)

ax.set_aspect('equal')
ax.set_xlim(-limit, limit)
ax.set_ylim(-limit, limit)

# Hide the normal box axes
ax.axis('off')


plt.tight_layout()
plt.savefig("4_QAM.jpg", dpi=300, bbox_inches="tight")