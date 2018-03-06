import csv
with open('final_data.csv', encoding = 'utf-8') as csvfile:
    read = csv.reader(csvfile, delimiter = ',')
    for row in read:
        description = row[8].lower()
        event_name = row[1].lower()
        if 'food' in description or 'pizza' in description or 'sausages' in description or 'BBQ' in description or 'BBQ\'s' in description or 'vegetarian' in description or 'pub crawl' in event_name:
            print (1)
        else:
            print (0)
