import html2text
import requests

r = requests.get("https://pypi.org/project/html2text/")
h = html2text.HTML2Text()
text = h.handle(r.text)
print(text)
