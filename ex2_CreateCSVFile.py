import csv

# Let's create a csv file containing data from week days
outfile = open('data.csv', 'w+')
writer = csv.writer(outfile, delimiter=',')
data = [
    ['monday', 'maandag', 1],
    ['tuesday', 'dinsdag', 2],
    ['wednesday', 'woensdag', 3],
    ['thursday', 'donderdag', 4],
    ['friday', 'vrijdag', 5],
    ['saturday', 'zaterdag', 6],
    ['sunday', 'zondag', 7]
]
writer.writerow(['day_eng', 'day_nl', 'day_nr'])
for row in data:
    writer.writerow(row)

outfile.close()

# Now let's read that data and produce some output
infile = open('data.csv')
reader = csv.reader(infile, delimiter=',')
data = []
for row in reader:
    data.append(row)
for i in [2, 4, 7]:
    print 'Today is {0}'.format(data[i][0])

infile.close()