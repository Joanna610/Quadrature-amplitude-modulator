import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import Normalize

# ==========================================
# GRID PARAMETERS (Full Sphere)
# ==========================================
theta_deg = np.linspace(0, 360, 1000)
theta_rad = np.radians(theta_deg)

# ==========================================
# OMNIDIRECTIONAL PATTERN COMPUTATION
# ==========================================
# A classic omnidirectional antenna (like a half-wave dipole) 
# radiates standard donut pattern: uniform in Phi, sin(theta) dependent in Theta.
R_abs = np.abs(np.sin(theta_rad))  # Z-axis nulls, uniform X-Y ring
R_abs /= np.max(R_abs)

gain_db = 20 * np.log10(R_abs + 1e-6)
gain_db = np.clip(gain_db, -30, 0)

# ==========================================
# 1. 2D FULL CIRCLE POLAR PLOT (Figure-8)
# ==========================================
fig2 = plt.figure(figsize=(8, 8))
ax1 = fig2.add_subplot(111, projection='polar')

r_plot = gain_db - np.min(gain_db)  
ax1.plot(theta_rad, r_plot, color='black', linewidth=1.5)
ax1.fill_between(theta_rad, 0, r_plot, color='blue', alpha=0.1)

ax1.set_rticks([np.min(r_plot), np.min(r_plot)+10, np.min(r_plot)+20, np.max(r_plot)])
ax1.set_yticklabels(['-30 dB', '-20 dB', '-10 dB', '0 dB'])
ax1.set_rlabel_position(225)

ax1.set_theta_zero_location("N")
ax1.set_theta_direction(-1) 
ax1.set_thetamin(0)
ax1.set_thetamax(360) 

plt.savefig("omni_2d.jpg", dpi=300, bbox_inches="tight")

# ==========================================
# 2. 3D SURFACE PLOT (Torus / Donut Shape)
# ==========================================
fig = plt.figure(figsize=(9, 8))
ax2 = fig.add_subplot(111, projection='3d')

phi_deg = np.linspace(-180, 180, 360)
phi_rad = np.radians(phi_deg)
THETA_3D, PHI_3D = np.meshgrid(theta_rad, phi_rad)

# Tile the pattern smoothly over 360 degrees of azimuth
R_3D = np.tile(R_abs, (360, 1))
gain_db_3D = 20 * np.log10(R_3D + 1e-6)
gain_db_3D = np.clip(gain_db_3D, -30, 0)

# Convert Spherical to Cartesian Coordinates
X = R_3D * np.sin(THETA_3D) * np.cos(PHI_3D)
Y = R_3D * np.sin(THETA_3D) * np.sin(PHI_3D)
Z = R_3D * np.cos(THETA_3D)

norm = Normalize(vmin=-30, vmax=0)
colors = cm.jet(norm(gain_db_3D))

surf = ax2.plot_surface(X, Y, Z, facecolors=colors, linewidth=0, antialiased=True, shade=True,
                       rcount=100, ccount=100)

ax2.set_xlabel("X")
ax2.set_ylabel("Y")
ax2.set_zlabel("Z")

# Dynamic bounds to center the torus perfectly at origin
ax2.set_xlim(-1, 1)
ax2.set_ylim(-1, 1)
ax2.set_zlim(-1, 1)  # Extends downward to include bottom donut half

# Colorbar configuration
mappable = cm.ScalarMappable(norm=norm, cmap=cm.jet)
mappable.set_array([])
fig.colorbar(mappable, ax=ax2, shrink=0.6, label="Gain (dB)")

ax2.view_init(elev=25, azim=45)
plt.tight_layout()

plt.savefig("omni_3d.jpg", dpi=300, bbox_inches="tight")
