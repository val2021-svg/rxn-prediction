import re

#identificar os átomos Ca,Cu,Cl,Co presentes nos SMILES para separar os reagentes dos reactantes.
#reactantes são consideradas as moléculas orgânicas sem esses átomos.

def separacao_reagentes(smiles):
  try:
    if 'c' in smiles:
      print("reactante")
    elif 'C' in smiles:
      if re.search("C(l|u|o|a)",smiles):
        print("reagente")
      else:
        print("reactante")
    else:
      print("reagente")
  except:
    a=0
