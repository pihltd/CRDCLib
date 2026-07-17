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
            srcedges = mdf.edges_by_src(node=mdf.nodes[node])
            for edge in srcedges:
                dstnode = edge.dst.handle
                headers = loadsheet.columns.tolist()
                dstprops = mdf.nodes[dstnode].props
                for prop in dstprops:
                    if mdf.props[dstnode,prop].is_key:
                        self.assertIn(f"{dstnode}.{prop}", headers)




if __name__ == "__main__":
    unittest.main(verbosity=2)