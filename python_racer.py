class PythonRacer(object):

# first make for two players.
# later retrofit so it can race an array of many players
  def __init__(self, players, die, length=30):
    self.players = players
    self.die = die
    self.length = length
    self.positions = self.create_positions(self.players)

  def create_positions(self, players):
    position_dict = {}
    for player in players:
      position_dict[player] = 0
    return position_dict

  def finished_game(self):
    print "yooooo"
    for player, position in self.positions.items():
      print position >= self.length




  # def advance_player(self, player):

  # def winner(self):

  # def board_visualization(self):