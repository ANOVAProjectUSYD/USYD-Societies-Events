from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError
import datetime, csv, time

def get_website():
    '''Ensure call to USU website is successful.'''
    try:
        html = urlopen('http://www.usu.edu.au/Our-Clubs-Societies/Our-clubs-societies.aspx')
    except HTTPError as e:
        # Page not found exception.
        print('Cannot connect to website at this time.')
        return
    if html is None:
        # Server is not found.
        print('Server not found.')
        return
    else:
        print("Success in connecting!")
        return html

def parse_site(html):
    '''Trawl USU webpage and return Facebook pages of each society on it.'''
    bs_Obj = BeautifulSoup(html, "html.parser")
    # Grab every society and USU listing from the page.
    names_list = []
    link_list = []
    for lists in bs_Obj.findAll("div", {"span5 clubhack"}):
        for club in lists.select("li"):
            names_list.append(club.text.strip())
        # Gets the USU link to the society.
        for a in lists.find_all('a', href=True):
            if a.get_text(strip=True):
                link_list.append(a['href'])

    return names_list, link_list


def get_fb_link(names_list, link_list):
    '''Create CSV file with name of society and Facebook link.'''
    # FB page for USU is an URL, not HTML so need to do this.
    URL = 'http://www.usu.edu.au'
    scrape_start = datetime.datetime.now()
    with open('societies_facebook.csv', 'w') as file:
        w = csv.writer(file)
        w.writerow(["Society", "Facebook Link"])
        for index in range(0, len(names_list)):
            usu_page = URL + link_list[index]
            html = urlopen(usu_page)
            if html is None:
                print("Error encountered for %s" % (names_list[index]))
                continue
            # Get the actual page of the society on USU.
            soup = BeautifulSoup(html, "html.parser")
            # Get Facebook URL of society.
            fb_url = soup.find("a", {"class": "facebook social-icon"}, href=True)['href']
            w.writerow([names_list[index], fb_url])
            if index % 10 ==0:
                print("Procssed %s societies so far: %s" % (index, datetime.datetime.now()))
        file.close()
    print("Done processing in %s" % (datetime.datetime.now() - scrape_start))


def get_facebook_likes():
    '''Connect to the Facebook page of each society.'''
    # TODO: Given the Facebook Link, get the number of likes for the page.
    reader = csv.reader(open('societies_facebook.csv', 'r'))
    for row in reader:
        if row[1] == 'Facebook Link':
            continue
        print(row[1])
        # TODO: Rewrite with Facebook Graph API.
        html = urlopen(row[1])
        if html is None:
            print("Error in connecting.")
        soup = BeautifulSoup(html, "html.parser")
        likes = soup.find("div", {"id": "u_0_f"})
        print(likes)
        print(likes.find("a", {"id": "u_0_f"}, href=True))
    #_4bl9

def grab_facebook_data(page_id, access_token, limit_status):
    '''Access Facebook data.'''
    # Construct the URL string
    token = 'EAACsR5scK9sBAEYiD8VoXPbJvDAOO9VQ7eRUSGTOu4YuN7tjf8KRFr9GZAhGCrU0wbFSL44VBbENKTUpdGLQXivNETGVXsvrTIRtCCPtMZC78YjYEzLeNeHksilobxRA36acDI2PMJvaCUzJppBfUtjKhhi37oX2Iv2bWadwZDZD'
    base = "https://graph.facebook.com/v2.4"
    node = "/" + page_id +"/feed"
    parameters = "/?fields=message,link,created_time,type,name,id,likes.limit(1).summary(true),comments.limit(1).summary(true),shares&limit=%s&access_token=%s" % (limit_status, access_token) # changed
    url = base + node + parameters
    # Retrieve data
    response = urlopen(url)
    data = json.loads(response.read())
    return data


def main():
    #html = get_website()
    #names_list, link_list = parse_site(html)
    #get_fb_link(names_list, link_list)
    get_facebook_likes()


if __name__ == "__main__":
    main()
