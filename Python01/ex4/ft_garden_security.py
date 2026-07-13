class Plant:
    def __init__(self, name: str, height: float, age_old: int) -> None:
        self.__name = name
        self.__height = height
        self.__age_old = age_old

    def get_height(self) -> float:
        return self.__height

    def get_name(self) -> str:
        return self.__name

    def get_age(self) -> int:
        return self.__age_old

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self.__name}: Error, height can't be negative")
            print("Height update rejected\n")
        else:
            self.__height = height
            print(f"Height updated: {self.__height}cm")

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self.__name}: Error, Age can't be negative")
            print("Age update rejected\n")
        else:
            self.__age_old = age
            print(f"Age updated: {self.__age_old} days\n")

    def show(self) -> None:
        print(f"{self.__name}: {self.__height:.1f} cm, "
              f" {self.__age_old} days old\n")

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
        initial_height = self.__height
        for i in range(1, 8):
            self.__age_old += 1
            print(f"=== Day {i} ===")
            self.grow()
        print(f"Growth this week: {self.__height - initial_height}")


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
