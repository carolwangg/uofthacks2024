
import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
from googleapiclient.discovery import build
# import selenium.webdriver as webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
from requests_html import HTMLSession, AsyncHTMLSession
import pyppeteer
# my_api_key = "AIzaSyBz53R95HLj1-EFBiDpTn1TD4xCjwDoixY"
# my_api_key = "AIzaSyAYIJYkb2JhuZ6wwCPYZSJJZkmQNvbQ4OM" #The API_KEY you acquired

# my_api_key = "AIzaSyARCsFukjY_JTBbiFsCG2NVjuBIXF56M-w"
my_api_key ="AIzaSyAVQUFUt2fVXjjqqkNuT73I2qAK_CPt864" #performance

my_cse_id = "17b679dc5a5aa4441" #The search-engine-ID you created
PYPPETEER_CHROMIUM_REVISION = '1263111'

from pyppeteer import launch

def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, fileType="", cx=cse_id, **kwargs).execute()
    return res['items']


# async def getdata(session, url: str):  
#     # Configure headless mode
#     # options = Options()
#     # options.add_argument('--headless')
#     # options.add_argument('--disable-gpu')
#     # options.add_argument('--window-size=1920,1080')  # Optional for layout-related JS rendering
#     # driver = webdriver.Chrome()
#     h = "hello"
#     try:
#         asession = AsyncHTMLSession()
#         r = await asession.get('https://python.org/')
#         # driver.get(url)
#         #driver = webdriver.Firefox()
#         #driver.get(url)
#     except requests.exceptions.WebDriverException as e:  # This is the correct syntax
#         return ""
#         # raise Exception(e)
#     except requests.exceptions.Timeout as e:
#         return ""
#         # raise Exception("Timed out!")
#     # htmldata1 = driver.page_source
#     # htmldata2 = requests.get(url).text
#     # driver.quit()
#     await r.html.arender()
#     soup = BeautifulSoup(r.html.html, 'html5lib')  
#     data = " "
#     for pText in soup.find_all("p"):  
#         data += pText.get_text() + "\n"
#     return data

def getdata(session, url: str):  
    # Configure headless mode
    # options = Options()
    # options.add_argument('--headless')
    # options.add_argument('--disable-gpu')
    # options.add_argument('--window-size=1920,1080')  # Optional for layout-related JS rendering
    # driver = webdriver.Chrome()
    h = "hello"
    try:
        session = HTMLSession()
        r = session.get(url, timeout=10)
        r.html.render()
        soup = BeautifulSoup(r.html.html, 'html5lib')  
        # driver.get(url)
        #driver = webdriver.Firefox()
        #driver.get(url)
    except requests.exceptions.Timeout as e:
        return ""
    except requests.exceptions.ConnectionError as e:
        return ""
    except requests.exceptions.RequestException as e:
        return ""
    except requests.exceptions.HTTPError as e:
        return ""
    except pyppeteer.errors.NetworkError:
        return ""
        # raise Exception("Timed out!")
    # htmldata1 = driver.page_source
    # htmldata2 = requests.get(url).text
    # driver.quit()
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

# async def get_info(q: str, number: int) -> list[dict]:
#     results = google_search(q, my_api_key, my_cse_id, num=number)
#     info = []
#     for result in results:
#         url = result['link']
#         session = requests.Session()
#         url_data = await getdata(session, url)
#         if(get_status(url_data)):
#             title = result['title']
#             snippet = result['snippet']
#             info.append({"title":title,"url":url, "snippet":snippet,"score":get_score(url_data, title, snippet)})
#     return info
def get_info(q: str, number: int) -> list[dict]:
    results = google_search(q, my_api_key, my_cse_id, num=number)
    info = []
    for result in results:
        url = result['link']
        session = requests.Session()
        url_data = getdata(session, url)
        session.close()
        if(get_status(url_data)):
            title = result['title']
            snippet = result['snippet']
            info.append({"title":title,"url":url, "snippet":snippet,"score":get_score(url_data, title, snippet)})
    return info
# def test():
#     url = "https://www.newswire.ca/news-releases/kognitiv-corporation-announces-shawn-pearson-joins-as-president--890145706.html"
#     driver = webdriver.Chrome()
#     driver.get(url)
#     htmldata = driver.page_source
#     soup = BeautifulSoup(htmldata, 'html5lib')  
#     data = " "
#     for pText in soup.find_all("p"):  
#         data += pText.get_text() + "\n"  
#     driver.quit()
#     print(data)
    

if __name__ == "__main__":
    # test()
    print(get_info('"Taylor Swift"', 5))
    # asyncio.run(get_info('"Taylor Swift"', 5))
    
    