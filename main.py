from flask import Flask, render_template, jsonify
from getdata import getdata

app = Flask(__name__, static_url_path='/static')


@app.route('/')
def root():
    return render_template('index.html', nodes='[]', edges='[]')


@app.route('/pubmed/<pmid>')
def getnode(pmid):
    return jsonify(getdata(pmid))


if __name__ == '__main__':
    import logging
    logging.basicConfig(filename='flask.log', level=logging.DEBUG)
    app.run(debug=False, threaded=True, port=4000, host='127.0.0.1')
