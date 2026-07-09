import unittest
import sys

sys.path.append('../')
import src.crdclib.crdclib as cl

class TestGetSTSPVListByProperty(unittest.TestCase):
    
    def test_getSTSPVListByProperty(self):
               
        baseurl = "https://sts.cancer.gov/v2/terms/model-pvs/"
        
        modelhandle = "CDS"
        propertyhandle = 'sex'
        modelversion = '11.0.4'
        
        answer = cl.getSTSPVListByProperty(modelhandle=modelhandle, propertyhandle=propertyhandle)
        self.assertCountEqual(answer, ['Unknown', 'Female', 'Male'])
        
        answer2 = cl.getSTSPVListByProperty(modelhandle=modelhandle, propertyhandle=propertyhandle, modelversion=modelversion)
        self.assertCountEqual(answer2, ['Unknown', 'Female', 'Male'])
        
        answer3 = cl.getSTSPVListByProperty(modelhandle=modelhandle, propertyhandle=propertyhandle, modelversion=modelversion, includeSynonyms=True)
        synonymlist = ['unknown', '? = Unknown', 'Unknown (qualifier value)', 'Not known', 'NOS, unknown', 'Unk', 'Do not know', "Don't know", 'Unknown','Female individual', 'Female structure', 'Female (finding)', 'Female structure (body structure)', 'female', 'Female','M', 'Male']
        keylist = []
        valuelist = []
        for entry in answer3:
            for key, value in entry.items():
                keylist.append(key)
                valuelist = valuelist+value
                
        self.assertCountEqual(keylist, ['Unknown', 'Female', 'Male'])
        self.assertCountEqual(valuelist, synonymlist)
        
        modelhandle = "Garbanzo"
        badanswer = cl.getSTSPVListByProperty(modelhandle=modelhandle, propertyhandle=propertyhandle)
        self.assertEqual(badanswer, {'detail': 'Not found.'})