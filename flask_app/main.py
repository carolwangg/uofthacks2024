
import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
from googleapiclient.discovery import build

my_api_key = "AIzaSyAYIJYkb2JhuZ6wwCPYZSJJZkmQNvbQ4OM" #The API_KEY you acquired
my_cse_id = "17b679dc5a5aa4441" #The search-engine-ID you created


def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, fileType="html", cx=cse_id, **kwargs).execute()
    return res['items']


def getdata(url: str):  
    data = ""
    try:
        r = requests.get(url)
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        raise Exception(e)
    except requests.exceptions.Timeout as e:
        raise Exception("Timed out!")
    htmldata = r.text
    soup = BeautifulSoup(htmldata, 'html.parser')  
    for pText in soup.find_all("p"):  
        data += pText.get_text() + "\n"  
    return data

def get_score(data: str) -> tuple:
    t = TextBlob(data)
    return (t.sentiment.polarity, t.sentiment.subjectivity)

def get_status(data: str) -> bool:
    if len(data) < 100:
        return False
    return True

def get_info(q: str, number: int) -> list[dict]:
    results = google_search(q, my_api_key, my_cse_id, num=number)
    urls = []
    titles = []
    snippets = []
    for result in results:
        urls.append(result['link'])
        titles.append(result['title'])
        snippets.append(result['snippet'])
    
    data = []
    scores = []
    status = []
    for url in urls:
        url_data = getdata(url)
        data.append(url_data)
        scores.append(get_score(url_data))
        status.append(get_status(url_data))
    
    result = []
    for i in range(len(data)):
        result.append({"title":titles[i],"url":urls[i],"snippet":snippets[i],"score":scores[i],"status":status[i]})
    return result

if __name__ == "__main__":
    print(get_info('"trump"', 2))
    
    

