from flask import Flask, render_template, jsonify
from getdata import getdata, config

app = Flask(__name__, static_url_path='/static')


@app.route('/')
def root():
    return render_template('index.html', nodes='[]', edges='[]')


@app.route('/pubmed/<pmid>')
def getnode(pmid):
    return jsonify(getdata(pmid))


if __name__ == '__main__':
    import logging
    flaskConfig = 'default'
    config = config[flaskConfig]
    logging.basicConfig(filename=config.logfile, level=logging.DEBUG)
    app.run(debug=config.DEBUG, threaded=True, port=4000, host=config.host)
