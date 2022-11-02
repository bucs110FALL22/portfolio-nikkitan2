import time
import uuid

class Animal:
  def __init__(self, name, type):
    self.id = time.strftime("%d%m%S")
    self.name = name
    self.type = type
    self.arrived = time.strftime("%d/%m/%Y")
    self.adopted = None
    
  def set_adopted(self):
    self.adopted = time.strftime("%d/%m/%Y")

  def __str__(self):
    result_str = f"{self.name}[{self.type}]"
    result_str += f"\narrived: {self.arrived}"
    result_str += f"\nadopted:{self.adopted}"
    return result_str




