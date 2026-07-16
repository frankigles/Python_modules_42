#!/usr/bin/python3

class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = round(height)
        self.age = age

    def show(self):
        print(f"{self.name}: {self.height} cm, {self.age} days old")


if __name__ == "__main__":
    rose = Plant("Rose", 43, 2)
    jazmin = Plant("Jazmin", 12, 1)
    rucusheda = Plant("Rucusheda", 98, 547)
    print("=== Garden Plant Registry ===")
    rose.show()
    jazmin.show()
    rucusheda.show()
