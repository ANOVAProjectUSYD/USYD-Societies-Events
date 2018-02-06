from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError
import datetime, csv, time

def get_website():
    '''Ensure call to USU website is successful.'''
    try:
        html = urlopen('http://www.usu.edu.au/Our-Clubs-Societies/Our-clubs-societies.aspx')
    except HTTPError as e:
        # page not found exception
        print('Cannot connect to website at this time.')
        return
    if html is None:
        # server is not found
        print('Server not found.')
        return
    else:
        print("Success in connecting!")
        return html


def parse_site(html):
    '''Trawl USU webpage and return individual page of each society.'''
    bs_Obj = BeautifulSoup(html, "html.parser")
    # grab every society and USU listing from the page
    names_list = []
    link_list = []
    for lists in bs_Obj.findAll("div", {"span5 clubhack"}):
        for club in lists.select("li"):
            names_list.append(club.text.strip())
        # gets the USU link to the society
        for a in lists.find_all('a', href=True):
            if a.get_text(strip=True):
                link_list.append(a['href'])

    return names_list, link_list


def get_fb_link(names_list, link_list):
    '''Create CSV file with name of society and Facebook link.'''
    # FB page for USU is an URL, not HTML so need to do this
    URL = 'http://www.usu.edu.au'
    scrape_start = datetime.datetime.now()
    with open('usu_societies.csv', 'w') as file:
        w = csv.writer(file)
        w.writerow(["Society", "Facebook Link", "Facebook ID", "Category"])
        for index in range(0, len(names_list)):
            usu_page = URL + link_list[index]
            html = urlopen(usu_page)
            if html is None:
                print("Error encountered for %s" % (names_list[index]))
                continue
            # we want the type of society they are on USU page which is in URL
            split_cat = link_list[index].split("-clubs-societies/", 1)[1]
            # now second split to just get the category
            category = split_cat.split("/", 1)[0]
            try:
                # get the actual page of the society on USU
                soup = BeautifulSoup(html, "html.parser")
                # get Facebook URL of society
                fb_url = soup.find("a", {"class": "facebook social-icon"}, href=True)['href']
                # we want the Facebook page id which comes after .com/
                fb_page_id = fb_url.split(".com/", 1)[1]
                w.writerow([names_list[index], fb_url, fb_page_id, category])
            except Exception as e:
                print("Error with %s" % (names_list[index]))
                print(e)
                w.writerow([names_list[index], "NONE", "NONE", category])
                continue

            if index % 10 ==0:
                print("Procssed %s societies so far: %s" % (index, datetime.datetime.now()))
        file.close()

    print("Done processing in %s" % (datetime.datetime.now() - scrape_start))


def main():
    html = get_website()
    names_list, link_list = parse_site(html)
    get_fb_link(names_list, link_list)


if __name__ == "__main__":
    main()
