#!python2

from flask import Flask, render_template

app = Flask('nyl')


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('index.html')


@app.route('/api/url/extract')
def api_url_extract():
    pass


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9801, debug=True)
