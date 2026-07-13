#!/usr/bin/python3

if __name__ == "__main__":
    class Plant:
        def __init__(self, name: str, height: float, age: int):
            self.name = name
            self.height = round(height)
            self.age = age

        def show(self):
            print(f"{self.name}: {self.height} cm, {self.age} days old")

rosa = Plant("rosa", 43, 2)
jazmin = Plant("Jazmin", 12, 1)
print("=== Garden Plant Registry ===")
rosa.show()
jazmin.show()
