#part a
class StringUtility:
  def __init__(self, string):
    self.string = string

  def __str__(self):
    return self.string
  
#part b
  def vowels(self):
    count = 0
    self.low_string = self.string.lower()
    for i in f"{self.string}":
      if(i=='a' or i=='e'or i=='i' or i=='o' or i=='u'):
        count = count + 1
    if count < 5:
      return str(count)
    else:
      count = "many"
      return str(count)
    
    
  def bothEnds(self):
    return f"{self.string[0:2]}"+f"{self.string[-2:]}"

  def fixStart(self):
    self.fix_string = list(self.string)
    c = 1
    for l in self.fix_string[1:]:
      if str(l) is str(self.fix_string[0]):
        self.fix_string[c]= "*"
        str(self.fix_string[c])
      c+=1
    return "".join(self.fix_string)

  def asciiSum(self):
    return sum([ord(letter) for letter in self.string])
    
  def cipher(self):
    cipher = ""
    for letter in range(len(self.string)):
      if self.string[letter].isupper() == True:
        cipher += chr((ord(self.string[letter].lower())+len(self.string)-97)%26+97).upper()
        
      if self.string[letter].islower()==True:
        cipher += chr((ord(self.string[letter])+len(self.string)-97)%26+97)
        
      if self.string[letter] == " ":
        cipher += " "
    return cipher
