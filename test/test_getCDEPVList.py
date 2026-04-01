import unittest
import sys
from collections import Counter
sys.path.append('../')
from src.crdclib import crdclib as cl


class TestGetCDEPVList(unittest.TestCase):

    def test_getCDEPVList(self):
        pv_cdeid = '2668478'
        pv_cdever = '1.00'
        nopv_cdeid = '16002823'
        nopv_cdever = '1.00'

        pvlist = ['MD', 'DO', 'DMD', 'DED', 'DD', 'DC', 'DBA', 'BT', 'BSW', 'BSL', 'BS', 'BSN', 'BN', 'BFA', 'BEd', 
                  'BEng', 'BE', 'BBA', 'BA', 'AS', 'AE', 'ABA', 'AB', 'AAS', 'AA', 'MSN', 'MSL', 'MS', 'MPH', 'MPA', 
                  'MME', 'MFA', 'MEE', 'MEd', 'ME', 'MDI', 'MCE', 'MA', 'LLM', 'JD', 'EdD', 'DSW', 'ThD', 'ScD', ''
                  'PhE', 'MT', 'MSW', 'AM', 'PharmD', 'OD', 'ND', 'MS', 'MPH', 'MHSA', 'MBA', 'DrPH', 'DPM', 'DDS', 'DVM', 'PhD']

        testlist = cl.getCDEPVList(cdeid=pv_cdeid, version=pv_cdever)
        self.assertEqual(Counter(testlist), Counter(pvlist))

        bumlist = cl.getCDEPVList(cdeid=nopv_cdeid, version=nopv_cdever)
        self.assertIsNone(bumlist)

