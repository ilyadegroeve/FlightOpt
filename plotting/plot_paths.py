# THIS CODE IS TO PLOT THE PATH WITHOUT ANY STOPS AT VUB
import matplotlib.pyplot as plt

# Real geographic coordinates (latitude, longitude)
real_coords = {
    "VUB": (50.8222329, 4.3969074),
    "Edith Cavell": (50.8139343, 4.3578839),
    "Cliniques de l'Europe": (50.8050334, 4.3686235),
    "Epsylon ASBL": (50.7861456, 4.3666663),
    "Hôpital Etterbeek-Ixelles": (50.8252055, 4.3787444),
    "Clinique Saint-Jean": (50.8543172, 4.3603786),
    "Hôpitaux iris Ziekenhuizen": (50.8334341, 4.3559617),
}

# Convert (lat, lon) to (x, y) = (longitude, latitude) for plotting.
coords = {name: (lon, lat) for name, (lat, lon) in real_coords.items()}

# Define the circular path and vaccine amounts (Δr = r₂ − r₁ for each leg)
path = [
    'VUB',
    'Hôpital Etterbeek-Ixelles',
    'Clinique Saint-Jean',
    'Hôpitaux iris Ziekenhuizen',
    'Edith Cavell',
    "Cliniques de l'Europe",
    'Epsylon ASBL',
    'VUB'
]
vaccine_amounts = [200, 170, 150, 110, 70, 20, 0]

fig, ax = plt.subplots(figsize=(8, 6))

for i in range(len(path) - 1):
    start, end = coords[path[i]], coords[path[i+1]]
    ax.annotate('', xy=end, xytext=start,
                arrowprops=dict(arrowstyle='->', lw=3, color='lightgray'))
    mid = ((start[0] + end[0]) / 2, (start[1] + end[1]) / 2)
    ax.text(mid[0], mid[1], str(vaccine_amounts[i]), fontsize=10, color='red', ha='center')

for loc, (x, y) in coords.items():
    if loc == 'VUB':
        ax.scatter(x, y, color='green', s=100)
        ax.text(x, y, loc, fontsize=15, va='bottom', ha='left', color='darkgreen')
    else:
        ax.scatter(x, y, color='darkgray', s=50)
        ax.text(x, y, loc, fontsize=10, va='bottom', ha='left')

ax.set_aspect('equal', adjustable='box')

# Add coordinate axes
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
ax.tick_params(axis='both', which='major', labelsize=10)

# Extend the axis limits to create whitespace
ax.set_xlim(4.34, 4.42)
ax.set_ylim(50.77, 50.87)

# Add grid with thinner, lighter lines.
ax.grid(True, which='both', linestyle='--', lw=0.5, color='lightgray')

# Save the figure as a PNG file with the highest quality
plt.savefig('vaccine_distribution_map.png', dpi=300, bbox_inches='tight')

plt.show()



# THIS CODE IS TO PLOT THE PATH WITH 1 STOP
import matplotlib.pyplot as plt

# Real geographic coordinates (latitude, longitude)
real_coords = {
    "VUB": (50.8222329, 4.3969074),
    "Edith Cavell": (50.8139343, 4.3578839),
    "Cliniques de l'Europe": (50.8050334, 4.3686235),
    "Epsylon ASBL": (50.7861456, 4.3666663),
    "Hôpital Etterbeek-Ixelles": (50.8252055, 4.3787444),
    "Clinique Saint-Jean": (50.8543172, 4.3603786),
    "Hôpitaux iris Ziekenhuizen": (50.8334341, 4.3559617),
}

# Convert (lat, lon) to (x, y) = (longitude, latitude) for plotting.
coords = {name: (lon, lat) for name, (lat, lon) in real_coords.items()}

# Define the paths and vaccine amounts
path1 = ['VUB', 'Hôpital Etterbeek-Ixelles', 'Hôpitaux iris Ziekenhuizen', 'Clinique Saint-Jean', 'VUB']
vaccine_amounts1 = [90, 60, 20, 0]

path2 = ['VUB', 'Edith Cavell', "Cliniques de l'Europe", 'Epsylon ASBL', 'VUB']
vaccine_amounts2 = [110, 70, 20, 0]

fig, ax = plt.subplots(figsize=(8, 6))

# Plot the first path
for i in range(len(path1) - 1):
    start, end = coords[path1[i]], coords[path1[i+1]]
    ax.annotate('', xy=end, xytext=start,
                arrowprops=dict(arrowstyle='->', lw=3, color='lightgray'))
    mid = ((start[0] + end[0]) / 2, (start[1] + end[1]) / 2)
    ax.text(mid[0], mid[1], str(vaccine_amounts1[i]), fontsize=10, color='red', ha='center')

# Plot the second path
for i in range(len(path2) - 1):
    start, end = coords[path2[i]], coords[path2[i+1]]
    ax.annotate('', xy=end, xytext=start,
                arrowprops=dict(arrowstyle='->', lw=3, color='lightblue'))
    mid = ((start[0] + end[0]) / 2, (start[1] + end[1]) / 2)
    ax.text(mid[0], mid[1], str(vaccine_amounts2[i]), fontsize=10, color='blue', ha='center')

# Plot the locations
for loc, (x, y) in coords.items():
    if loc == 'VUB':
        ax.scatter(x, y, color='green', s=100)
        ax.text(x, y, loc, fontsize=15, va='bottom', ha='left', color='darkgreen')
    else:
        ax.scatter(x, y, color='darkgray', s=50)
        ax.text(x, y, loc, fontsize=10, va='bottom', ha='left')

ax.set_aspect('equal', adjustable='box')

# Add coordinate axes
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
ax.tick_params(axis='both', which='major', labelsize=10)

# Extend the axis limits to create whitespace
ax.set_xlim(4.34, 4.42)
ax.set_ylim(50.77, 50.87)

# Add grid with thinner, lighter lines.
ax.grid(True, which='both', linestyle='--', lw=0.5, color='lightgray')

# Save the figure as a PNG file with the highest quality
plt.savefig('vaccine_distribution_map_two_paths.png', dpi=300, bbox_inches='tight')

plt.show()
