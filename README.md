# rxn-prediction
## Introduction
This is the repository with the software codes developed and the data obtained in our research group on chemical reaction prediction by Machine Learning.

## Technologies
The project is created with:
* Python version: 3.7.7
* Pytorch version: 1.11.0/1.6.0
* Torchtext version: 0.3.1
* Six
* Tqdm
* Future

## Launch
### SMILE molecules processing
For the processing of SMILES molecules, we have developed modules to check canonization, aromatization and separation of reagents and reactants using the RDKit tool.

Before running the codes it is necessary to download the RDKit package:

```
!pip install rdkit-pypi -qqq
import datetime
import pandas as pd
from rdkit import Chem
from rdkit.Chem import AllChem, Draw
```

### Reaction predictions with IBM RXN
For IBM RXN reaction prediction, you must first install the wrapper below to access the API:

```
pip install rxn4chemistry
```
To start using the API, it is necessary to create a project or set an existing one from the api key of each user's on the IBM platform.
```
from rxn4chemistry import RXN4ChemistryWrapper

rxn4chemistry_wrapper = RXN4ChemistryWrapper(api_key=api_key)
# NOTE: you can create a project or set an esiting one using:
# rxn4chemistry_wrapper.set_project('PROJECT_ID')

#print(rxn4chemistry_wrapper.list_all_projects())
rxn4chemistry_wrapper.list_all_attempts_in_project()
rxn4chemistry_wrapper.set_project(project_id)
#print(rxn4chemistry_wrapper.project_id)
```

### Reaction predictions with Molecular Transformer
