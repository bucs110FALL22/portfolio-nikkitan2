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

    def asciiSum(self):
        ans = 0
        for i in range(len(self.s)):
            ans = ans + ord(self.s[i])
        return ans
    
    def cipher(self):
        l = len(self.s)
        out=''
        for i in range(l):
            if ord(self.s[i]) in range(65, 91):
                if ord(self.s[i]) + l <=90:
                    out = out + chr(ord(self.s[i]) + l)
                else:
                    out = out + chr(ord('A') + ord(self.s[i]) + l - 90)
            
            elif ord(self.s[i]) in range(97, 123):
                if ord(self.s[i]) + l <=122:
                    out = out + chr(ord(self.s[i]) + l)
                else:
                    out = out + chr(ord('A') + ord(self.s[i]) + l - 122)
            else:
                out = out + self.s[i]
        return out
