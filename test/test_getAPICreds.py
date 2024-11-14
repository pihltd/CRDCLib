import unittest
import os
from CRDCLib import dhAPICreds

class TestGetCreds(unittest.TestCase):
    def test_getCreds(self):
        check_token = os.getenv('DEV2API')
        check_url = 'https://hub-dev2.datacommons.cancer.gov/api/graphql'
        check_dict = {'url':check_url, 'token':check_token}
        self.assertEqual(dhAPICreds('dev2'), check_dict)

if __name__ == "__main__":
    unittest.main(verbosity=2)