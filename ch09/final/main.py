# main.py
from EmojiHubAPI import EmojiHubAPI
from AztroAPI import AztroAPI

def main():
  emojihub = EmojiHubAPI()
  aztro = AztroAPI("sign", "day")

  emojihub_data = emojihub.get()
  aztro_data = aztro.get()

   # Check if aztro_data is None
  if aztro_data is None:
    print("Error: Could not get data from AztroAPI.")
  else:
    # Process and combine the data here...
  
  # Process and combine the data here...
    combined_data = []

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

  print(combined_data)

if __name__ == "__main__":
  main()
