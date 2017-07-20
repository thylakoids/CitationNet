from __init__ import *
app=Flask(__name__,static_url_path='/static')
#data=getdata()
#data={'nodes':pd.read_excel('nodes1.xlsx'),'edges':pd.read_csv('edges1.csv')}
#nodes_j=frame2json(data['nodes'])
#edges_j=frame2json(data['edges'])
#seednode="[{'id':21685086,'label':216850}]"
@app.route('/')
def root():
	return render_template('index.html',nodes=[],edges='[]')
@app.route('/pubmed/<pmid>')
def getnode(pmid):
	#connect to mysql
	conn = pymysql.connect(user='root')
	cur=conn.cursor()
	#create database
	#cur.execute('CREATE DATABASE IF NOT EXISTS citationMap')
	cur.execute('use citationMap')
	#remove table
	#cur.execute('DROP TABLE IF EXISTS pubmed')
	#create table
	#cur.execute('CREATE TABLE IF NOT EXISTS pubmed(pmid varchar(8),Title text(200),FullJournalName text(50),PubDate 	varchar(20),Citationin text(200),created timestamp default current_timestamp,primary key (pmid))')
	if not cur.execute('select 1 from pubmed where pmid = %s',pmid):
		#if not exist, then search and add to database
		summary=get_summary(pmid)
		Citationin=get_citation_id(pmid)
		try:
			cur.execute('INSERT INTO pubmed(pmid,Title,FullJournalName,PubDate,Citationin) VALUES (%s,%s,%s,%s,%s)',(pmid,summary['Title'],summary['FullJournalName'],summary['PubDate'],json.dumps(Citationin)))
		except Exception,e:
			print e
		conn.commit()
	#get data from database 
	cur.execute('select Title, Citationin from pubmed where pmid = %s',pmid)
	result=cur.fetchone()
	Title=result[0]
	Citationin=json.loads(result[1])
	cur.execute('select FullJournalName from pubmed where pmid = %s',pmid)
	result=cur.fetchone()
	print result
	cur.close()
	conn.close()
	return jsonify({'title':Title,'citedpmids':Citationin})
if __name__=='__main__':
	import logging
    	logging.basicConfig(filename='flask.log',level=logging.DEBUG)
	app.run(debug=False,threaded=True,port=4000,host='0.0.0.0')