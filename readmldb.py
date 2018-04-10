import sys, os
import numpy as np
import pickle as pick

sys.path.insert(0, '/lcrc/project/AWA-beam-dynamics/software/pyOPALTools/')
sys.path.insert(0, '/lcrc/project/AWA-beam-dynamics/software/pyOPALTools/db/')
sys.path.insert(0, '/lcrc/project/AWA-beam-dynamics/software/pyOPALTools/utilities/')
from db import mldb

baseFN = './databases/paper-run-1-bounded'#'rand_sample'

#Read database and loop through generations:
dbr       = mldb.mldb()
dbr.load(baseFN+'.pk')
dvars = dbr.getXNames()
ovals = dbr.getYNames()
gens  = dbr.getNumberOfSamples()

dbr.printOverview()

xvals = []
yvals = [] 
for gen in range(0,gens):
    nsims = dbr.getSampleSize(i=gen)
    #print(nsims) #len(dbr[gen]['dvarValues'])
    for x in range(0,nsims):
        #print(x)
        xsim = dbr.getDVarVec(gen,x)
        ysim = dbr.getObjVec(gen,x)
        xvals.append(xsim)
print(dvars, np.shape(xvals))
xvals = np.array(xvals)
for j in range(0, len(dvars)):
        print('Now printing bounds of good points:')
        print("max of "+ dvars[j] + '= '+ str(np.max(xvals[:,j])))
        print("min of "+ dvars[j] + '= '+ str(np.min(xvals[:,j])))
        print('\n')

#Read all data at once:
with open(baseFN+'.pk', 'rb') as f:
    dbr = pick.load(f, encoding='latin1')

allx = dbr[gens+1]['allDvarValues']
ally = dbr[gens+1]['allObjValues']

print(np.shape(allx), np.shape(ally))


#z       = np.zeros([dbr.getSampleSize()])
#numpart = np.zeros([dbr.getSampleSize()])
#
#for i in range(dbr.getSampleSize()):
#    z[i]       = dbr.getObjVec(0,i)[0]
#    numpart[i] = dbr.getObjVec(0,i)[1]
#    if numpart[i] != 1e4:
#        print(numpart[i])
#    if z[i] < 3.15:
#        print(z[i]) 
