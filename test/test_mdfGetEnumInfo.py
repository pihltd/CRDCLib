import unittest
import bento_mdf
import sys
from pathlib import Path
sys.path.append('../')
from src.crdclib import crdclib as cl


class TestMDFGetEnumInfo(unittest.TestCase):
    def test_mdfGetEnumInfo(self):
        
        TESTPATH = Path(__file__).parent
        
        testfiles = [f"{TESTPATH}/data/TEST_SDM-model.yml", f"{TESTPATH}/data/TEST_SDM-model-properties.yml"]
        mdf = bento_mdf.MDF(*testfiles)
        mdf = mdf.model
        
        propname = 'prg_full_description'
        nodename = 'program'
        
        result = cl.mdfGetEnumInfo(mdf=mdf, nodename=nodename, propname=propname)
        
        self.assertEqual(len(result), 1)
        expected = {'study_administration_program_full_description_text': {'handle': 'study_administration_program_full_description_text', 'value': 'Study Administration Program Full Description Text', 'origin_id': '17087562', 'origin_version': '1', 'origin_name': 'EDP'}}
        
        self.assertDictEqual(result[0], expected)
