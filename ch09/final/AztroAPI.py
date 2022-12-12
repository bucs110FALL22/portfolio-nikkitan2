import requests

class AztroAPI:

  def __init__(self):
    self.api_url = "https://aztro.sameerkumar.website"
    self.sign = sign
    self.day = day
   
  def get(self):
    response = requests.get(self.api_url, params={"sign": self.sign, "day": self.day})
    return response.json()
