from api import *
import sys
app=Flask(__name__,static_url_path='/static')
#data=getdata()
#data={'nodes':pd.read_excel('nodes1.xlsx'),'edges':pd.read_csv('edges1.csv')}
#nodes_j=frame2json(data['nodes'])
#edges_j=frame2json(data['edges'])
seednode="[{'id':21685086,'label':216850}]"
@app.route('/')
def root():
	return render_template('index.html',nodes=[],edges='[]')
@app.route('/pubmed/<pmid>')
def getnode(pmid):
	title=get_summary(pmid)['Title']
	citedpmids=get_citation_id(pmid)
	return jsonify({'title':title,'citedpmids':citedpmids})
if __name__=='__main__':
	import logging
    	logging.basicConfig(filename='flask.log',level=logging.DEBUG)
	app.run(debug=False,threaded=True,port=4000,host='0.0.0.0')