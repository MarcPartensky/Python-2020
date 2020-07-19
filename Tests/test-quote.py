import requests

url = "https://quotes15.p.rapidapi.com/quotes/random/"

querystring = {"language_code":"fr"}

headers = {
    'x-rapidapi-host': "quotes15.p.rapidapi.com",
    'x-rapidapi-key': "9f89a4d69emsh51b4e1005159b42p14a115jsn521840e553e7"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

