from route_calculations import total_energy_wh


if __name__ == "__main__":
    path = ["VUB", "Edith Cavell", "Cliniques de l'Europe", "Epsylon ASBL", "VUB"]
    total_wh = total_energy_wh(path, initial_vaccines_amount=110)
    print(f"Energy consumption: {total_wh} Wh")
