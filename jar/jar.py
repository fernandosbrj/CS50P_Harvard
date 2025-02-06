class Jar:

    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return '🍪' * self._size

    def deposit(self, n):
        if n < 0:
            raise ValueError("Negative deposit number")
        if self._size + n > self._capacity:
            raise ValueError("Beyond capacity")
        else:
            self._size += n

    def withdraw(self, n):
        if n < 0:
            raise ValueError("Negative withdraw number")
        if n > self._size:
            raise ValueError("Not enough biscuit at jar")
        else:
            self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("Capacity with negative number")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not 0 <= value <= self._capacity:
            raise ValueError("Size outside limits")
        self._size = value
