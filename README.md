# Drone Delivery Optimization for Vaccine Distribution

## Overview

This repository contains code for optimizing drone delivery routes for vaccine distribution to hospitals in the Brussels area. It addresses the challenge of minimizing energy consumption (Wh) during deliveries, considering factors like distance, vaccine payload, and drone battery consumption model. The project explores both direct routes and sub-route strategies to enhance delivery efficiency.

## Project Structure

The repository is organized as follows:

-   **`route_data.py`**: Defines hospital locations, vaccine needs, coordinates, and the drone current model.
-   **`route_calculations.py`**: Provides shared distance and energy calculations for route scripts.
-   **`bruteforce_subroutes.py`**: Implements a brute-force approach to find the optimal sub-routes for vaccine delivery to minimize energy consumption.
-   **`route_example.py`**: Runs a small example route using the shared calculation functions.
-   **`plotting/`**: Contains scripts for visualizing delivery routes on a map.
    -   **`plot_paths.py`**: Generates plots of vaccine distribution routes, highlighting hospital locations, delivery paths, and vaccine amounts.
-   **`routes/`**: Stores optimal route information.
    -   **`route1.txt`**: Contains information about the shortest route without subroutes, and the best subroutes.
-   **`hospital_coordinates/`**: Contains different sets of coordinates for the hospitals.
    -   **`field_coordinates.py`**: Defines a set of hospital coordinates for testing autonomous flights, downscaled to a field.

## Usage

1.  **Install Dependencies:**

    ```bash
    pip install matplotlib
    ```

2.  **Run Route Optimization:**

    ```bash
    python bruteforce_subroutes.py
    ```

    This script will output the best sub-routes found and their corresponding total energy consumption.  Note that due to the nature of the brute-force approach, this script may take a significant amount of time to run, especially as the number of hospitals increases.

3.  **Visualize Routes:**

    Modify the `plotting/plot_paths.py` script to reflect the desired routes.  Then, run the script:

    ```bash
    cd plotting
    python plot_paths.py
    ```

    This will generate a `vaccine_distribution_map.png` or `vaccine_distribution_map_two_paths.png` file showing the delivery routes.

