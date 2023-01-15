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
        if n > self.n:
            raise ValueError("Not enough cookies")
        else:
            self.n -= n
        ...

    @property
    def capacity(self):
        return self._capacity
    

    @property
    def size(self):
        return self._n

jar1 = Jar(10)
print(

jar1.capacity
)