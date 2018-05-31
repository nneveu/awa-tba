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

def plot_stuff(title, xname, yname, xyrange=False):
    plt.title(title, size=25)
    plt.xlabel(xname, size=20)
    plt.ylabel(yname, size=20)
    if xyrange:
        plt.axis(xyrange)


plt.rc('text', usetex=True)
plt.rc('font', family='serif') 
plt.rc('axes', labelsize=18)

root = '/home/nicole/Documents/awa-tba/'

#baseFN = ['./noquads']#['optLinac_40nC']
#baseFN = ['./noquads/corrected/']
baseFN = ['./extquads', './noquads']

for fn in baseFN:
    allemx1  = []
    allrmss1 = []
    allrmsx1 = []
    allde1   = [] 

    allemx2  = []
    allrmss2 = []
    allrmsx2 = []

    allde3   = []
    allemx3  = []
    allrmss3 = []
    allrmsx3 = []
   
    allemx4  = []
    allrmss4 = []
    allrmsx4 = []
     
    allq1   = []
    allq2   = [] 
    allq3   = []
    allq4   = []
    allq5   = []
    allq6   = [] 
    allq7   = []
    allq8   = []
    allq9   = []

    allphs  = []
    allfwhm = []
    allim   = []
    allib   = []

    ngen  = len(glob.glob(fn+'/results/*.json'))
    dsets = load_dataset(fn+'/results/', ftype=FileType.OPTIMIZER)
    ds    = dsets[0]

    for i in range(1,ngen+1):
        #Loadig all data in the i-th generation
        de    = ds.getData('DE1', gen=i)
        emx1  = ds.getData('EMITX1', gen=i)
        rmss1 = ds.getData('RMSS1', gen=i)
        rmsx1 = ds.getData('RMSX1', gen=i)
        
        rmss2 = ds.getData('RMSS2', gen=i)
        rmsx2 = ds.getData('RMSX2', gen=i)
        emx2  = ds.getData('EMITX2', gen=i)

        de3    = ds.getData('DE3', gen=i)
        emx3  = ds.getData('EMITX3', gen=i)
        rmss3 = ds.getData('RMSS3', gen=i)
        rmsx3 = ds.getData('RMSX3', gen=i)

        emx4  = ds.getData('EMITX4', gen=i)
        rmss4 = ds.getData('RMSS4', gen=i)
        rmsx4 = ds.getData('RMSX4', gen=i)
        #rmsy4 = ds.getData('RMSY4', gen=i)

        gphs = ds.getData('GPHASE', gen=i)
        fwhm = ds.getData('FWHM', gen=i)
        im = ds.getData('IM', gen=i)
        ib = ds.getData('IBF', gen=i)
        q1 = ds.getData('KQ1', gen=i)
        q2 = ds.getData('KQ2', gen=i)
        q3 = ds.getData('KQ3', gen=i)
        q4 = ds.getData('KQ4', gen=i)
        try:
            q5 = ds.getData('KQ5', gen=i)
            q6 = ds.getData('KQ6', gen=i)
        except:
            pass
        q7 = ds.getData('KQ7', gen=i)
        q8 = ds.getData('KQ8', gen=i)
        q9 = ds.getData('KQ9', gen=i)


        #Some runs don't have q5 and q6
        try:
            q5 = ds.getData('KQ5', gen=i)
            q6 = ds.getData('KQ6', gen=i)
        except:
            pass
            #print('no q5, q6')
       
        try: 
            q7 = ds.getData('KQ7', gen=i)
            q8 = ds.getData('KQ8', gen=i)
            q9 = ds.getData('KQ9', gen=i)
        except:
            pass
            #print('no q7-q9')

        #Saving i-th generation data to an array
        #that holds data for every generation
        allemx1  = np.append(emx1, allemx1)
        allrmss1 = np.append(rmss1, allrmss1)
        allrmsx1 = np.append(rmsx1, allrmsx1)

        allemx2  = np.append(emx2, allemx2)
        allrmss2 = np.append(rmss2, allrmss2)
        allrmsx2 = np.append(rmsx2, allrmsx2)

        #Before structure
        allemx3  = np.append(emx3, allemx3)
        allrmss3 = np.append(rmss3, allrmss3)
        allrmsx3 = np.append(rmsx3, allrmsx3)

        #after structure
        allemx4  = np.append(emx4, allemx4)
        allrmss4 = np.append(rmss4, allrmss4)
        allrmsx4 = np.append(rmsx4, allrmsx4)

        allq1  = np.append(q1, allq1)
        allq2  = np.append(q2, allq2)
        allq3  = np.append(q3, allq3)
        allq4  = np.append(q4, allq4)
        allq5  = np.append(q5, allq5)
        allq6  = np.append(q6, allq6)
        allq7  = np.append(q7, allq7)
        allq8  = np.append(q8, allq8)
        allq9  = np.append(q9, allq9)

        allphs  = np.append(gphs, allphs)
        allfwhm = np.append(fwhm, allfwhm) 
        allim   = np.append(im, allim)
        allib   = np.append(ib, allib)

    #After data for all generations is saved, 
    #Make a pareto front using all data from opt run.
    #(pfdata1, ind1) = pareto_pts(allrmss1, allemx1)
    #(pfdata2, ind2) = pareto_pts(allrmsx2, allemx2)
    #(pfdata2, ind2) = pareto_pts(allrmss2, allrmsx2)
    #plt.plot(pfdata2['x'], pfdata2['y'], '-.')

    (pfdatax3, indx3) = pareto_pts(allrmss3, allrmsx3)
    #plt.plot(pfdata3['x'], pfdata3['y'], '-o')

    #(pfdatay4, indy4) = pareto_pts(allrmss4, allrmsy4)
    (pfdatax4, indx4) = pareto_pts(allrmss4, allrmsx4)
    plot_stuff('Pareto Front after Structure: \n $\sigma_x$ vs. $\sigma_z$', 'Bunch Length: $\sigma_z$ [mm]', 'Beam Size: $\sigma_x$ [mm]')
    label = fn.split('./')[1]
    label = label.split('/')[0]
    mmxrms = np.asarray(pfdatax4['y'])*10**3
    mmzrms = np.asarray(pfdatax4['x'])*10**3
    #plt.plot(pfdatax4['x'], pfdatax4['y'], '-o', label=fn)
    plt.plot(mmzrms, mmxrms, '-o', label=fn)
    #plt.show()

    #print('indx3', indx3)
    #print('indx4', indx4)
    #Printing design variables that 
    #correspond to pareto front points
    print(fn)
    print('xrms', pfdatax4['y'])
    print('zrms', pfdatax4['x'])
    print('GPHASE', allphs[indx4])
    print('FWHM', allfwhm[indx4])
    print('IM', allim[indx4])
    print('BF', allib[indx4])
    print('Q1', allq1[indx4])
    print('Q2', allq2[indx4])
    print('Q3', allq3[indx4])
    print('Q4', allq4[indx4])
    try:
        print('Q5', allq5[indx4])
        print('Q6', allq6[indx4])
    except:
        pass
    print('Q7', allq7[indx4])
    print('Q8', allq8[indx4])
    print('Q9', allq9[indx4])

    #print('xrms1', allrmsx1[ind1])
    #print('xrms2', pfdata4['x'])
    #print('rmss2', pfdata3['x'])
    
    #gens = ds.getLabel(data)
    #ds = dsets[0]
    #plot_parallel_coordinates(dsets[0], 1)
#plt.plot([0,5], [3,3], 'k-')
plt.grid()
plt.legend()
plt.savefig('quads_noquads.pdf', dpi=1000, bbox_inches='tight')
