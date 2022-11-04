import rectangle

class Surface:
  def __init__(self, filename, x, y, h, w):
    self.rect = rectangle.Rectangle(x, y, h, w) 
    self.image = filename

  def getRect(self):
    return self.rect
    
sur = Surface("filename", 5, -7, 10, 10)
rec = sur.getRect()
print(rec)
