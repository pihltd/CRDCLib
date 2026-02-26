import unittest
import bento_mdf
import sys
from collections import Counter
sys.path.append('../')
from src.crdclib import crdclib as cl

class TestAnnotateMDFTerms(unittest.TestCase):

    def test_mdfBuildLoadsheets(self):
        #Using the GC/CDS Model for testing
        mdffiles = ['https://raw.githubusercontent.com/CBIIT/cds-model/refs/heads/11.0.3/model-desc/cds-model.yml','https://raw.githubusercontent.com/CBIIT/cds-model/refs/heads/11.0.3/model-desc/cds-model-props.yml']
        mdf = bento_mdf.MDF(*mdffiles)
        mdf = mdf.model

        loadsheets = cl.mdfBuildLoadSheets(mdf)

        #Check that nodes match
        startnodes = list(mdf.nodes)
        sheetnodes = list(loadsheets.keys())
        
        self.assertEqual(Counter(startnodes), Counter(sheetnodes))

        # Test that the properties are in the model
        for node, loadsheet in loadsheets.items():
            sourceprops = list(mdf.nodes[node].props)
            sheetprops = loadsheet.columns.tolist()
            for sheetprop in sheetprops:
                if "." not in sheetprop:
                    self.assertIn(sheetprop, sourceprops)

        # Edges in the loadsheet are expressed as node.property.  Check that they exist
        for node, loadsheet in loadsheets.items():
            sheetprops = loadsheet.columns.tolist()
            #print(f"Node: {node}\nProps: {sheetprops}")
            for sheetprop in sheetprops:
                if "." in sheetprop:
                    temp = sheetprop.split(".")
                    tempnode = temp[0]
                    tempprop = temp[1]
                    testsheet = loadsheets[tempnode]
                    testprops = testsheet.columns.tolist()
                    #print(f"Source node: {tempnode}\t dervied from {sheetprop}\n Testprops: {testprops}")
                    self.assertIn(tempprop, testprops)






if __name__ == "__main__":
    unittest.main(verbosity=2)