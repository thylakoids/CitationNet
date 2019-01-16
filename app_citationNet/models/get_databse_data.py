import sqlite3
import json

from config import Config
from .get_pubmed_data import get_citation_id, get_summary


def getdata(pmid):
    '''
    '''
    # connect to db, creat new file if file does not exist
    conn = sqlite3.connect(Config.citationNet_databasename)
    cur = conn.cursor()

    # creat table if not exists
    cur.execute(
        'CREATE TABLE IF NOT EXISTS {}\
        (pmid varchar(10),\
        Title varchar(400),\
        FullJournalName varchar(200),\
        Source varchar(200),\
        PubDate varchar(50),\
        Citationin varchar(2000),\
        created timestamp default current_timestamp,\
        primary key(pmid))'
        .format(Config.pubmed_tablename))

    # 1.search the database
    if not cur.execute('select 1 from pubmed where pmid = {}'.format(pmid)).fetchone():
        # 2.search pubmed
        summary = get_summary(pmid)
        if summary is not None:
            Citationin = get_citation_id(pmid)
            # 3.save to database
            try:
                cur.execute(
                    'INSERT INTO {}\
                    (pmid, Title, FullJournalName, Source, PubDate, Citationin)\
                    VALUES (?,?,?,?,?,?)'
                    .format(Config.pubmed_tablename),
                    (pmid,
                     summary['Title'],
                     summary['FullJournalName'],
                     summary['Source'],
                     summary['PubDate'],
                     json.dumps(Citationin)))
            except Exception as e:
                print(e.__str__())
            conn.commit()
    # get data from database
    cur.execute('select Title,Citationin,FullJournalName,Source from pubmed where pmid = {}'.format(pmid))
    result = cur.fetchone()
    Title = result[0]
    Citationin = json.loads(result[1])
    Journal = result[2]
    Source = result[3]
    try:
        cur.execute('select ImpactFactor from impactFactor_2017 where FullJournalTitle ={}'.format(Journal))
        IF = cur.fetchone()[0]
        IF = float(IF)
    except Exception as e:
        IF = 0
    cur.close()
    conn.close()
    return {'title': Title, 'citedpmids': Citationin, 'Journal': Source, 'IF': IF}
