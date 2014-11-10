import csv

infile = open('data.csv')
outfile = open('new_data.csv', 'w+')

reader = csv.reader(infile, delimiter=',')
writer = csv.writer(outfile, delimiter=';')
for row in reader:
    outrow = [row[1], row[2], row[0]]
    writer.writerow(outrow)
infile.close()
outfile.close()
