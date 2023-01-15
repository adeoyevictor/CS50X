class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        self.capacity = capacity
        self.n = 0


    def __str__(self):
        return "🍪" * self.n

    def deposit(self, n):
        if (self.n + n) > capacity:
            raise ValueError("Jar is full")
        else:
            self.n += n

    def withdraw(self, n):
        ...

    @property
    def capacity(self):
        ...

    @property
    def size(self):
        ...