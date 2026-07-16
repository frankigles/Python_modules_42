#!/usr/bin/python3

class Plant:
    def __init__(self, name: str, height: float, age_old: int) -> None:
        self._name = name
        self.set_height(height)
        self.set_age(age_old)
        self.stats = self.Stats(self)

    class Stats:
        def __init__(self, plant_instance) -> None:
            self.plant = plant_instance
            self._times_grow = 0
            self._times_age = 0
            self._times_show = 0
            self._times_shade = 0

        def add_grow(self):
            self._times_grow += 1

        def add_age(self):
            self._times_age += 1

        def add_show(self):
            self._times_show += 1

        def add_shade(self):
            self._times_shade += 1

        def show_stats(self, class_type="") -> None:
            print(f"[statistics for {self.plant.get_name}]")
            print(f"Stats: {self._times_grow} grow,"
                  f"{self._times_age} age, {self._times_show} show")
            if class_type == "Tree":
                print(f"{self._times_shade} shade")

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
        self.stats.add_show()
        print(f"{self.get_name}: {self.get_height:.1f} cm, "
              f" {self.get_age} days old")

    def grow(self):
        self.stats.add_grow()
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
        self.stats.add_age()
        print("=== Garden Plant Growth===")
        self.show()
        initial_height = self.get_height
        for i in range(1, 8):
            self._age_old += 1
            print(f"=== Day {i} ===")
            self.grow()
        print(f"Growth this week: {self._height - initial_height}")


class Flower(Plant):
    def __init__(self, name: str, height: float, age_old: int, color: str):
        super().__init__(name, height, age_old)
        self._color = color
        self._bloom = 0
        self.Stats

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
        self.stats.add_grow()
        self.stats.add_age()
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
        self.Stats

    def produce_shade(self):
        self.Stats.add_shade
        print(f"[asking the {self._name} to produce shade]")
        if self._shade == 0:
            self._shade = 1
            print(f"Tree {self._name} now produces a shade of ", end=""
                  f"{self._height:.1f}cm"
                  f" long and {self._trunk_diameter:.1f}cm wide.\n")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter:.1f}cm")


def show_stats_non_member(name, class_type="") -> None:
    name.stats.show_stats()


def main():

    print("=== Garden statistics ===")
    print("=== Check year-old")
    Plant.year_old(30)
    Plant.year_old(400)
    print("\n")

    print("=== Flower")
    rose = Flower("Rose", 15, 10, "red")
    rose.show()
    rose.stats.show_stats()
    print(f"[asking the {rose._name} to grow and bloom]")
    rose.bloom()
    rose.grow()
    rose.stats.show_stats()
    print("\n")

    print("=== Tree")
    oak = Tree("Oak", 200, 365, 5)
    oak.show()
    oak.stats.show_stats("Tree")
    oak.produce_shade()
    oak.stats.show_stats("Tree")
    print("\n")

    print("=== Seeds")
    seed = Seed("Sunflower", 80, 45, "yellow")
    seed.show()
    seed.explode_flower()
    seed.show()
    seed.stats.show_stats()
    print("\n")
    print("=== Anonymous")
    random = Plant.random_plant()
    random.show()
    random.stats.show_stats()
    print("\n")
    show_stats_non_member(rose)


if __name__ == "__main__":
    main()
