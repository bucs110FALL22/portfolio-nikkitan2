class Player:
  def __init__(self):
    self.player_num = 1
    self.lives = 3
    self.dodge = 0


class Position:
  def __init__(self):
    self.move = 10
    self.direction = 90
    self.speed = 20

class Background:
  def __init__(self):
    self.clouds = True
    self.color = "light blue"
    self.random_blocks = True