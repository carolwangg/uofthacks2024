from flask import Flask, render_template, request
from main import SearchEngine, SearchResult, SentimentAnalyzer, WebScraper
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    search_engine = SearchEngine(query)
    search_engine.search()
    results = search_engine.get_results()
    return render_template('results.html', query=query, results=results)

if __name__ == '__main__':
    app.run(debug=True)