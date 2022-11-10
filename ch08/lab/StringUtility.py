#part a
def __init__(self, s):
  self.s = s

def __str__(self):
  return self.s

#part b
def vowels(self):
  vowelCount = 0
  n = self.s
  n.lower()

  for i in n:
    if(i == 'a', i == 'e', i == 'i', i == 'o', i == 'u'):
      vowelCount +=1
  if(vowelCount >=5):
    return print("many")
  else:
    return vowelCount
    
def bothEnds(self):
  if (len(self.s) <= 2):
    return ''
  return self.s[:2]+self.s[-2:]

def fixStart(self):
  n = self.s[1:]
  n.replace(self.s[0],'*')
  return self.s[0]+n

def asciiSum(self):
  total = 0
  for i in self.s:
    total += ord(i)
  return total
  
def cipher(self):
  key = len(self.s)
  encrypt = ''
  for i in self.s:
    if (i.isupper()):
      encrypt += chr((ord(i) + key - 65) % 26 +65)
    else:
      encrypt += chr((ord(i)+key -97) % 26 +97)
  return encrypt
  