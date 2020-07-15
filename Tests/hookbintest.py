import requests

url = 'https://hookb.in/mZ16DkLRJDHeqq710qXL'

data = {
    "name": "John"
}

r = requests.post(url, verify=False, json=data)
