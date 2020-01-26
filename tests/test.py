print("Running tests ...")
# ----------------------------------------
print("\t > Testing single node ...")
from neurolib.models import aln

alnModel = aln.ALNModel()
alnModel.params['sigma_ou'] = 0.1 # add some noise

alnModel.run()

# ----------------------------------------
print("\t > Testing brain network ...")
from neurolib.utils.loadData import Dataset

ds = Dataset("gw")

alnModel = aln.ALNModel(Cmat = ds.Cmat, Dmat = ds.Dmat, simulateBOLD=True)
alnModel.params['duration'] = 0.5*60*1000 # in ms, simulates for 5 minutes

alnModel.run()
# ----------------------------------------
print("All tests passed!")