
import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
from googleapiclient.discovery import build
# import selenium.webdriver as webdriver

my_api_key = None
my_cse_id = None #The search-engine-ID you created


def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, fileType="", cx=cse_id, **kwargs).execute()
    return res['items']


def getdata(session, url: str):  
    data = ""
    try:
        htmldata = requests.get(url).text
        htmldata[:1000]
        #driver = webdriver.Firefox()
        #driver.get(url)
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        return ""
        # raise Exception(e)
    except requests.exceptions.Timeout as e:
        return ""
        # raise Exception("Timed out!")
    #soup = BeautifulSoup(driver.page_source)  
    soup = BeautifulSoup(htmldata, 'html.parser')  
    data = " "
    for pText in soup.find_all("p"):  
        data += pText.get_text() + "\n"  
    return data

def get_score(data: str, title: str, snippet: str) -> tuple:
    ratioData = 0.7
    ratioSnippet = 0.2
    t1 = TextBlob(data)
    t2 = TextBlob(title)
    t3 = TextBlob(snippet)
    # temp1= t1.sentiment.polarity
    # temp2 = t2.sentiment.polarity
    # temp3 = t1.sentiment.subjectivity
    # temp4 = t2.sentiment.subjectivity
    # t2 = TextBlob(data, analyzer=NaiveBayesAnalyzer())
    if (t2.sentiment.polarity or t2.sentiment.subjectivity):
        return (t1.sentiment.polarity * ratioData + t2.sentiment.polarity*(1-ratioData-ratioSnippet) + t3.sentiment.polarity * ratioSnippet, t1.sentiment.subjectivity *ratioData + t2.sentiment.subjectivity*(1-ratioData-ratioSnippet) + t3.sentiment.polarity * ratioSnippet )
    else:
        return (t1.sentiment.polarity, t1.sentiment.subjectivity)
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
        session = requests.Session()
        url_data = getdata(session, url)
        if(get_status(url_data)):
            title = result['title']
            snippet = result['snippet']
            info.append({"title":title,"url":url, "snippet":snippet,"score":get_score(url_data, title, snippet)})
    return info

# def test():
#     from urllib import request
#     url = "https://www.utoronto.ca/"
    
#     htmldata = requests.get(url).text
#     htmldata[:60]
#     from bs4 import BeautifulSoup
#     soup = BeautifulSoup(htmldata, 'html.parser')
#     session = requests.Session()
#     data = getdata(session, url)
#     title = soup.title.string
#     print(get_score(data, title, snippet))

if __name__ == "__main__":
    # test()
    print(get_info('"Taylor Swift"', 5))
