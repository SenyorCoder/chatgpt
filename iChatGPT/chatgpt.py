import json
import requests

def text(matn):

  url = "https://openai80.p.rapidapi.com/chat/completions"

  payload = {
    "model": "gpt-3.5-turbo",
    "messages": [
      {
        "role": "user",
        "content": matn
      }
    ]
  }
  headers = {
    "content-type": "application/json",
    "X-RapidAPI-Key": "2052bc373bmsh90938c82770c07fp1d3eadjsne5840c836aa5",
    "X-RapidAPI-Host": "openai80.p.rapidapi.com"
  }

  response = requests.request("POST", url, json=payload, headers=headers)
  rest = json.loads(response.text)
  return rest['choices'][0]['message']['content']