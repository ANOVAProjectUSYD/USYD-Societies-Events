import csv
with open('final_data.csv', encoding = 'utf-8') as csvfile:
    read = csv.reader(csvfile, delimiter = ',')
    for row in read:
        description = row[8].lower()
        if 'alcohol' in description or 'wine' in description or 'beer' in description or 'drinks' in description or 'jug' or 'jugs':
            print (1)
        else:
            print (0)
