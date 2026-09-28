import unittest
import sys
from collections import Counter
sys.path.append('../')
from src.crdclib import crdclib as cl

class GetTestCDESummaryInfo(unittest.TestCase):
    
    def test_getCDEInfo(self):
        pv_cdeid = '2668478'
        pv_cdever = '1.00'
        nopv_cdeid = 'ABCDEF'
        #nopv_cdeid = '16002823'
        nopv_cdever = '1.00'
        
        pos_result = {'cdename': 'Person Academic Degree Suffix Abbreviation Text', 'cdedef': 'The abbreviation that represents the affix occurring at the end of a name for an award conferred by a college, university, or other postsecondary education institution as official recognition for the successful completion of a program of studies.', 'cdever': '1'}
        neg_result = {'cdename': None, 'cdedef': None, 'cdever': None}
        
        postestinfo = cl.getCDEInfo(cdeid=pv_cdeid, version=pv_cdever)
        self.assertDictEqual(pos_result, postestinfo)
        
        negtestinfo = cl.getCDEInfo(cdeid=nopv_cdeid, version=nopv_cdever)
        self.assertDictEqual(neg_result, negtestinfo)