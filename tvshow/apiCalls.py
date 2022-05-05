import urllib.request, json
apiPath = "https://api.themoviedb.org/3/"
api_key = "b3786a390467799c11abd24aaa2ea7b4"
types = []
def dataToDict(url):
    url = url.replace(" ", "%20")
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)
    return dict


    
def apiCallTrending(type):
    url =f'{apiPath}trending/{type}/day?api_key={api_key}'
    dict =  dataToDict(url)
    return dict['results']

def apiCallPopular(type):
    url =f'{apiPath}{type}/popular?api_key={api_key}'
    dict =  dataToDict(url)
    return dict['results']

def apiCallSearch(type:any,query:any)->any:
    url =f'{apiPath}search/{type}?api_key={api_key}&query={query}'
    dict =  dataToDict(url)
    dict = dict['results']
    for i in dict:
        i['type'] = f'{type}'
    return dict

def apiCall(type,id):
    url =f'{apiPath}{type}/{id}?api_key={api_key}'
    dict =  dataToDict(url)
    return dict

def apiCallCast(type,id):
    url =f'{apiPath}{type}/{id}/credits?api_key={api_key}'
    dict =  dataToDict(url)
    return dict['cast']

def apiCallPerson(person):
    url =f'{apiPath}search/person?api_key={api_key}&query={person}'
    dict =  dataToDict(url)
    return dict['results']

def apiCallPersonDetails(person):
    results = apiCallPerson(person)
    for result in results:
        if result['name'] == person:
            id = result['id']
            break
    url =f'{apiPath}person/{id}?api_key={api_key}'
    dict =  dataToDict(url)
    return dict


