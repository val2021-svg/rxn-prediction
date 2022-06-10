def canonizacao(smiles):
  from rdkit import Chem
  data=[]
  for i in range(len(smiles)):
    smis=[]
    smis.append(smiles[i])
    print("a forma não canonizada é:",smis)
    try:
      cans = [Chem.MolToSmiles(Chem.MolFromSmiles(smi),True) for smi in smis]
      print("a forma canonizada é:", cans)
      data.append(cans)
    except:
      print("Deu erro ao canonizar", smis)
  print(data)
