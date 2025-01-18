from textblob import TextBlob
import requests
from bs4 import BeautifulSoup

class SearchResult:
    """Represents a single search result."""
    def __init__(self, title, link, content):
        self.title = title
        self.link = link
        self.content = content
        self.sentiment = None

    def analyze_sentiment(self):
        """Analyze sentiment of the content."""
        if self.content:
            self.sentiment = TextBlob(self.content).sentiment.polarity
        else:
            self.sentiment = 0  # Neutral sentiment if no content

class WebScraper:
    """Fetch and parse web pages."""
    def __init__(self, query):
        self.query = query

    def fetch_results(self):
        """Fetch search results using a web scraper."""
        search_url = f"https://www.google.com/search?q={self.query}"
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(search_url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        results = []
        for g in soup.find_all('div', class_='BNeawe vvjwJb AP7Wnd'):
            title = g.get_text()
            link = g.find_parent('a')['href']
            results.append(SearchResult(title, link, None))  # Content will be fetched later
        return results

    def fetch_content(self, search_result):
        """Fetch content for a single search result."""
        try:
            response = requests.get(search_result.link)
            search_result.content = response.text
        except Exception as e:
            search_result.content = None
            print(f"Failed to fetch content: {e}")

class SentimentAnalyzer:
    """Analyze sentiment for a list of search results."""
    @staticmethod
    def analyze_results(results):
        for result in results:
            result.analyze_sentiment()


class SearchEngine:
    """Coordinate the search and ranking process."""
    def __init__(self, query):
        self.query = query
        self.results = []

    def search(self):
        """Perform the search."""
        scraper = WebScraper(self.query)
        self.results = scraper.fetch_results()

        # Fetch content for each result
        for result in self.results:
            scraper.fetch_content(result)

        # Analyze sentiment
        SentimentAnalyzer.analyze_results(self.results)

        # Rank results by sentiment
        self.results.sort(key=lambda x: x.sentiment, reverse=True)

    def get_results(self):
        """Return search results."""
        return [{"title": r.title, "link": r.link, "sentiment": r.sentiment} for r in self.results]
