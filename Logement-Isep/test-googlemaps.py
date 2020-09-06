import googlemaps

from googlemaps_keys import api_keys

def login_no_matter_how(keys):
    for key in keys:
        try:
            print(key)
            client = googlemaps.Client(key=key)
            return client
        except:
            print('caught error')
            pass

client = login_no_matter_how(api_keys)

print(client.directions("Sydney", "Melbourne"))
