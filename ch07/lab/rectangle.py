class Rectangle:
  def __init__(self, x, y, h, w):
    self.x = max(0, x)
    self.y = max(0,y)
    self.height = max(h, 0)
    self.width = max(w, 0)
  def __str__(self):
    s = "(x: {}, y: {) width: {}, height: {}"
    return s.format(self.x, self.y, self.width, self.height)