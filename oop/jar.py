class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must be a non-negative integer")
        # if not isinstance(initial_cookies, int) or initial_cookies < 0:
        #     raise ValueError("Initial cookies must be a non-negative integer")
        self._capacity = capacity
        self._size = 0  # Initialize with the specified initial cookies

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if n < 0:
            raise ValueError("Number of cookies to deposit must be non-negative")
        if self._size + n > self._capacity:
            raise ValueError("Exceeds jar capacity")
        self._size += n

    def withdraw(self, n):
        if n < 0:
            raise ValueError("Number of cookies to withdraw must be non-negative")
        if self._size < n:
            raise ValueError("Not enough cookies in the jar")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size


jar = Jar()
jar.deposit(5)
jar.withdraw(2)
print(jar)
