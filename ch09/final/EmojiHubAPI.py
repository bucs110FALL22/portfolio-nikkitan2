import requests
import json

class EmojiHubAPI:
  def __init__(self):
    self.api_url = "https://emojihub.yurace.pro/api/all"
  
  def get(self):
    response = requests.get(self.api_url)
    return response.json()