
import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
from googleapiclient.discovery import build

my_api_key = "AIzaSyBz53R95HLj1-EFBiDpTn1TD4xCjwDoixY"
# my_api_key = "AIzaSyAYIJYkb2JhuZ6wwCPYZSJJZkmQNvbQ4OM" #The API_KEY you acquired
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
        return ""
        # raise Exception(e)
    except requests.exceptions.Timeout as e:
        return ""
        # raise Exception("Timed out!")
    htmldata = r.text
    soup = BeautifulSoup(htmldata, 'html.parser')  
    data = soup.getText()
    for pText in soup.find_all("p"):  
        data += pText.get_text() + "\n"  
    return data

def get_score(data: str) -> tuple:
    t = TextBlob(data)
    # t2 = TextBlob(data, analyzer=NaiveBayesAnalyzer())
    return (t.sentiment.polarity, t.sentiment.subjectivity)
    # return (t.sentiment.polarity, t.sentiment.subjectivity, t2.sentiment)

def get_status(data: str) -> bool:
    if len(data) < 100:
        return False
    return True

def get_info(q: str, number: int) -> list[dict]:
    results = google_search(q, my_api_key, my_cse_id, num=number)
    info = []
    for result in results:
        url = result['link']
        url_data = getdata(url)
        if(get_status(url_data)):
            info.append({"title":result['title'],"url":url, "snippet":result['snippet'],"score":get_score(url_data)})
    return info

if __name__ == "__main__":
    text = "love"
    print(get_score(text))
    