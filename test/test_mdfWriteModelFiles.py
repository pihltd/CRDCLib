import unittest
import bento_mdf
from io import StringIO
import sys
import hashlib
from pathlib import Path
sys.path.append('../')
from src.crdclib import crdclib as cl

# https://stackoverflow.com/questions/3942820/how-to-do-unit-testing-of-functions-writing-files-using-pythons-unittest
# https://stackoverflow.com/questions/25651898/variation-in-md5sum-for-stringio-object-vs-saved-file

class TestMDFWriteModelFiles (unittest.TestCase):
    def test_mdfWriteModelFiles(self):
        TESTPATH = Path(__file__).parent
        testfiles = [f"{TESTPATH}/data/crdc_submission.yml", f"{TESTPATH}/data/crdc_submission_properties.yml"]
        mdf = bento_mdf.MDF(*testfiles)
        sections = ['Model']

        cl.mdfWriteModelFiles(mdf=mdf, writedir=f"{TESTPATH}/output/", sectionlist=sections)

        with open(f"{TESTPATH}/output/{mdf.handle}-model.yml", 'rb') as f:
            filedata = f.read()
            newmd5hash = hashlib.md5(filedata).hexdigest()        

        with open(f"{TESTPATH}/data/TEST_crdc_submission.yml", 'rb') as g:
            oldfiledata = g.read()
            oldmd5hash = hashlib.md5(oldfiledata).hexdigest()

        self.assertEqual(newmd5hash, oldmd5hash)

