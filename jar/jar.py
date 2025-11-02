class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if not isinstance(n, int):
            raise ValueError
        if self._size + n > self.capacity or n < 0:
            raise ValueError
        self._size += n
        return self._size

    def withdraw(self, n):
        if not isinstance(n, int):
            raise ValueError
        if self._size - n < 0 or n < 0:
            raise ValueError
        self._size -= n
        return self._size

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size
