import unittest
import os
import sys

sys.path.append('../')
from src.crdclib import crdclib as cl

class TestGetCDERecord(unittest.TestCase):

    IN_GITHUB = os.getenv("GITHUB_ACTIONS")
    
    @unittest.skipIf(IN_GITHUB, "Doesn't run in Github")
    def test_getSTSCCPVs(self):
        cdeid = '7572817'
        cdeversion = '3.00'
        cdeinfo = cl.getSTSCCPVs(cdeid, cdeversion)
        self.assertDictEqual(cdeinfo, {'C17998':'Unknown', 'C20197':'Male', 'C16576':'Female'})
        empty_cdeid = '11479876'
        empty_cdeversion = '1.00'
        empty_cdeinfo = cl.getSTSCCPVs(empty_cdeid, empty_cdeversion)
        self.assertIsNone(empty_cdeinfo)

if __name__ == "__main__":
    unittest.main(verbosity=2)