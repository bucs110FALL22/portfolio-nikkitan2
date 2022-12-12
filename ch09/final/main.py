# main.py
from EmojiHubAPI import EmojiHubAPI
from AztroAPI import AztroAPI

def main():
  emojihub = EmojiHubAPI()
  aztro = AztroAPI("today")

  
  signnames = ['aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 'libra', 'scorpio', 'sagittarius', 'capricorn', 'aquarius', 'pisces']
  go = True
  while go:
    print('''
    1: aries
    2: taurus
    3: gemini
    4: cancer
    5: leo
    6: virgo
    7: libra
    8: scorpio
    9: sagittarius
    10: capricorn
    11: aquarius
    12: pisces
    ''')
    sign = input("please input the number to the sign you are")
    sign = sign.strip()
    try:
      sign = int(sign)
      if not (0 < sign < 13):
        print("Number is out of range")
        continue
    except:
      print("Input did not match format")
      continue
    sign = signnames[sign]
    aztro_data = aztro.get(sign)
    emojihub_data = emojihub.get()
    emoji = emojihub_data["unicode"][0].replace("+", "000")
    # emoji = "{" + emoji + "}"
    print("Your lucky color today is: " + aztro_data["color"])
    print("Personally, that color makes me feel like this", emoji)
    # TODO: get this work
    # print(eval(rf"\{emoji}"))

if __name__ == "__main__":
  main()
