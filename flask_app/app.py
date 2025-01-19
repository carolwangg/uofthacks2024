from flask import Flask, jsonify, request, after_this_request
from flask_app.main2 import get_info

app = Flask(__name__)

@app.route('/')
def home():
    return "You can't look here!"
@app.route('/search', methods=['GET'])
def search():
    @after_this_request
    def add_header(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    if not request.args.get('q'):
        return jsonify("no data inputted!!")
    else:
        data = get_info(request.args.get('q'), 6)
        return jsonify(data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)