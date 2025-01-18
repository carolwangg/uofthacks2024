from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/search', methods=['GET'])
def search():
    if not request.args['q']:
        return jsonify({"error":"please input a query!", "data": ""})
    else:
        return jsonify({"error":"", "data": request.args['q']})

if __name__ == "__main__":
    app.run(debug=True)