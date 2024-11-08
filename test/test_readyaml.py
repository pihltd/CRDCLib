import unittest
from CRDCStuff import readYAML

class TestReadYaml(unittest.TestCase):
    def test_readyaml(self):
        answer = {'first': ['second', 'third', 'fourth'], 'fifth': {'sixth': 'seventh'}}
        yamltestfile = r"yamltestfile.yml"
        self.assertEqual(readYAML(yamltestfile), answer)
    
if __name__ == "__main__":
    unittest.main(verbosity=2)