from flask import jsonify
from . import main
from ..api import proxy_spider


@main.route('/proxyip')
def get_proxyip():
    return jsonify(proxy_spider())
