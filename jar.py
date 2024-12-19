class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0 or capacity > 12:
            raise ValueError("Capacity must be a non-negative integer.")
        
        self._capacity = capacity
        self._size = 0
    
    def __str__(self):
        return "🍪" * self._size

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, value):
        if value > self._capacity:
            raise ValueError("Size cannot be bigger than the Jar's capacity (12).")
        self._size = value
    
    def deposit(self, n):
        if self._size + n > self._capacity:
            raise ValueError(f"Cannot add {n} cookies. Jar capacity is {self._capacity}.")
        self._size += n
    
    def withdraw(self, n):
        if self._size - n < 0:
            raise ValueError(f"Cannot remove {n} cookies. Only {self._size} in the jar.")
        self._size -= n