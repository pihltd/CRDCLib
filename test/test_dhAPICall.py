import unittest
import CRDCLib
import DHQueries

class TestDHAPICalls(unittest.TestCase):
    
    def test_dhAPICall(self):
        creds = CRDCLib.dhAPICreds('stage')
        result = CRDCLib.dhApiQuery(creds['url'], creds['token'], DHQueries.org_query)
        self.assertEqual(list(result.keys()), ['data'])
        self.assertIn('listApprovedStudiesOfMyOrganization', result['data'])

if __name__ == "__main__":

    unittest.main(verbosity=2)
