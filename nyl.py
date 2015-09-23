#!python2
import os

from flask import Flask, render_template, request, jsonify
from models.url_model import URLModel
from models.html_model import HTMLModel

app = Flask('nyl')


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('index.html')


@app.route('/api/url/extract', methods=['POST'])
def api_url_extract():
    url = request.form['url']
    html = URLModel(url).get_html()
    data = HTMLModel(html).extract_all()
    return jsonify(**{
        'code': 1,
        'data': data,
    })


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9801, debug=True)
