import requests

response = requests.get('http://api.gbif.org/v1/organization', params={'q': 'INBO'})
print 'raw text response: '
print response.text
data = response.json()
first_result = data['results'][0]
print first_result['description']