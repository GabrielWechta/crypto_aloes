from sympy import isprime
from random import randint

class Group:
    def __init__(self, order) -> None:
        # check if orderd is prime
        if order < 2:
            raise ValueError("Order must be greater than 1")
        if isprime(order):
            print(f"Group with prime {order=} created.")
        else:
            raise print(f"Group with NOT prime {order=} created.")
        self.order = order

    def get_generator(self):
        return GroupElement(self, 2)

    def get_random_exponent(self):
        r = randint(1, self.order - 1)
        return r


class GroupElement:
    def __init__(self, group, value) -> None:
        self.group = group
        self.value = value % group.order

    def __mul__(self, other):
        return GroupElement(self.group, self.value * other.value % self.group.order)

    def __pow__(self, power):
        return GroupElement(self.group, pow(self.value, power, self.group.order))

    def __eq__(self, other):
        return self.value == other.value

    def __repr__(self):
        return f"GroupElement({self.value})"

    def __str__(self):
        return f"{self.value}"

    def __int__(self):
        return self.value

    def __hash__(self):
        return hash(self.value)

    def inverse(self):
        return GroupElement(self.group, pow(self.value, -1, self.group.order))

    def generate_values(self):
        generated_elements = []
        generated_elements.append(self.value)
        value = self.value
        for _ in range(self.group.order - 2):
            value = GroupElement(self.group, value * self.value).value
            generated_elements.append(value)
        return generated_elements