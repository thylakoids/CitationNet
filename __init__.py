from Bio import Entrez
from flask import Flask ,render_template,jsonify
import json
import pymysql
Entrez.email = '812033546@qq.com'
def get_citation_id(pmid):
#get pubmed id list which cite this article
	links = Entrez.elink(dbfrom="pubmed", id=pmid, linkname="pubmed_pubmed_citedin")	
	record = Entrez.read(links)
	try:
		pubmed_ids = [link["Id"] for link in record[0]["LinkSetDb"][0]["Link"]]
	except Exception,e:
		print '+++++++++++++++++++++>>empty list!'
		print e
		pubmed_ids=[]
	return pubmed_ids
def frame2json(df):
	d=[
	dict(
		[(colname,row[i] )for i,colname in enumerate(df.columns)]
		) 
	for row in df.values]
	return json.dumps(d)
def get_summary(pmid):
#get some useful information for this article
	handle = Entrez.esummary(db="pubmed", id=pmid, retmode="xml")
	records = Entrez.read(handle)
	#records = Entrez.parse(handle)
	return records[0]
