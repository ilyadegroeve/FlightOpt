import math

from route_data import vaccines_current, vaccines_hospitals, world_coordinates


def calculate_distance(coord1, coord2):
    """Calculate the Haversine distance between two GPS coordinates."""
    lat1, lon1 = math.radians(coord1[0]), math.radians(coord1[1])
    lat2, lon2 = math.radians(coord2[0]), math.radians(coord2[1])

    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.asin(math.sqrt(a))
    return c * 6371


def total_energy_wh(path, initial_vaccines_amount=200, flight_velocity=7, current_by_vaccine_count=vaccines_current):
    if not path or len(path) < 2:
        raise ValueError("path must contain at least two locations")

    if not isinstance(initial_vaccines_amount, int):
        raise ValueError(
            f"initial_vaccines_amount must be an integer, got {type(initial_vaccines_amount).__name__}"
        )
    if initial_vaccines_amount < 0:
        raise ValueError(f"initial_vaccines_amount cannot be negative: {initial_vaccines_amount}")

    amount_of_vaccines = initial_vaccines_amount
    total_ah = 0.0

    for i in range(len(path) - 1):
        start_location = path[i]
        end_location = path[i + 1]

        if start_location not in world_coordinates or end_location not in world_coordinates:
            raise ValueError(f"Unknown location in path: {start_location!r} -> {end_location!r}")

        if i > 0:
            stop_location = path[i]
            if stop_location not in vaccines_hospitals:
                raise ValueError(f"Location {stop_location!r} is not a hospital in vaccines_hospitals")
            amount_of_vaccines -= vaccines_hospitals[stop_location]

        if amount_of_vaccines < 0:
            raise ValueError(
                f"Payload becomes negative on route step {i}: {amount_of_vaccines} vaccines after visiting {path[i]!r}"
            )

        if amount_of_vaccines not in current_by_vaccine_count:
            raise ValueError(
                f"No current value defined for {amount_of_vaccines} vaccines. "
                "Add a mapping entry for this payload level."
            )

        distance = calculate_distance(world_coordinates[start_location], world_coordinates[end_location])
        flight_time = distance / flight_velocity
        current = current_by_vaccine_count[amount_of_vaccines]
        total_ah += current * flight_time

    return round(total_ah * 14.8)


def initial_vaccines_route(route):
    return sum(vaccines_hospitals[location] for location in route if location in vaccines_hospitals)


def total_energy_wh_with_subroutes(list_of_subroutes):
    total_wh = sum(
        total_energy_wh(subroute, initial_vaccines_route(subroute))
        for subroute in list_of_subroutes
    )
    print(f"{len(list_of_subroutes)} subroutes total consumption: {total_wh} Wh")
    return total_wh
