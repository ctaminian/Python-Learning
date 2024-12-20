class VideoGameCharacter:
    DEFAULT_MAX_HEALTH = 100

    def __init__(self, name, level=1, health=100):
        self.name = name
        self.level = level
        self.health = min(health, self.__class__.DEFAULT_MAX_HEALTH)

    @property
    def name(self):
        return self._name
        
    @name.setter
    def name(self, value):
        if isinstance(value, str) and value.strip():
            self._name = value
        else:
            raise ValueError("Your character must have a valid name!")

    @property
    def level(self):
        return self._level
    
    @level.setter
    def level(self, value):
        if isinstance(value, int) and value > 0:
            self._level = value
        else:
            raise ValueError("You must enter a postive number for level!")
        
    @property
    def health(self):
        return self._health
    
    @health.setter
    def health(self, value):
        if isinstance(value, int) and value <= self.__class__.DEFAULT_MAX_HEALTH and value > 0:
            self._health = value
        else:
            raise ValueError("You must enter a positive number for health between 0 - 100!")

    def level_up(self):
        self.health = min(self.health + 10, self.__class__.DEFAULT_MAX_HEALTH)
        self.level += 1
    
    def take_damage(self, amount):
        if isinstance(amount, int) and amount >= 0:
            self.health = max(0, self.health - amount)
        else:
            raise ValueError("Damage amount must be a non negative integer!")
    
    def is_alive(self):
        return self.health > 0

    def __str__(self):
        return f"A video game character called {self.name} at level {self.level} with {self.health} / {self.__class__.DEFAULT_MAX_HEALTH} HP."