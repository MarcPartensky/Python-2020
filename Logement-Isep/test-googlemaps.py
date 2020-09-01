import googlemaps

from googlemaps_keys import api_keys

def login_no_matter_how(keys):
    for key in keys:
        try:
            return  googlemaps.Client(key=key)
        except:
            pass

client = login_no_matter_how(api_keys)

print(client.directions("Sydney", "Melbourne"))
