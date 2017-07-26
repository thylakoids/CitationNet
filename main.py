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
	#connect to mysql,utf-8
	conn = pymysql.connect(user='root',charset='utf8')
	cur=conn.cursor()
	#create database
	#cur.execute('CREATE DATABASE IF NOT EXISTS citationMap')
	cur.execute('use citationMap')
	#remove table
	#cur.execute('DROP TABLE IF EXISTS pubmed')
	#create table
	#cur.execute('CREATE TABLE IF NOT EXISTS pubmed(pmid varchar(10),Title varchar(400),FullJournalName varchar(200),Source varchar(200),PubDate varchar(50),Citationin varchar(2000),created timestamp default current_timestamp,primary key (pmid))')
	if not cur.execute('select 1 from pubmed where pmid = %s',pmid):
		#if not exist, then search and add to database
		summary=get_summary(pmid)
		Citationin=get_citation_id(pmid)
		try:
			cur.execute('INSERT INTO pubmed(pmid,Title,FullJournalName,Source,PubDate,Citationin) VALUES (%s,%s,%s,%s,%s,%s)',(pmid,summary['Title'],summary['FullJournalName'],summary['Source'],summary['PubDate'],json.dumps(Citationin)))
		except Exception,e:
			print e
		conn.commit()
	#get data from database 
	cur.execute('select Title, Citationin, FullJournalName,Source from pubmed where pmid = %s',pmid)
	result=cur.fetchone()
	Title=result[0]
	#27773806 decode error
	#28360131
	#27609891 science
	Citationin=json.loads(result[1])
	Journal=result[2]
	Source=result[3]
	if cur.execute('select ImpactFactor from impactFactor_2017 where FullJournalTitle =%s ',Journal):
		IF=cur.fetchone()[0]
	elif cur.execute('select ImpactFactor from impactFactor_2017 where FullJournalTitle =%s ',Source):
		IF=cur.fetchone()[0]
	else:
		IF='0'
	try:
		IF=float(IF)
	except Exception,e:
		IF=0
	cur.close()
	conn.close()
	return jsonify({'title':Title,'citedpmids':Citationin,'Journal':Source,'IF':IF})
if __name__=='__main__':
	import logging
    	logging.basicConfig(filename='flask.log',level=logging.DEBUG)
	app.run(debug=True,threaded=True,port=4000,host='127.0.0.1')