import requests
import json

# Everything relies on the mediawiki API and the numeric article ID
# There are fancier ways to implement the various API parameters but they seem like more work than is necessary
api = 'https://www.wikihow.com/api.php?format=json&action='


def return_details(id):
    article_details = {}
    r = requests.get(
        api + 'query&prop=info|templates|categories&inprop=url&pageids=' + str(id))
    data = r.json()
    article_details['url'] = data['query']['pages'][str(id)]['fullurl']
    return article_details


def search(search_term, max_results=10):
    search_results = []
    r = requests.get(api + 'query&format=json&utf8=&list=search&srsearch=' +
                     search_term + "&srlimit=" + str(max_results))
    data = r.json()
    if not data:
        return "Fuck"
    else:
        data = data['query']['search']
        return return_details(data[0]['pageid'])['url']


if __name__ == "__main__":
    print('Hey get outta here')
