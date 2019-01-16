from flask import render_template, jsonify
from . import main
from ..models import getdata


@main.route('/')
def root():
    return render_template('index.html', nodes='[]', edges='[]')


@main.route('/pubmed/<pmid>')
def getnode(pmid):
    return jsonify(getdata(pmid))
