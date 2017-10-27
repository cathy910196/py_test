import csv
with open('test2.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
     		print(row['first'], row[' a'])