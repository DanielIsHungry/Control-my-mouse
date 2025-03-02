from abc import ABC, abstractmethod
class Monster(ABC):
    def __init__(self, name: str, color: str, eyes: int, age: int, weight: float):
        # Type-checking for each attribute
        self.check_instance(name, str)
        self.check_instance(color, str)
        self.check_instance(eyes, int)
        self.check_instance(age, int)
        self.check_instance(weight, float)

        self.name = name
        self.color = color
        self.eyes = eyes
        self.age = age
        self.weight = weight

    def check_instance(self, value, expected_type):
        if not isinstance(value, expected_type):
            raise TypeError(f"Expected {expected_type}, but got {type(value)}")

    @abstractmethod
    def ability(self):
        pass
