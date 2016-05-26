class PythonRacer(object):

  def __init__(self, players, die, length=30):
    self.players = players
    self.die = die
    self.length = length

  def does_work(self):
    print "yes it does"