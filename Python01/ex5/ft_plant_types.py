class Plant:
    def __init__(self, name: str, height: float, age_old: int) -> None:
        self._name = name
        self._height = height
        self._age_old = age_old

    def get_height(self) -> float:
        return self._height

    def get_name(self) -> str:
        return self._name

    def get_age(self) -> int:
        return self._age_old

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected\n")
        else:
            self._height = height
            print(f"Height updated: {self._height}cm")

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self._name}: Error, Age can't be negative")
            print("Age update rejected\n")
        else:
            self._age_old = age
            print(f"Age updated: {self._age_old} days\n")

    def show(self) -> None:
        print(f"{self._name}: {self._height:.1f} cm, "
              f" {self._age_old} days old")

    def grow(self):
        match self._name:
            case "Rose":
                self._height += 0.5
            case "Jazmin":
                self._height += 1.5
            case "Tulipan":
                self._height += 1
            case _:
                self._height += 3
        self.show()

    def age(self):
        print("=== Garden Plant Growth===")
        self.show()
        initial_height = self._height
        for i in range(1, 8):
            self.__age_old += 1
            print(f"=== Day {i} ===")
            self.grow()
        print(f"Growth this week: {self._height - initial_height}")


class Flower(Plant):
    def __init__(self, name, height, age_old, color: str):
        super().__init__(name, height, age_old)
        self._color = color
        self._bloom = 0

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")
        if self._bloom == 0:
            print(f"{self._name} has not bloomed yet")
        elif self._bloom == 1:
            print(f"{self._name} is blooming beautifully!")

    def bloom(self) -> None:
        print(f"[asking the {self._name} to bloom]")
        if self._bloom == 0:
            self._bloom = 1


class Tree(Plant):
    def __init__(self, name, height, age_old, trunk_diameter: float):
        super().__init__(name, height, age_old)
        self._trunk_diameter = trunk_diameter
        self._shade = 0

    def produce_shade(self):
        print("[asking the oak to produce shade]")
        if self._shade == 0:
            self._shade = 1
            print(f"Tree {self._name} now produces a shade of ", end=""
                  f"{self._height:.1f}cm"
                  f" long and {self._trunk_diameter:.1f}cm wide.")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter:.1f}cm")


class Vegetable(Plant):
    def __init__(
        self,
        name,
        height,
        age_old,
        harvest_season: str,
        nutritional_value: int = 0,
    ):
        super().__init__(name, height, age_old)
        self._harvest_season = harvest_season
        self._nutritional_value = nutritional_value

    def show(self):
        super().show()
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutritional value: {self._nutritional_value}")

    def age(self, days_grow):
        self._age_old = self._age_old + days_grow

    def grow(self, days_grow):
        print(f"[make tomato grow and age for {days_grow} days]")
        self.age(days_grow)
        self._height += (4.3 * days_grow)
        self._nutritional_value += days_grow
        self.show()


def main() -> None:
    print("=== Garden Plant Types ===")
    print("=== Flower")
    flor = Flower("Rosa", 15, 6, "gris")
    flor.show()
    flor.bloom()
    flor.show()
    print("\n")
    print("=== Tree")
    oak = Tree("Oak", 200, 365, 5)
    oak.show()
    oak.produce_shade()
    print("\n")
    print("=== Vegetable")
    vegetal = Vegetable("Tomato", 20, 52, "April")
    vegetal.show()
    vegetal.grow(10)


if __name__ == "__main__":
    main()
