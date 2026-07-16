#!/usr/bin/python3

class Plant:
    def __init__(self, name: str, height: float, age_old: int) -> None:
        self._name = name
        self.set_height(height)
        self.set_age(age_old)

    @property
    def height(self) -> float:
        return self._height

    @property
    def name(self) -> str:
        return self._name

    @property
    def age_old(self) -> int:
        return self._age_old

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected\n")
        else:
            self._height = height
            print(f"Height updated: {self.height}cm")

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self.name}: Error, Age can't be negative")
            print("Age update rejected\n")
        else:
            self._age_old = age
            print(f"Age updated: {self.age_old} days\n")

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f} cm, "
              f" {self.age_old} days old\n")

    def grow(self):
        match self.name:
            case "Rose":
                self.height += 0.5
            case "Jazmin":
                self.height += 1.5
            case "Tulipan":
                self.height += 1
            case _:
                self.height += 3
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


def main() -> None:
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15, 7)
    print("Plant created:", end=" ")
    rose.show()
    rose.set_height(25)
    rose.set_age(30)
    rose.set_height(-15)
    rose.set_age(-10)

    print("Current state:", end="")
    rose.show()


if __name__ == "__main__":
    main()
