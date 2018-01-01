import urllib, facebook, requests, json, datetime, csv, time
from urllib.request import urlopen


def grab_facebook_data(page_id, access_token, limit_status):
    '''Access Facebook data.'''
    # Construct the URL string
    base = "https://graph.facebook.com/v2.4"
    node = "/" + page_id +"/feed"
    parameters = "/?fields=message,link,created_time,type,name,id,likes.limit(1).summary(true),comments.limit(1).summary(true),shares&limit=%s&access_token=%s" % (limit_status, access_token) # changed
    url = base + node + parameters
    # Retrieve data
    data = json.loads(request_until_succeed(url))
    return data


def request_until_succeed(url):
    '''Helps to prevent HTTP:5000 error.'''
    response = urlopen(url)
    success = False
    while success is False:
        try:
            response = urlopen(url)
            if response.getcode() == 200:
                success = True
        except Exception as e:
            print(e)
            time.sleep(5)
            print("Error for URL %s: %s" % (url, datetime.datetime.now()))
    return response.read()


def print_data(data):
    '''Print out the json dump given to us from testFacebookPageData.'''
    print(json.dumps(data, indent=4, sort_keys=True))


def process_page_status(status):
    '''Process each field in the Facebook data.'''
    # The status is now a Python dictionary, so for top-level items,
    # we can simply call the key.

    # Additionally, some items may not always exist,
    # so must check for existence first
    status_id = status['id']
    status_message = '' if 'message' not in status.keys() else status['message'].encode('utf-8')
    link_name = '' if 'name' not in status.keys() else status['name'].encode('utf-8')
    status_type = status['type']
    status_link = '' if 'link' not in status.keys() else status['link']

    # Time needs special care since it is in UTC and not easy to use in statistical programs.
    status_published = datetime.datetime.strptime(status['created_time'],'%Y-%m-%dT%H:%M:%S+0000')
    status_published = status_published + datetime.timedelta(hours=-5) # EST
    status_published = status_published.strftime('%Y-%m-%d %H:%M:%S') # Best time format for spreadsheet.

    # Nested items require chaining dictionary keys.
    num_likes = 0 if 'likes' not in status.keys() else status['likes']['summary']['total_count']
    num_comments = 0 if 'comments' not in status.keys() else status['comments']['summary']['total_count']
    num_shares = 0 if 'shares' not in status.keys() else status['shares']['count']

    # return a tuple of all processed data
    return (status_id, status_message, link_name, status_type, status_link,
           status_published, num_likes, num_comments, num_shares)

def scrape_facebook_page_status(page_id, access_token):
    '''Scraping Facebook statuses for the page and writing to csv file.'''
    with open('%s_facebook_statuses.csv' % page_id, 'w') as file:
        w = csv.writer(file)
        w.writerow(["status_id", "status_message", "link_name", "status_type", "status_link", "status_published", "num_likes", "num_comments", "num_shares"])
        has_next_page = True
        num_processed = 0   # keep a count on how many we've processed
        scrape_starttime = datetime.datetime.now()
        print("Scraping %s Facebook Page: %s\n" % (page_id, scrape_starttime))
        statuses = grab_facebook_data(page_id, access_token, 10)
        done_scraping = False
        while has_next_page:
            if done_scraping == True:
                break
            for status in statuses['data']:
                w.writerow(process_page_status(status))
                # Output progress occasionally to make sure code is not stalling
                num_processed += 1
                if num_processed == 50:
                    # Determines how many statuses we would like to scrape.
                    done_scraping = True
                    break
                if num_processed % 10 == 0:
                    print("%s Statuses Processed: %s" % (num_processed, datetime.datetime.now()))

            # Ff there is no next page, we're done.
            if 'paging' in statuses.keys():
                statuses = json.loads(request_until_succeed(statuses['paging']['next']))
            else:
                has_next_page = False
        print("\nDone!\n%s Statuses Processed in %s" %
             (num_processed, datetime.datetime.now() - scrape_starttime))


def main():
    token = 'EAACsR5scK9sBAEYiD8VoXPbJvDAOO9VQ7eRUSGTOu4YuN7tjf8KRFr9GZAhGCrU0wbFSL44VBbENKTUpdGLQXivNETGVXsvrTIRtCCPtMZC78YjYEzLeNeHksilobxRA36acDI2PMJvaCUzJppBfUtjKhhi37oX2Iv2bWadwZDZD'
    # We need to access the data key and everything is stored in the first index.
    page_id = "SydneyUniversityBusinessSociety"
    socities_to_scrape = ["SydneyUniversityBusinessSociety", "SydneyUniversityLawSociety", "SUITSUsyd"]
    scrape_facebook_page_status(page_id, token)


if __name__ == "__main__":
    main()
