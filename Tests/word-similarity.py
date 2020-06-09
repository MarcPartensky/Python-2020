import requests
import re

r = requests.get('https://wordsimilarity.com/en/dog')
pattern = re.compile('/en/([a-z]+)')
results = re.findall(pattern, r.text)

print(results)
