import numpy as np
from rdkit.Chem import AllChem
from src.utils import TanimotoSimilarity
from src.data_fetch import fetch_smiles

def compute_similarities(mols):
    fps = [AllChem.GetMorganFingerprintAsBitVect(mol, 2, nBits=1024) for mol in mols]
    similarity_matrix = np.zeros((len(fps), len(fps)))

    for i in range(len(fps)):
        for j in range(i + 1, len(fps)):
            similarity_matrix[i][j] = TanimotoSimilarity(fps[i], fps[j])
            similarity_matrix[j][i] = similarity_matrix[i][j]

    return similarity_matrix

if __name__ == "__main__":
    cids = [5280443, 10467, 312822, 2518, 234096, 5281416, 5351506, 86821, 965, 437080, 346340, 866, 857, 22395651, 985, 840, 5250, 5280460, 4819, 312827, 5281, 25203368, 262500, 5250, 327232, 437080, 262500, 312827, 234096, 985, 5281, 522740]
    mols = fetch_smiles(cids)
    similarity_matrix = compute_similarities(mols)
    print("Computed similarity matrix.")
