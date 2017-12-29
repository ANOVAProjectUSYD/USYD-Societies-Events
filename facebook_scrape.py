import urllib
import facebook
import requests

# https://github.com/mobolic/facebook-sdk#egg=facebook-sdk
# http://facebook-sdk.readthedocs.io/en/latest/install.html
def get_connected(token):
    '''Connect to the Facebook Graph API.'''
    graph = facebook.GraphAPI(access_token=token, version=2.11)
    subs = graph.search(type='page',q="Sydney University Business Society - SUBS")
    print(subs['data'])
    # https://developers.facebook.com/tools/explorer?method=GET&path=SydneyUniversityBusinessSociety%2Fevents%3Flimit%3D3&version=v2.11

def query_graph(society_list):
    '''Return events for each society.'''

def main():
    token = 'EAACsR5scK9sBAEYiD8VoXPbJvDAOO9VQ7eRUSGTOu4YuN7tjf8KRFr9GZAhGCrU0wbFSL44VBbENKTUpdGLQXivNETGVXsvrTIRtCCPtMZC78YjYEzLeNeHksilobxRA36acDI2PMJvaCUzJppBfUtjKhhi37oX2Iv2bWadwZDZD'
    get_connected(token)


if __name__ == "__main__":
    main()
