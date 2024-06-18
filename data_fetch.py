import requests
from rdkit import Chem

def fetch_smiles(cids):
    prolog = "https://pubchem.ncbi.nlm.nih.gov/rest/pug"
    str_cid = ",".join(map(str, cids))
    url = f"{prolog}/compound/cid/{str_cid}/property/isomericsmiles/txt"
    
    response = requests.get(url)
    smiles = response.text.split()
    
    mols = [Chem.MolFromSmiles(smile) for smile in smiles if Chem.MolFromSmiles(smile)]
    return mols

if __name__ == "__main__":
    cids = [5280443, 10467, 312822, 2518, 234096, 5281416, 5351506, 86821, 965, 437080, 346340, 866, 857, 22395651, 985, 840, 5250, 5280460, 4819, 312827, 5281, 25203368, 262500, 5250, 327232, 437080, 262500, 312827, 234096, 985, 5281, 522740]
    mols = fetch_smiles(cids)
    print(f"Fetched {len(mols)} molecules.")
