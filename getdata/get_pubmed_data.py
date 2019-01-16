from Bio import Entrez
from .Config import Config


def get_citation_id(pmid: str)->list:
    '''
    get pubmed id list which cite this article
    '''
    Entrez.email = Config.email
    links = Entrez.elink(dbfrom='pubmed', id=pmid, linkname='pubmed_pubmed_citedin')
    record = Entrez.read(links)
    try:
        pubmed_ids = [link['Id'] for link in record[0]['LinkSetDb'][0]['Link']]
    except Exception as e:
        print(e.__str__())
        print('wrong pmid: {}'.format(pmid))
        pubmed_ids = []
    return pubmed_ids


def get_summary(pmid: str)->dict:
    '''
    get some useful information for this article
    '''
    try:
        Entrez.email = Config.email
        handle = Entrez.esummary(db="pubmed", id=pmid, retmode="xml")
        records = Entrez.read(handle)[0]
    except Exception as e:
        print(e.__str__())
        print('Wrong pmid: {}'.format(pmid))
        records = None
    # records = Entrez.parse(handle)
    return records
