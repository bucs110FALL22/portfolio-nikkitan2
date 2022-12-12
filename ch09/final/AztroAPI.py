import requests

class AztroAPI:

  def __init__(self, day):
    self.api_url = "https://aztro.sameerkumar.website"
    self.day = day
   
  def get(self, sign):
    response = requests.post(self.api_url, params={"sign": sign, "day": self.day})
    return response.json()
