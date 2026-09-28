import numpy as np
import folium
from folium.plugins import MarkerCluster

def transform_coordinates(coords, scale_factor, rotation_angle_degrees, reference_point, new_origin):
    """
    Transform coordinates by scaling relative to a reference point, rotating, and translating.
    """
    # Convert to numpy array for easier operations
    coords_array = np.array(coords)
    reference_array = np.array(reference_point)

    # Step 1: Translate all points so the reference point is at the origin
    centered_coords = coords_array - reference_array

    # Step 2: Apply scaling
    scaled_coords = centered_coords / scale_factor

    # Step 3: Apply rotation (clockwise rotation is negative angle)
    angle_rad = np.radians(-rotation_angle_degrees)
    rotation_matrix = np.array([
        [np.cos(angle_rad), -np.sin(angle_rad)],
        [np.sin(angle_rad), np.cos(angle_rad)]
    ])
    rotated_coords = np.dot(scaled_coords, rotation_matrix.T)

    # Step 4: Translate to the new origin
    new_origin_array = np.array(new_origin)
    transformed_coords = rotated_coords + new_origin_array

    # Convert back to list of tuples
    result = [tuple(coord) for coord in transformed_coords]

    return result

def create_hospital_map(locations, original_coords, transformed_coords, output_file="hospital_map.html"):
    """
    Create a Folium map showing both original and transformed hospital locations.

    Parameters:
    -----------
    locations : list of str
        List of hospital names
    original_coords : list of tuples
        List of original (lat, lon) coordinates
    transformed_coords : list of tuples
        List of transformed (lat, lon) coordinates
    output_file : str
        Filename for the output HTML file
    """
    # Calculate the center point for the map (average of all coordinates)
    all_coords = original_coords + transformed_coords
    center_lat = sum(coord[0] for coord in all_coords) / len(all_coords)
    center_lon = sum(coord[1] for coord in all_coords) / len(all_coords)

    # Create a map centered at the average position
    m = folium.Map(location=[center_lat, center_lon], zoom_start=11)

    # Create marker clusters for original and transformed coordinates
    original_cluster = MarkerCluster(name="Original Locations", overlay=True)
    transformed_cluster = MarkerCluster(name="Transformed Locations", overlay=True)

    # Add transformed coordinates with red markers
    for i, (name, coord) in enumerate(zip(locations, transformed_coords)):
        folium.Marker(
            location=coord,
            popup=f"{name} (Transformed)",
            tooltip=name,
            icon=folium.Icon(color="red", icon="hospital", prefix="fa")
        ).add_to(transformed_cluster)

    # Add both layers to the map
    original_cluster.add_to(m)
    transformed_cluster.add_to(m)

    # Add layer control
    folium.LayerControl().add_to(m)

    # Save the map as an HTML file
    m.save(output_file)
    print(f"Map saved to {output_file}")

    return m

def create_field_locations_dict(locations, transformed_coords):
    """
    Create a dictionary of field locations with their transformed coordinates.

    Parameters:
    -----------
    locations : list of str
        List of hospital names
    transformed_coords : list of tuples
        List of transformed (lat, lon) coordinates

    Returns:
    --------
    dict
        Dictionary with hospital names as keys and transformed coordinates as values
    """
    field_locations = {location: (float(lat), float(lon)) for location, (lat, lon) in zip(locations, transformed_coords)}
    return field_locations

def main():
    # Locations and coordinates
    locations = [
        "VUB", "Edith Cavell", "Cliniques de l'Europe",
        "Epsylon ASBL", "Hôpital Etterbeek-Ixelles",
        "Clinique Saint-Jean", "Hôpitaux iris Ziekenhuizen"
    ]
    coordinates = [
        (50.8222329, 4.3969074),  # VUB
        (50.8139343, 4.3578839),  # Edith Cavell
        (50.8050334, 4.3686235),  # Cliniques de l'Europe
        (50.7861456, 4.3666663),  # Epsylon ASBL
        (50.8252055, 4.3787444),  # Hôpital Etterbeek-Ixelles
        (50.8543172, 4.3603786),  # Clinique Saint-Jean
        (50.8334341, 4.3559617)   # Hôpitaux iris Ziekenhuizen
    ]

    # Transformation parameters
    scale_factor = 90
    rotation_angle = -9
    reference_point = coordinates[3]  # Edith Cavell as reference point
    new_origin = (50.940361, 4.210500)  # New location for Edith Cavell

    # Apply transformation
    transformed_coords = transform_coordinates(coordinates, scale_factor, rotation_angle,
                                             reference_point, new_origin)

    # Create and save the map
    create_hospital_map(locations, coordinates, transformed_coords, "brussels_hospitals_map.html")

    # Create and print the field locations dictionary
    field_locations = create_field_locations_dict(locations, transformed_coords)
    print("\nField locations dictionary:")
    print(field_locations)

    # Print transformed coordinates for reference
    print("\nTransformed coordinates:")
    for i, location in enumerate(locations):
        trans = transformed_coords[i]
        print(f"{location}: ({trans[0]:.7f}, {trans[1]:.7f})")

if __name__ == "__main__":
    main()
