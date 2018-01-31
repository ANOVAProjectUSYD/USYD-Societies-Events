import urllib, facebook, requests, json, datetime, csv, time
from urllib.request import urlopen


def connect(page_id, token):
    '''Connect to FB Graph API and get data about society events.'''
    base = "https://graph.facebook.com/v2.11/"
    test_file = open('Test.csv', 'w')
    writer = csv.writer(test_file)

    #TODO: Why does session keep on expiring?
    parameters = "/?fields=events.limit(10)%7Battending_count%2Ccategory%2Cdeclined_count%2Cdescription%2Cend_time%2Cevent_times%2Cinterested_count%2Cmaybe_count%2Cname%2Cnoreply_count%2Cplace%2Cscheduled_publish_time%2Cstart_time%2Cticket_uri%2Ctype%7D&access_token=EAACEdEose0cBAAnZB6jhSiHFzwzapuTxDdDvbX8vxMOLUh2lTWIICBBZBJw2tsGr46Ea62pBLxjPO9EJlXBet8dgrsNZCBrBrMU2m20o9N7KRACM1fGRYDrPHhMzsXWx6mplOsZCWWd22lb1qjqxwU3WQuqIVpOaBDIaJYXxBSTADBM8xid0JAqQ6ZA3rtcmINDEikymjJwZDZD"
    url = base + page_id + parameters

    data = json.loads(urlopen(url).read())
    writer.writerow(["Society", "event_name", "attendance_count",
                     "interested_count", "no_reply_count", "declined_count",
                     "maybe_count", "total_invited_count", "description",
                     "start_time", "end_time", "place", "event_type" ])

    # What this return is a dictionary in a list in a dictionary in a dictionary.
    for i in range(0, len(data['events']['data'])):
        try:
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
            end_time = data_obj['end_time']
            place = data_obj['place']
            type_of_event = data_obj['type']

            writer.writerow(["180DC", name, attendance_count, interested_count,
                             no_reply_count, declined_count, maybe_count,
                             total_invited_count, description, start_time,
                             end_time, place, type_of_event])
        except Exception as e:
            continue

    test_file.close()


def read_data():
    '''Open CSV file and pass next entry to FB graph API.'''
    read_file = open('final_data.csv', 'r')
    reader = csv.reader(read_file, delimiter=',')
    for row in reader:
        if row[2] == "Facebook_ID":
            continue
        connect(row[2])


def main():
    token = 'EAACsR5scK9sBAPzJdyZBuiw7TBqfFMwUYw7qbZAuVI2FrRegxxdfsTqFPS51wF1NFklyV6ZA5HLHz7vAjRJwzPblbnrGiY6sfulSlqZBZASf1ZBG7qQcRjozmHGLlmajZCGNqClEYHZB7EOk6HrFRuEKZAc6MpZB6fZAgoZD'

    connect("180DegreesSydneyUniversity", token)
    read_data()


    #"https://graph.facebook.com/v2.11/180DegreesConsulting/?fields=events.limit(10)%7Battending_count%2Ccategory%2Cdeclined_count%2Cdescription%2Cend_time%2Cevent_times%2Cinterested_count%2Cmaybe_count%2Cname%2Cnoreply_count%2Cplace%2Cscheduled_publish_time%2Cstart_time%2Cticket_uri%2Ctype%7D&access_token=EAACEdEose0cBAAnZB6jhSiHFzwzapuTxDdDvbX8vxMOLUh2lTWIICBBZBJw2tsGr46Ea62pBLxjPO9EJlXBet8dgrsNZCBrBrMU2m20o9N7KRACM1fGRYDrPHhMzsXWx6mplOsZCWWd22lb1qjqxwU3WQuqIVpOaBDIaJYXxBSTADBM8xid0JAqQ6ZA3rtcmINDEikymjJwZDZD"

if __name__ == "__main__":
    main()
