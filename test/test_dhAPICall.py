import unittest
from crdclib import crdclib as cl
from crdclib import dhqueries as dh


class TestDHAPICalls(unittest.TestCase):

    def test_dhAPICall(self):
        creds = cl.dhAPICreds('stage')
        result = cl.dhApiQuery(creds['url'], creds['token'], dh.org_query)
        self.assertEqual(list(result.keys()), ['data'])
        self.assertIn('listApprovedStudiesOfMyOrganization', result['data'])


if __name__ == "__main__":
    unittest.main(verbosity=2)
