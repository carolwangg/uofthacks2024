from flask import Flask, render_template, request, jsonify
from main import SearchEngine, SearchResult, SentimentAnalyzer, WebScraper
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    print("Search route hit!")
    query = request.form['query']
    print(f"Search query: {query}")
    search_engine = SearchEngine(query)
    search_engine.search()
    results = search_engine.get_results()
    print("Search Results:", results)
    return jsonify({'results': [vars(res) for res in results], 'query': query})

if __name__ == '__main__':
    app.run(debug=True, port=5001)
