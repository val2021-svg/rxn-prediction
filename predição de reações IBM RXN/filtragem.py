from rdkit import Chem
from rdkit.Chem import rdqueries

def check_hibridizacao(org1,org2,produto,grau_de_reacao):
  print(org1,'\n',org2,'\n',produto)
  if org1 == produto:
    grau_de_reacao=0
    output=0
  elif org2 == produto:
    grau_de_reacao=0
    output=0
  else:
    (grau_de_reacao,output)=check_til(produto,grau_de_reacao)
  return (grau_de_reacao,output)


def check_til(produto,grau_de_reacao):
  if '~' in produto:
    grau_de_reacao=0
    output=0
  else:
    (grau_de_reacao,output)=count_carb(org1,org2,produto,grau_de_reacao)
  return (grau_de_reacao,output)


def count_carb(org1,org2,produto,grau_de_reacao):
  ncarb_org1=org1.count("C")
  ncarb_aro_org1=org1.count("c")
  ncarb_org2=org2.count("C")
  ncarb_aro_org2=org2.count("c")
  ncarb_tot_in=ncarb_org1+ncarb_aro_org1+ncarb_org2+ncarb_aro_org2
  #print(ncarb_tot_in)
  ncarb_produto=produto.count("C")
  ncarb_aro_produto=produto.count("c")
  ncarb_tot_out=ncarb_produto+ncarb_aro_produto
  #print(ncarb_tot_out)
  if (ncarb_tot_out - ncarb_tot_in) >= 0:
    if (ncarb_tot_out - ncarb_tot_in) == 0:
      grau_de_reacao=1
      (grau_de_reacao,output)=check_aromatization(org1,org2,produto,grau_de_confianca,grau_de_reacao)
    else:
      grau_de_reacao=0
      output=0
  else:
    grau_de_reacao=0
    output=0
  return (grau_de_reacao,output)

def check_aromatization(org1,org2,produto,grau_de_confianca,grau_de_reacao):
  try:
    m = Chem.MolFromSmiles(produto)
    ri = m.GetRingInfo()

    r = False
    for j in range(len(ri.BondRings())):
      r = r or isRingAromatic(m, ri.BondRings()[j])
    if r == True:
      m1 = Chem.MolFromSmiles(org1)
      ri1 = m1.GetRingInfo()
      m2 = Chem.MolFromSmiles(org2)
      ri2 = m2.GetRingInfo()
      r1 = False
      r2 = False
      for k in range(len(ri1.BondRings())):
        r1 = r1 or isRingAromatic(m1, ri1.BondRings()[k])
      for l in range(len(ri2.BondRings())):
        r2 = r2 or isRingAromatic(m2, ri2.BondRings()[l])
      if r1 == True or r2 == True:
        a=0
      else:
        grau_de_reacao=2
    output=(grau_de_confianca)*(grau_de_reacao)
  except Exception as err:
    print(f"  {err}")
    # print("não deu para checar a aromaticidade")
    grau_de_reacao=err
    output=grau_de_reacao
  finally:
      return (grau_de_reacao,output)

def isRingAromatic(mol,bondRing):
  try:
    for id in bondRing:
      if not mol.GetBondWithIdx(id).GetIsAromatic():
        return False
    return True
  except:
    a=0
       
 (grau_de_reacao,output)=check_hibridizacao(org1,org2,produto,grau_de_reacao)
