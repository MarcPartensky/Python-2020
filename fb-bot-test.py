from fbchat import Client
# from fbchat.models import Message
from fbchat.models import *
import os


username = os.environ['FACEBOOK_MAIL']
password = os.environ['FACEBOOK_PASSWORD']
# login
client = Client(username, password)

# users = client.fetchThreadList()
# print(users)


users = client.searchForUsers('Paul Vaugier')
print(users[0])
