import random

class Die(object):

  def __init__(self, side_count=6):
    self.side_count = side_count

  def roll(self):
    return random.randrange(0, self.side_count) + 1

# d = Die()
# print d.roll()