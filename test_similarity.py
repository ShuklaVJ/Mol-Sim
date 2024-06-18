import unittest
from rdkit import Chem
from rdkit.Chem import AllChem
from src.utils import TanimotoSimilarity

class TestTanimotoSimilarity(unittest.TestCase):

    def test_tanimoto_similarity(self):
        mol1 = Chem.MolFromSmiles('CCO')
        mol2 = Chem.MolFromSmiles('CCN')
        fp1 = AllChem.GetMorganFingerprintAsBitVect(mol1, 2, nBits=1024)
        fp2 = AllChem.GetMorganFingerprintAsBitVect(mol2, 2, nBits=1024)

        similarity = TanimotoSimilarity(fp1, fp2)
        self.assertGreaterEqual(similarity, 0)
        self.assertLessEqual(similarity, 1)

if __name__ == "__main__":
    unittest.main()
