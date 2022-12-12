import requests

# Get the user's birthdate from the command line
birthdate = input("Enter your birthdate in the format YYYY-MM-DD: ")

# Use the requests library to make an HTTP GET request to the aztro API
response = requests.get("https://aztro.sameerkumar.website/api?date={}".format(birthdate))

# Parse the JSON data returned by the aztro API
data = response.json()

# Get the user's astrological sign from the data
sign = data["sign"]

# Use the requests library to make an HTTP GET request to the emojihub API
response = requests.get("https://emoji-hub.com/api/animals/{}".format(sign))

# Parse the JSON data returned by the emojihub API
data = response.json()

# Get the appropriate animal emoji for the user's zodiac sign
emoji = data["emoji"]

# Print the message
print("Based on your birthdate ({}), your zodiac sign is: {} {}".format(birthdate, sign, emoji))




for emoji in emojihub_data:
  # Check if the name of the current emoji exists in the aztro_data object
  if emoji["name"].lower() in aztro_data:
    # If it does, then access the description of the emoji
    description = aztro_data[emoji["name"].lower()]
  else:
    # If it doesn't, then set the description to an empty string
    description = ""

  combined_data.append({
    "name": emoji["name"],
    "htmlCode": emoji["htmlCode"],
    "description": description
  })

