import unittest
import CRDCStuff
import DHQueries

class TestDHAPICalls(unittest.TestCase):
    def test_dhAPICall(self):
        creds = CRDCStuff.dhAPICreds('stage')
        result = CRDCStuff.dhApiQuery(creds['url'],creds['token'], DHQueries.org_query)
        self.assertEqual(list(result.keys()), ['data'])
        self.assertIn('listApprovedStudiesOfMyOrganization', result['data'])

if __name__ == "__main__":
    unittest.main(verbosity=2)