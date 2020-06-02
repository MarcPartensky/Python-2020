# Import the api module for the results class
import search_google.api

# Define buildargs for cse api
buildargs = {
  'serviceName': 'customsearch',
  'version': 'v1',
  'developerKey': 'AIzaSyAAXUH2ywHr34ZCjlDzSyybsBc7_Wfgejg'
}

# Define cseargs for search
cseargs = {
  'q': 'keyword query',
  'cx': 'your_cse_id',
  'num': 3
}

# Create a results object
results = search_google.api.results(buildargs, cseargs)
print(results)
