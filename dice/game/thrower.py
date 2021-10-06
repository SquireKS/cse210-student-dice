import random

class Thrower:
    

    def __init__(self):
        self.dice_rolls = []
        self.num_throws = 0
        

    
    def throw_dice(self):
        '''Rolls the dice by outputting 5 random numbers.'''
        self.dice_rolls.clear()
        for i in range(5):
            dice = random.randint(1, 6)
            self.dice_rolls.append(dice)
        


    def get_points(self):
        return self.dice_rolls.count(5) * 50 + self.dice_rolls.count(1) * 100

    def can_throw(self):
        return (self.dice_rolls.count(5) > 0 or self.dice_rolls.count(1) > 0
            or self. num_throws == 0)