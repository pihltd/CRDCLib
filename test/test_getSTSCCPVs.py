import unittest
from crdclib import crdclib as cl

class TestGetCDERecord(unittest.TestCase):
    def test_getSTSCCPVs(self):
        cdeid = '7572817'
        cdeversion = '3.00'
        cdeinfo = getSTSCCPVs(cdeid, cdeversion)
        self.assertEqual(cdeinfo, {})

if __name__ == "__main__":
    unittest.main(verbosity=2)