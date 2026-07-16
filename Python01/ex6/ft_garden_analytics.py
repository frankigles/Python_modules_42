#!/usr/bin/python3

class Plant:
    def __init__(self, name: str, height: float, age_old: int) -> None:
        self._name = name
        self.set_height(height)
        self.set_age(age_old)
        self._times_grow = 0
        self._times_age = 0
        self._times_show = 0
        self._times_shade = 0

    @classmethod
    def random_plant(cls):
        return cls("Anonymous plant", 0, 0)

    @staticmethod
    def year_old(age_old):
        print(f"Is {age_old} days more than a year? -> ", end="")
        if age_old > 365:
            print("True")
        else:
            print("False")

    @property
    def get_height(self) -> float:
        return self._height

    @property
    def get_name(self) -> str:
        return self._name

    @property
    def get_age(self) -> int:
        return self._age_old

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self.get_name}: Error, height can't be negative")
        else:
            self._height = height

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self.get_name}: Error, Age can't be negative")
        else:
            self._age_old = age

    def show(self) -> None:
        self._times_show += 1
        print(f"{self.get_name}: {self.get_height:.1f} cm, "
              f" {self.get_age} days old")

    def grow(self):
        self._times_grow += 1
        match self._name:
            case "Rose":
                self._height += 8
            case "Jazmin":
                self._height += 1.5
            case "Tulipan":
                self._height += 1
            case _:
                self._height += 3
        self.show()

    def age(self):
        self._times_age += 1
        print("=== Garden Plant Growth===")
        self.show()
        initial_height = self.get_height
        for i in range(1, 8):
            self._age_old += 1
            print(f"=== Day {i} ===")
            self.grow()
        print(f"Growth this week: {self._height - initial_height}")

    def show_stats(self, class_type="") -> None:
        print(f"[statistics for {self.get_name}]")
        print(f"Stats: {self._times_grow} grow,"
              f"{self._times_age} age, {self._times_show} show")
        if class_type == "Tree":
            print(f"{self._times_shade} shade")


class Flower(Plant):
    def __init__(self, name: str, height: float, age_old: int, color: str):
        super().__init__(name, height, age_old)
        self._color = color
        self._bloom = 0

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")
        if self._bloom == 0:
            print(f"{self.get_name} has not bloomed yet")
        elif self._bloom == 1:
            print(f"{self.get_name} is blooming beautifully!")

    def bloom(self) -> None:
        if self._bloom == 0:
            self._bloom = 1

    def grow(self):
        super().grow()


class Seed(Flower):
    def __init__(
        self, name: str,
        height: float, age_old: int, color: str, seeds: int = 0
    ):
        super().__init__(name, height, age_old, color)
        self.seeds = 0

    def bloom(self):
        super().bloom()
        self.seeds = 42

    def show(self):
        super().show()
        print(f"Seeds: {self.seeds}")

    def explode_flower(self):
        self._times_grow += 1
        self._times_age += 1
        print(f"[make {self._name} grow, age and bloom]")
        self._height += 30
        self._age_old += 20
        self.bloom()


class Tree(Plant):
    def __init__(
            self, name: str, height: float, age_old: int,
            trunk_diameter: float):
        super().__init__(name, height, age_old)
        self._trunk_diameter = trunk_diameter
        self._shade = 0

    def produce_shade(self):
        self._times_shade += 1
        print(f"[asking the {self._name} to produce shade]")
        if self._shade == 0:
            self._shade = 1
            print(f"Tree {self._name} now produces a shade of ", end=""
                  f"{self._height:.1f}cm"
                  f" long and {self._trunk_diameter:.1f}cm wide.\n")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter:.1f}cm")


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age_old: int,
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


def show_stats_non_member(name, grow, age, show,
                          shade=0, class_type="") -> None:
    print(f"[statistics for {name}]")
    print(f"Stats: {grow} grow,"
          f"{age} age, {show} show")
    if class_type == "Tree":
        print(f"{shade} shade")


def main():

    print("=== Garden statistics ===")
    print("=== Check year-old")
    Plant.year_old(30)
    Plant.year_old(400)
    print("\n")

    print("=== Flower")
    rose = Flower("Rose", 15, 10, "red")
    rose.show()
    rose.show_stats()
    print(f"[asking the {rose._name} to grow and bloom]")
    rose.bloom()
    rose.grow()
    rose.show_stats()
    print("\n")

    print("=== Tree")
    oak = Tree("Oak", 200, 365, 5)
    oak.show()
    oak.show_stats("Tree")
    oak.produce_shade()
    oak.show_stats("Tree")
    print("\n")

    print("=== Seeds")
    seed = Seed("Sunflower", 80, 45, "yellow")
    seed.show()
    seed.explode_flower()
    seed.show()
    seed.show_stats()
    print("\n")
    print("=== Anonymous")
    random = Plant.random_plant()
    random.show()
    show_stats_non_member(random.get_name, random._times_grow,
                          random._times_age, random._times_show)


if __name__ == "__main__":
    main()
