import numpy as np
import matplotlib.pyplot as plt
from dataclasses import dataclass

# zadanie 1

class Counter:
    def __init__(self, value=0):
        self.value = value

    def plus1(self):
        self.value += 1

    def minus1(self):
        self.value -= 1

    def set0(self):
        self.value = 0

    def read(self):
        return self.value

print("Zadanie 1")
kalkulator = Counter(7)
kalkulator.minus1()
print(kalkulator.read())
kalkulator.plus1()
print(kalkulator.read())
kalkulator.set0()
print(kalkulator.read())

# zadanie 2

@dataclass
class Measurement:
    time: float
    value: float
    unit: str
    

pomiar1 = Measurement(12.5, 100, "cm")
pomiar2 = Measurement(15.0, 200, "cm")
pomiar3 = Measurement(20.0, 300, "cm")

pomiary = [pomiar1, pomiar2, pomiar3]
print ("Zadanie 2")
print(pomiary)
print("max pomiar:", max(pomiary, key=lambda x: x.value))

#zadanie 3

class Vector2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2d(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2d(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector2d(self.x * scalar, self.y * scalar)
    
    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    def __truediv__(self, scalar):
        return Vector2d(self.x / scalar, self.y / scalar)

    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def scalar_product(self, other):
        return self.x * other.x + self.y * other.y
    
    def length(self):
        return np.sqrt(self.x**2 + self.y**2)
    
v1 = Vector2d(1, 2)
v2 = Vector2d(3, 4)
print("Zadanie 3")
print("v1:", v1)    
print("v2:", v2)
print("v1 + v2:", v1 + v2)
print("v1 - v2:", v1 - v2)
print("v1 * 2:", v1 * 2)
print("v1 / 2:", v1 / 2)
print("v1 · v2:", v1.scalar_product(v2))
print("length of v1:", v1.length())
print("length of v2:", v2.length())

#zadanie 4

class MeasurementSeries:
    def __init__(self, data):
        self.data = list(data)

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        self.data[index] = value

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        return iter(self.data)

    def mean(self):
        return sum(self.data) / len(self.data)

    def min_max(self):
        return min(self.data), max(self.data)


series = MeasurementSeries([1, 2, 3, 4])
print("Zadanie 4")
print(series[2])
series[2] = 10
for x in series:
    print(x)
print(len(series))
print(series.mean())
print(series.min_max())

#zadanie 5

class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients 

    def __repr__(self):
        terms = []
        for i, a in enumerate(self.coefficients):
            if a != 0:
                terms.append(f"{a}x^{i}" if i > 0 else str(a))
        return " + ".join(terms)

    def __call__(self, x):
        result = 0
        for i, a in enumerate(self.coefficients):
            result += a * (x ** i)
        return result
    def degree(self):
        return len(self.coefficients) - 1

print("Zadanie 5")
p = Polynomial([1, 0, 3])  # 1 + 3x^2

print(p)
print(p(2))
print("stopien:", p.degree())

#zadanie 6

class Account:
    def __init__(self, username, points=0):
        self.username = username
        self.points = points

    def plus(self, amount):
        self.points += amount

    def minus(self, amount):
        self.points -= amount

    def info(self):
        print(f"{self.username}: {self.points} pkt")


class PremiumAccount(Account):
    def __init__(self, username, points=0, bonus=0.1):
        super().__init__(username, points)
        self.bonus = bonus

    def plus(self, amount):
        bonus_points = amount * self.bonus
        super().plus(amount + bonus_points)


print("zadanie 6")
acc = PremiumAccount("Jan", 100, 0.2)
acc.info()
acc.plus(50)
acc.info()

#zadanie 7
class Animal:
    def __init__(self, name, x=0, y=0):
        self.name = name
        self.x = x
        self.y = y

    def move(self):
        raise NotImplementedError

    def sound(self):
        raise NotImplementedError

    def info(self):
        print(f"{self.name} at ({self.x}, {self.y})")


class Dog(Animal):
    def move(self):
        self.x += 1

    def sound(self):
        print("miaaaaaaaał!")


class Bird(Animal):
    def move(self):
        self.y += 2

    def sound(self):
        print("jajo, jajo!")



animals = [Dog("Kotek"), Bird("Jajon")]

print("Zadanie 7")
for a in animals:
    a.move()
    a.sound()
    a.info()