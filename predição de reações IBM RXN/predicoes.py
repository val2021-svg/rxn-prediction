import time
import json
import openpyxl

def reaction(org1,org2,inorg,agua):
  soma=org1+'.'+org2+'.'+inorg+'.'+agua
  print(soma)
  try:
    response = rxn4chemistry_wrapper.predict_reaction(soma)
    #print(json.dumps(response, indent=2))
    time.sleep(10)
    results = rxn4chemistry_wrapper.get_predict_reaction_results(
      response['prediction_id']
    )
    smiles_result = results['response']['payload']['attempts'][0]['smiles']
    print(smiles_result)
    smiles_confidence = results['response']['payload']['attempts'][0]['confidence']
    print(smiles_confidence)
  except:                                                                                                                                                                                                                                                                        
    print("A reação",soma,"deu erro!")
  finally:
    return

  reaction(org1,org2,inorg,agua)
  time.sleep(20)
