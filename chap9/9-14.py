#Dice

from random import randint

class Die():
    """defines a die with arbitrary number of sides"""
    
    def __init__(self, sides=6):
        """initializes dice"""
        self.sides = sides

    def roll_die(self):
        """roll die"""
        return randint(1,self.sides)

d6 = Die()
rolls = []
for i in range(10):
    rolls.append(d6.roll_die())
print(rolls)

rolls = []
d10 = Die(10)
for i in range(10):
    rolls.append(d10.roll_die())
print(rolls)

rolls = []
d20 = Die(20)
for i in range(10):
    rolls.append(d10.roll_die())
print(rolls)