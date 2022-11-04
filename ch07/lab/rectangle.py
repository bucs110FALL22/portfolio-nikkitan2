class Rectangle:
  def __init__(self, x, y, h, w):
    self.x = max(0, x)
    self.y = max(0,y)
    self.height = max(h, 0)
    self.width = max(w, 0)
  def __str__(self):
    result_str = f"coordinate: {self.x, self.y}"
    result_str += f"\nheight: {self.height}"
    result_str += f"\nwidth: {self.width}"
    return result_str
    
    


def main():
  rec_size = Rectangle(1, 5, 7, 10)
  print(rec_size)
main()