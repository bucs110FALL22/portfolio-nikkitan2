#part a
class StringUtility:
  def __init__(self, string):
    self.string = string

  def __str__(self):
    return self.string
  
#part b
  def vowels(self):
    count = 0
    for i in self.string:
      if(i=='a' or i=='e'or i=='i' or i=='o' or i=='u'):
        count = count + 1
    if count < 5:
      return str(count)
    else:
      return f"many"
  
  def bothEnds(self):
    if len(self.string) >= 2:
      my_string = self.string[0] + self.string[1] + self.string[-2] + self.string[-1]
      return my_string
    else:
      return ''

def fixStart(self):
  if len(self.string)>=1:
    firstl= self.string[0]
    for i in self.string:
      mystring = self.string[1:].replace(firstl,"*")
      return self.string[0]+ mystring
  else:
    return('')



 