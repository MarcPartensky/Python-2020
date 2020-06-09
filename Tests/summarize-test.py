import requests

url = "https://text-monkey-summarizer.p.rapidapi.com/nlp/summarize"

payload = "{ \"url\": \"https://en.wikipedia.org/wiki/Adolf_Hitler\"}"
headers = {
    'x-rapidapi-host': "text-monkey-summarizer.p.rapidapi.com",
    'x-rapidapi-key': "9f89a4d69emsh51b4e1005159b42p14a115jsn521840e553e7",
    'content-type': "application/json",
    'accept': "application/json"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
