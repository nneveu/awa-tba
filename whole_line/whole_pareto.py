import glob
import numpy as np
from db import mldb
import matplotlib.pyplot as plt

#Functions from pyOPALTools
#https://gitlab.psi.ch/OPAL/pyOPALTools
from opal.analysis.pareto_fronts import *
from opal import load_dataset
from opal.datasets.filetype import FileType
from opal.visualization.plots import *
from opal.datasets.OptimizerDataset import *

plt.rc('text', usetex=True)
plt.rc('font', family='serif') 

root = '/home/nicole/Documents/awa-tba/'

baseFN = ['optLinac_40nC']

for fn in baseFN:
    allemx1 = []
    allrmss1 = []
    allrmsx1 = []
  
    allemx2 = []
    allrmss2 = []
    allrmsx2 = []
    allq1   = []
    allq2   = [] 
    allq3   = []
    allq4   = []

    ngen  = len(glob.glob(fn+'/results/*.json'))
    dsets = load_dataset(fn+'/results/', ftype=FileType.OPTIMIZER)
    ds    = dsets[0]

    for i in range(1,ngen+1):

        de    = ds.getData('DE1', gen=i)
        emx1  = ds.getData('EMITX1', gen=i)
        emx2  = ds.getData('EMITX2', gen=i)
        rmss1 = ds.getData('RMSS1', gen=i)
        rmss2 = ds.getData('RMSS2', gen=i)
        rmsx1 = ds.getData('RMSX1', gen=i)
        rmsx2 = ds.getData('RMSX2', gen=i)
 
    
        gphs = ds.getData('GPHASE', gen=i)
        fwhm = ds.getData('FWHM', gen=i)
        im = ds.getData('IM', gen=i)
        ib = ds.getData('IBF', gen=i)
        q1 = ds.getData('KQ1', gen=i)
        q2 = ds.getData('KQ2', gen=i)
        q3 = ds.getData('KQ3', gen=i)
        q4 = ds.getData('KQ4', gen=i)

        allemx1  = np.append(emx1, allemx1)
        allrmss1 = np.append(rmss1, allrmss1)
        allrmsx1 = np.append(rmsx1, allrmsx1)

        allemx2  = np.append(emx2, allemx2)
        allrmss2 = np.append(rmss2, allrmss2)
        allrmsx2 = np.append(rmsx2, allrmsx2)

        allq1  = np.append(q1, allq1)
        allq2  = np.append(q2, allq2)
        allq3  = np.append(q3, allq3)
        allq4  = np.append(q4, allq4)
    
    #(pfdata1, ind1) = pareto_pts(allrmss1, allemx1)
    #(pfdata2, ind2) = pareto_pts(allrmsx2, allemx2)

    (pfdata3, ind1) = pareto_pts(allrmss2, allemx2)
    (pfdata4, ind2) = pareto_pts(allrmsx2, allemx2)
    #plt.plot(pfdata2['x'], pfdata2['y'], '-.')
    #plt.show()

    print('Q1', allq1[ind2])
    print('Q2', allq2[ind2])
    print('Q3', allq3[ind2])
    print('Q4', allq4[ind2])
    print('xrms1', allrmsx1[ind1])
    print('xrms2', pfdata4['x'])
    print('rmss2', pfdata3['x'])
    #print(len(data))
    #gens = ds.getLabel(data)
    #print(gens)
    #print(data)
    #ds.design_variables()
    #num = getattr(ds, "num_generations")
    #print(num)
    #ds.getData('objective or design variable', gen=gen)

    #allxy = dsets.get_all_data()
    #print(allxy)
    
    #ds = dsets[0]
    #plot_parallel_coordinates(dsets[0], 1)
    #print(dsets)

