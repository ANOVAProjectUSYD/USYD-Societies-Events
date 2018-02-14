import urllib, requests, json, datetime, csv, time
from urllib.request import urlopen

def get_facebook_likes(token):
    '''Get the number of Facebook likes for each society.'''
    with open('usu_societies.csv', 'r', encoding='utf8') as ogFile:
        tempFile = open('final_societies_facebook.csv', 'w')
        reader = csv.reader(ogFile, delimiter=',')
        writer = csv.writer(tempFile)
        writer.writerow(["Society", "Facebook_Link", "Facebook_ID", "Category", "Likes"])
        count = 0
        print("Reading file was successful.")
        for row in reader:
            if count ==0:
                count = count+1
                continue

            page_id = row[2]
            base = "https://graph.facebook.com/v2.11/"
            # fan_count gets us number of likes for the page
            # note that if global, then all pages across brand
            parameters = "/?fields=fan_count,username&access_token=%s" % (token)
            try:
                url = base + page_id + parameters
                data = json.loads(urlopen(url).read())
                writer.writerow([row[0], row[1], data["username"], row[3], data["fan_count"]])
            except Exception as e:
                writer.writerow([row[0], row[1], row[2], row[3], 0])

            if count % 10 ==0:
                print("Procssed %s societies so far" % (count))
            count = count+1

        ogFile.close()
        tempFile.close()
    print("Done writing!")


def main():
    token = 'EAACsR5scK9sBAEYiD8VoXPbJvDAOO9VQ7eRUSGTOu4YuN7tjf8KRFr9GZAhGCrU0wbFSL44VBbENKTUpdGLQXivNETGVXsvrTIRtCCPtMZC78YjYEzLeNeHksilobxRA36acDI2PMJvaCUzJppBfUtjKhhi37oX2Iv2bWadwZDZD'
    get_facebook_likes(token)


if __name__ == "__main__":
    main()
