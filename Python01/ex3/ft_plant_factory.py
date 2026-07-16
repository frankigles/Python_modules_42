#!/usr/bin/python3

class Plant:
    def __init__(self, name: str, height: float, age_old: int):
        self.name = name
        self.height = height
        self.age_old = age_old

    def show(self):
        print(f"{self.name}: {self.height:.1f} cm, {self.age_old} days old")

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
        initial_height = self.height
        for i in range(1, 8):
            self.age_old += 1
            print(f"=== Day {i} ===")
            self.grow()
        print(f"Growth this week: {self.height - initial_height}")


if __name__ == "__main__":
    rose = Plant("Rose", 5, 21)
    jazmin = Plant("Jazmin", 4, 12)
    cardo = Plant("Cardo", 54, 35)
    diente_leon = Plant("Diente de Leon", 13, 5)
    lavanda = Plant("Lavanda", 37, 90)
    plants = [rose, jazmin, cardo, diente_leon, lavanda]
    print("=== Plant Factory Output ===")
    for plant in plants:
        print("Created: ", end="")
        plant.show()
