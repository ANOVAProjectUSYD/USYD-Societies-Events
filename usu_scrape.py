from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError


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
    table = bs_Obj.findAll("div", {"class": "span5 clubhack"})
    # TODO: Grab every society from this. Currently only gets the first one.
    for i in range(0, len(table)):
        list_of_club = table[i].findAll("li")
        # print(type(list_of_club[0]))
        # print(table[i].text.strip())
    # for x in table:
    #     print(x)
    return

def get_fb_link():
    URL = 'http://www.usu.edu.au/Clubs-Societies/Our-clubs-societies/Political/Greens-on-Campus.aspx'
    # TODO: Scrape the FB link for the page and return the link to FB.
    # FB page for USU is an URL, not HTML so need to do this.
    soup = BeautifulSoup(urlopen(URL), "html.parser")
    print(soup.find('a', href=True))

def get_facebook_likes(society):
    '''Connect to the Facebook page of each society.'''
    # TODO: Given the Facebook Link, get the number of likes for the page.

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
    html = get_website()
    parse_site(html)
    # get_facebook('hi')

if __name__ == "__main__":
    main()
