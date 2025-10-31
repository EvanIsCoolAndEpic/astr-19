class Planet:
    def __init__(self, avg_temp, num_moons, has_rings, dominant_gas, is_habitable):
        self.avg_temp = avg_temp
        self.num_moons = num_moons
        self.has_rings = has_rings
        self.dominant_gas = dominant_gas
        self.is_habitable = is_habitable

    def describe(self):
        print(f"Average temperature: {self.avg_temp}\nAverage number of moons: {self.num_moons}\nHas rings?: {self.has_rings}\n Dominant gas: {self.dominant_gas}\n Is it habitable?: {self.is_habitable}")


if __name__ == "__main__":
    example = Planet(100, 2, True, "Nitrous", True)
    example.describe()