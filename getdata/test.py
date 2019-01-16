import unittest
from get_pubmed_data import get_summary, get_citation_id
from get_databse_data import getnode


class TestPubmed(unittest.TestCase):
    def test_get_citation_id(self):
        pubmed_ids = get_citation_id('aaa')
        self.assertIsInstance(pubmed_ids, list)

    def test_get_summary(self):
        summary = get_summary(1111)
        self.assertIsInstance(summary, dict)

    def test_getnode(self):
        # 27773806 decode error
        # 28360131
        result = getnode(27773806)
        print(result)
        self.assertIsInstance(result, dict)


if __name__ == '__main__':
    unittest.main()
