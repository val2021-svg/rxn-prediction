from rdkit import Chem

# To detect aromatic rings, I would loop over the bonds in each ring and
# flag the ring as aromatic if all bonds are aromatic:
def isRingAromatic(mol, bondRing):
  try:
    for id in bondRing:
      if not mol.GetBondWithIdx(id).GetIsAromatic():
        return False
    return True
  except:
    ("não é anel")
    
def check_aromatizacao(smiles):
  m = Chem.MolFromSmiles('O=C1CCC(=O)C2CCCCC12')

  ri = m.GetRingInfo()
  list_r=[]
  # You can interrogate the RingInfo object to tell you the atoms that make up each ring:
  print(ri.AtomRings())

  # or the bonds that make up each ring:
  print(ri.BondRings())
  r = False
  for j in range(len(ri.BondRings())):
    r= r or isRingAromatic(m, ri.BondRings()[j])
    print(r)
    list_r.append(r)
  print(list_r)
  if True in (t == True for t in list_r):
    print("um dos aneis da molecula possui aromaticidade")
  else:
    print("nenhum dos aneis da molecula possui aromaticidade")
