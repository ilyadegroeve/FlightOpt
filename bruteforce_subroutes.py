import itertools

from route_calculations import total_energy_wh_with_subroutes
from route_data import vaccines_hospitals


hospitals = [hospital for hospital in vaccines_hospitals if hospital != "VUB"]


def get_all_partitions(items, max_parts=None):
    """Generate all possible partitions of the given items."""
    if not items:
        yield []
        return

    first = items[0]
    for smaller in get_all_partitions(items[1:], max_parts):
        if max_parts is None or len(smaller) < max_parts:
            yield [[first]] + smaller
        for index in range(len(smaller)):
            yield smaller[:index] + [smaller[index] + [first]] + smaller[index + 1:]


def create_subroutes(partition):
    """Create subroutes by adding VUB at the beginning and end of each part."""
    return [["VUB"] + part + ["VUB"] for part in partition if part]


def optimize_route():
    best_consumption = float("inf")
    best_subroutes = None

    for permutation in itertools.permutations(hospitals):
        for max_parts in range(1, len(hospitals) + 1):
            for partition in get_all_partitions(list(permutation), max_parts):
                subroutes = create_subroutes(partition)
                consumption = total_energy_wh_with_subroutes(subroutes)

                if consumption < best_consumption:
                    best_consumption = consumption
                    best_subroutes = subroutes
                    print(f"New best: {best_consumption} Wh with {len(best_subroutes)} subroutes")
                    print(f"Partition: {partition}")
                    print(f"Subroutes: {best_subroutes}")

    return best_subroutes, best_consumption


if __name__ == "__main__":
    best_routes, best_wh = optimize_route()
    print("\nFinal result:")
    print(f"Best consumption: {best_wh} Wh")
    print(f"Best subroutes: {best_routes}")
