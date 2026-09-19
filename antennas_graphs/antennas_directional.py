import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import Normalize

# ==========================================
# ANTENNA PARAMETERS
# ==========================================
# We will use a linear array to generate the pattern
N = 5           # Number of elements
d = 0.5         # Spacing in wavelengths (0.5 for lambda/2)

# ==========================================
# PATTERN COMPUTATION
# ==========================================
# 1. Define the angle grid (0 to 180 degrees)
theta_deg = np.linspace(0, 360, 1000)
theta_rad = np.radians(theta_deg)

# ==========================================
# PATTERN COMPUTATION
# ==========================================
psi = 2 * np.pi * d * np.cos(theta_rad)
AF = np.abs(np.sin(N * psi / 2) / (N * np.sin(psi / 2) + 1e-12))

# np.maximum clips negative cosine values to 0, completely suppressing the rear hemisphere
element_factor = np.maximum(np.cos(theta_rad), 0)**2
R_abs = AF * element_factor
R_abs /= np.max(R_abs)

gain_db = 20 * np.log10(R_abs + 1e-6)
gain_db = np.clip(gain_db, -30, 0)

# ==========================================
# RE-CALCULATE BEAMWIDTH INDEX
# ==========================================
idx_hpbw = np.where(gain_db <= -3)[0][0]
hpbw_half = theta_deg[idx_hpbw]
hpbw_total = 2 * hpbw_half

try:
    diffs = np.diff(gain_db)
    first_null_idx = np.where(diffs > 0)[0][0] + 1
    fnbw_half = theta_deg[first_null_idx]
    fnbw_total = 2 * fnbw_half
except IndexError:
    fnbw_total = 0

# ==========================================
# 2D FULL CIRCLE POLAR PLOT
# ==========================================
fig2 = plt.figure(figsize=(8, 8))
ax1 = fig2.add_subplot(111, projection='polar')

# Shift the radial axis so -30dB is at the center, 0dB is at the outer edge
r_plot = gain_db - np.min(gain_db)  
ax1.plot(theta_rad, r_plot, color='black', linewidth=1.5)
ax1.fill_between(theta_rad, 0, r_plot, color='blue', alpha=0.1)

# Format radial axis labels
ax1.set_rticks([np.min(r_plot), np.min(r_plot)+10, np.min(r_plot)+20, np.max(r_plot)])
ax1.set_yticklabels(['-30 dB', '-20 dB', '-10 dB', '0 dB'])
ax1.set_rlabel_position(225)

# Orient theta axis to match standard antenna coordinates
ax1.set_theta_zero_location("N")
ax1.set_theta_direction(-1) # Clockwise

# --- REMOVED THE CROP TO SHOW THE WHOLE CIRCLE ---
ax1.set_thetamin(0)
ax1.set_thetamax(360) 

# Save the full image
plt.savefig(
    "test.jpg",
    dpi=300,
    bbox_inches="tight"
)

# ==========================================
# 2. 3D SURFACE PLOT
# ==========================================
fig = plt.figure(figsize=(9, 8))
ax2 = fig.add_subplot(111, projection='3d')

# Create full 3D grid
phi_deg = np.linspace(-180, 180, 360)
phi_rad = np.radians(phi_deg)
THETA_3D, PHI_3D = np.meshgrid(theta_rad, phi_rad)

# Use the same R, but tiled for the entire phi circle
R_3D = np.tile(R_abs, (360, 1))
gain_db_3D = 20 * np.log10(R_3D + 1e-6)
gain_db_3D = np.clip(gain_db_3D, -30, 0)

# Spherical -> Cartesian
X = R_3D * np.sin(THETA_3D) * np.cos(PHI_3D)
Y = R_3D * np.sin(THETA_3D) * np.sin(PHI_3D)
Z = R_3D * np.cos(THETA_3D)

# Create color mapping based on dB gain
norm = Normalize(vmin=-30, vmax=0)
colors = cm.jet(norm(gain_db_3D))

# Plot the 3D surface
surf = ax2.plot_surface(X, Y, Z, facecolors=colors, linewidth=0, antialiased=True, shade=True,
                      rcount=100, ccount=100)

# Customize Axes
ax2.set_xlabel("X")
ax2.set_ylabel("Y")
ax2.set_zlabel("Z")

# Tight boundaries for a good view
ax2.set_xlim(-1, 1)
ax2.set_ylim(-1, 1)
ax2.set_zlim(0, 1)

# Add Colorbar for 3D plot
mappable = cm.ScalarMappable(norm=norm, cmap=cm.jet)
mappable.set_array([])
# fig.colorbar(mappable, ax=ax2, shrink=0.7, pad=0.1, label="Gain (dB)")
fig.colorbar(
    mappable,
    ax=ax2,
    shrink=0.6,
    # pad=0.1,
    label="Gain (dB)"
)
# Optimal viewing angle
ax2.view_init(elev=20, azim=45)

plt.tight_layout()

plt.savefig(
    "test2.jpg",
    dpi=300,
    bbox_inches="tight"
)