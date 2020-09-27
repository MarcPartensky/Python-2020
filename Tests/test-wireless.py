from wireless import Wireless
import os
PASSWORD = os.environ['ISEP_HYPERPLANNING_PASSWORD']
wireless = Wireless()
print(wireless.interfaces())
if wireless.connect(ssid='en0', password=PASSWORD):
    print('success')
else:
    print('error')

