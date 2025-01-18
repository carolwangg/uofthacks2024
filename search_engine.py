from textblob import TextBlob
import requests
from bs4 import BeautifulSoup

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