#!python2
import logging
import os
from datetime import datetime
FORMAT = '%(asctime)-15s %(levelname)s %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)
log = logging

from flask import Flask, render_template, request, jsonify
from bson.objectid import ObjectId

from models.url_model import URLModel
from models.html_model import HTMLModel
from env import MONGO, REDIS

app = Flask('nyl')


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('index.html')


@app.route('/api/url/fetch', methods=['POST'])
def api_url_extract():
    url = request.form['url']
    _doc = MONGO.url_response_cache.find_one({
        'url': url,
    })
    if _doc:
        html = _doc['body']
        oid = str(_doc.pop('_id'))
        log.info('load html from cache')
    else:
        html = URLModel(url).get_html()
        _doc = {
            'url': url,
            'body': html,
            'timestamp': None,
            'datetime': datetime.now().strftime('%Y-%M-%d %H:%M:%S'),
            'status': 1,
        }
        oid = str(MONGO.url_response_cache.insert(_doc))
    data = HTMLModel(html).extract_all()
    return jsonify(**{
        'code': 1,
        'data': data,
        'oid': oid,
    })


@app.route('/api/feedback/url_fetch', methods=['POST'])
def api_feedback_url_fetch():
    oid = request.args.get('oid')
    MONGO.url_response_cache.update({
        '_id': ObjectId(oid),
    }, {
        '$set': {
            'status': -1,
        }
    })
    return jsonify(**{
        'code': 1,
    })


@app.route('/api/markdown/preview', methods=['POST'])
def api_markdown_preview():
    pass


if __name__ == "__main__":
    assert 'NYL_MONGO_URL' in os.environ, 'NYL_** not undefined'
    app.run(host='0.0.0.0', port=9801, debug=True)
