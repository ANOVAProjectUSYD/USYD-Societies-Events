import urllib, facebook, requests, json, datetime, csv, time
from urllib.request import urlopen


def initial_write(name):
    '''Create and write first entry in file.'''
    csv_file = name + '.csv'
    write_file = open(csv_file, 'w')
    writer = csv.writer(write_file)
    writer.writerow(["Society", "event_name", "attendance_count",
                     "interested_count", "no_reply_count", "declined_count",
                     "maybe_count", "total_invited_count", "description",
                     "start_time", "place" ])
    write_file.close()


def read_data(token):
    '''Open CSV file and pass next entry to FB graph API.'''
    read_file = open('final_data.csv', 'r')
    reader = csv.reader(read_file, delimiter=',')

    initial_write('final_data_2')

    for row in reader:
        if row[2] == "Facebook_ID":
            continue
        scrape_api(token, row[2], 'final_data_2') # scrapes info about the society

    read_file.close()


def scrape_api(token, society, file_name):
    '''Scraping FB data.'''
    base = "https://graph.facebook.com/v2.12/"
    url = "?fields=events.limit(100)%7Bname%2Cattending_count%2Cinterested_count%2Cnoreply_count%2Cdeclined_count%2Cmaybe_count%2Cdescription%2Cstart_time%2Cplace%7D&access_token="
    link = base + society + url + token
    data = json.loads(urlopen(link).read())
    print(society)
    total_scrape = 0
    fail_scrape = 0
    csv_file = file_name + '.csv'
    write_file = open(csv_file, 'a')
    writer = csv.writer(write_file)
    # collects all the data regarding events
    for i in range(0, len(data['events']['data'])):
        try:
            # what this return is a dictionary in a list in a nested dict.
            data_obj = data['events']['data'][i]
            name = data_obj['name']
            attendance_count = data_obj['attending_count']
            interested_count = data_obj['interested_count']
            no_reply_count = data_obj['noreply_count']
            declined_count = data_obj['declined_count']
            maybe_count = data_obj['maybe_count']
            total_invited_count = attendance_count + interested_count + no_reply_count + declined_count + maybe_count
            description = data_obj['description']
            start_time = data_obj['start_time']
            place = data_obj['place']
            writer.writerow([society, name, attendance_count, interested_count,
                             no_reply_count, declined_count, maybe_count,
                             total_invited_count, description, start_time,
                             place])
            total_scrape +=1
        except Exception as e:
            fail_scrape +=1
            continue

    write_file.close()

    print("{event_num} were scraped".format(event_num = total_scrape))
    print("{fail_num} failed scrapes".format(fail_num = fail_scrape))


def main():
    token = 'EAACEdEose0cBALbpMDjM32oWIQla52FxGqtykoO5MlGQR45exf5GLBPsJYNgp7gofVcQNHLzo5ffNq1KeuKVhabm2YQzKGRPFLpherblPSz19uovZCKPX5roGtMXLDvttKDUfFOB32TZAzrjiwOLoyznNZB7TFLLQsI9z7Bx3i42b9FNNBv38VVoKJaK2CSrs6YgJtp0wZDZD'

    read_data(token)


if __name__ == "__main__":
    main()
