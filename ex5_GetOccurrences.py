import requests
import dateutil.parser
import csv

parameters = {'scientificName': 'Larus', 'decimalLatitude': '49.5,51.5', 'decimalLongitude': '2.5456,6.406'}
response = requests.get('http://api.gbif.org/v1/occurrence/search', params=parameters)
data = response.json()
outfile = open('occurrence_data.csv', 'w+')
writer = csv.writer(outfile, delimiter='\t')
print 'number of records found: {0}\n\n'.format(data['count'])
header = ['species', 'observation_type', 'owner_institute', 'year', 'month', 'day', 'hour', 'minutes', 'decimal_latitude', 'decimal_longitude']
writer.writerow(header)
for record in data['results']:
    species = record['species']
    observation_type = record['basisOfRecord']
    owner_institute = record['ownerInstitutionCode']
    date_string = record['eventDate']
    date = dateutil.parser.parse(date_string)
    dec_lat = record['decimalLatitude']
    dec_long = record['decimalLongitude']
    out_row = [species, observation_type, owner_institute, date.year, date.month, date.day, date.hour, date.minute, dec_lat, dec_long]
    writer.writerow(out_row)
outfile.close()