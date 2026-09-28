import unittest
import bento_mdf
import sys
from pathlib import Path
sys.path.append('../')
from src.crdclib import crdclib as cl


class TestMDFGetTermInfo(unittest.TestCase):
    def test_mdfGetTermInfo(self):
        
        TESTPATH = Path(__file__).parent
        
        testfiles = [f"{TESTPATH}/data/TEST_SDM-model.yml", f"{TESTPATH}/data/TEST_SDM-model-properties.yml"]
        mdf = bento_mdf.MDF(*testfiles)
        mdf = mdf.model
        
        propname = 'prg_full_description'
        nodename = 'program'
        
        result = cl.mdfGetTermInfo(mdf=mdf, nodename=nodename, propname=propname)
        
        print(result)
        
        self.assertEqual(len(result), 1)
        expected = {('study_administration_program_full_description_text', 'caDSR', 17087562, '1'): {'handle': 'study_administration_program_full_description_text', 'value': 'Study Administration Program Full Description Text', 'origin_id': '17087562', 'origin_version': '1', 'origin_name': 'caDSR'}}
        
        self.assertDictEqual(result[0], expected)
