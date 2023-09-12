import random


list_age = [7, 8, 9, 10, 11, 22, 13, 14, 15, 16, 17, 18, 33]
list_id = [
    32233432,
    34234222,
    4342422,
    3423444,
    123444,
    342342322,
    34555434544,
    5656544564,
]
list_name = [
    "Liam",
    "livia",
    "Noah",
    "Emma",
    "Oliver",
    "Charlotte",
    "James",
    "Amelia",
    "Isabella",
]


class Person:
    def __init__(self):
        self.name = random.choice(list_name)
        self.id = random.choice(list_id)
        self.age = random.choice(list_age)
        # getter

    def get_name(self):
        return self.name

    def get_id(self):
        return self.id

    def get_age(self):
        return self.age
        # setter

    def set_name(self, x):
        self.name = x

    def set_id(self, x):
        self.id = x

    def set_age(self, x):
        self.age = x

    def __str__(self):
        return f"{self.name},{self.age},{self.id}"
