def star_pyramid():
  stars = int(input("Please enter the number of rows you would like."))
  for i in range(stars):
    print ("*" * (i+1))

star_pyramid()

def rstar_pyramid():
 stars = int(input("Please enter the number of rows you would like."))
 while stars != 0:
    print(stars*"*")
    stars -=1

rstar_pyramid()

