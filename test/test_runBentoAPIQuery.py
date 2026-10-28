import unittest
#import os
import sys
sys.path.append('../')

from src.crdclib import crdclib as cl
from src.crdclib import dhqueries as dh


class TestBentoAPICalls(unittest.TestCase):
    def test_runBenotAPIQuery(self):
        # Test GC 
        gcquery = """
            {
        programList{
            name
        }
        }
        """
        gcurl = "https://general.datacommons.cancer.gov/v1/graphql/"

        gcres1 = cl.runBentoAPIQuery(url="gc", query=gcquery, variables=None)
        gcres2 = cl.runBentoAPIQuery(url=gcurl, query=gcquery)
        
        self.assertDictEqual(gcres1, gcres2)
        
        # CTDC
        ctdcquery = """
                {
        getAllStudies{
            study_id
        }
        }
        """
        
        
        ctdcurl = "https://clinical.datacommons.cancer.gov/v1/graphql/"
        
        ctdcres1 = cl.runBentoAPIQuery(url="ctdc", query=ctdcquery, variables={})
        ctdcres2 = cl.runBentoAPIQuery(url=ctdcurl, query=ctdcquery, variables={})
        
        self.assertDictEqual(ctdcres1, ctdcres2)
        
        #ICDC
        icdcquery = """
                    {
            program{
                program_name
            }
            }
        """
        
        icdcurl = "https://caninecommons.cancer.gov/v1/graphql/"
        
        icdcres1 = cl.runBentoAPIQuery(url="icdc", query=icdcquery, variables=None)
        icdcres2 = cl.runBentoAPIQuery(url=icdcurl, query=icdcquery)
        
        self.assertDictEqual(icdcres1, icdcres2)
        


