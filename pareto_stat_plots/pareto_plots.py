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

#baseFN = ['./noquads']#['optLinac_40nC']
#baseFN = ['./noquads/corrected/']
#baseFN = ['./extquads', './noquads']
#baseFN = ['to_q7-9']
z1=True; z2=False; z3=False; z4=False
gun     = True
lphase  = True
quads   = False
doublet = False
triplet = False
baseFN  = ['../phases']
savefile = 'xy_pareto_front_linac_phases_after_quads'
plottitle = 'Pareto Front After Quads \n $\sigma_{x,y}$ vs. $\sigma_z$'
#xtitle = "Energy Spread [MeV]"
xtitle = 'Bunch Length: $\sigma_z$ [mm]'
ytitle =  'Beam Size: $\sigma_{x,y}$ [mm]'
for fn in baseFN:
    
    if gun == True:
        allphs  = []
        allfwhm = []
        allim   = []
        allib   = []
    if quads == True:
        allq1   = []
        allq2   = [] 
        allq3   = []
        allq4   = []
    if lphase == True:
        allp1 = []
        allp2 = []
        allp3 = []
        allp4 = []
        allp5 = []
        allp6 = []
    if doublet == True:
        allq5   = []
        allq6   = []
    if triplet==True:
        allq7   = []
        allq8   = []
        allq9   = []
    if z1 == True:
        allrmss1 = []
        allrmsx1 = []
        allrmsy1 = []
        allrmspx1 = []
        allrmspy1 = []
        allde1   = [] 
    if z2 == True:
        allrmss2 = []
        allrmsx2 = []
        allrmsy2 = []
        allrmspx2 = []
        allrmspy2 = []
        allde2   = [] 

    if z3 ==True:
        allrmss3 = []
        allrmsx3 = []
        allrmsy3 = []
        allrmspx3 = []
        allrmspy3 = []
        allde3   = [] 

    if z4==True:
        allrmss4 = []
        allrmsx4 = []
        allrmsy4 = []
        allrmspx4 = []
        allrmspy4 = []
        allde4   = [] 
 

    ngen  = len(glob.glob(fn+'/results/*.json'))
    dsets = load_dataset(fn+'/results/', ftype=FileType.OPTIMIZER)
    ds    = dsets[0]

    for i in range(1,ngen+1):

        if z1==True:
            #Loadig all data in the i-th generation
            de1   = ds.getData('DE1', gen=i)
            rmss1 = ds.getData('RMSS1', gen=i)
            rmsx1 = ds.getData('RMSX1', gen=i)
            rmsy1 = ds.getData('RMSY1', gen=i)

            #Saving i-th generation data to an array
            #that holds data for every generation
            #allemx1  = np.append(emx1, allemx1)
            allrmss1 = np.append(rmss1, allrmss1)
            allrmsx1 = np.append(rmsx1, allrmsx1)
            allrmsy1 = np.append(rmsy1, allrmsy1)
            allde1 = np.append(de1, allde1)

        if z2==True:
            #Loadig all data in the i-th generation
            de2   = ds.getData('DE2', gen=i)
            rmss2 = ds.getData('RMSS2', gen=i)
            rmsx2 = ds.getData('RMSX2', gen=i)
            rmsy2 = ds.getData('RMSY2', gen=i)

            #Saving i-th generation data to an array
            #that holds data for every generation
            #allemx1  = np.append(emx1, allemx1)
            allrmss2 = np.append(rmss2, allrmss2)
            allrmsx2 = np.append(rmsx2, allrmsx2)
            allrmsy2 = np.append(rmsy2, allrmsy2)
            allde2 = np.append(de2, allde2)


        if z3==True:
            #Loadig all data in the i-th generation
            de3   = ds.getData('DE3', gen=i)
            rmss3 = ds.getData('RMSS3', gen=i)
            rmsx3 = ds.getData('RMSX3', gen=i)
            rmsy3 = ds.getData('RMSY3', gen=i)

            #Saving i-th generation data to an array
            #that holds data for every generation
            #allemx1  = np.append(emx1, allemx1)
            allrmss3 = np.append(rmss3, allrmss3)
            allrmsx3 = np.append(rmsx3, allrmsx3)
            allrmsy3 = np.append(rmsy3, allrmsy3)
            allde3 = np.append(de3, allde3)


        if gun == True:
            #Some runs don't have q5 and q6
            gphs = ds.getData('GPHASE', gen=i)
            fwhm = ds.getData('FWHM', gen=i)
            im = ds.getData('IM', gen=i)
            ib = ds.getData('IBF', gen=i)

            allphs  = np.append(gphs, allphs)
            allfwhm = np.append(fwhm, allfwhm) 
            allim   = np.append(im, allim)
            allib   = np.append(ib, allib)

        if quads==True: 
            q1 = ds.getData('KQ1', gen=i)
            q2 = ds.getData('KQ2', gen=i)
            q3 = ds.getData('KQ3', gen=i)
            q4 = ds.getData('KQ4', gen=i)
            
            allq1  = np.append(q1, allq1)
            allq2  = np.append(q2, allq2)
            allq3  = np.append(q3, allq3)
            allq4  = np.append(q4, allq4)

        if lphase == True:
            p1 = ds.getData('P1', gen=i)
            p2 = ds.getData('P2', gen=i)
            p3 = ds.getData('P3', gen=i)
            p4 = ds.getData('P4', gen=i)
            p5 = ds.getData('P5', gen=i)
            p6 = ds.getData('P6', gen=i)

            allp1 = np.append(p1, allp1)
            allp2 = np.append(p2, allp2)
            allp3 = np.append(p3, allp3)
            allp4 = np.append(p4, allp4)
            allp5 = np.append(p5, allp5)
            allp6 = np.append(p6, allp6)

        if doublet==True:
            q5 = ds.getData('KQ5', gen=i)
            q6 = ds.getData('KQ6', gen=i)


            #q7 = ds.getData('KQ7', gen=i)
            #q8 = ds.getData('KQ8', gen=i)
            #q9 = ds.getData('KQ9', gen=i)


            allq5  = np.append(q5, allq5)
            allq6  = np.append(q6, allq6)
            #allq7  = np.append(q7, allq7)
            #allq8  = np.append(q8, allq8)
            #allq9  = np.append(q9, allq9)



    #After data for all generations is saved, 
    #Make a pareto front using all data from opt run.
    #(pfdata1, ind1) = pareto_pts(allrmss1, allemx1)
    #(pfdata2, ind) = pareto_pts(allrmss2, allrmsx2)
    #(pfdata2, ind) = pareto_pts(allrmss2, allrmsx2)
    (pfdatasx, ind) = pareto_pts(allrmsx1, allrmss1)
    #(pfdatasx, ind) = pareto_pts(allrmss3, allrmsx3)
    #(pfdatase, ind) = pareto_pts(allrmsx1, allde1)
    #(pfdatay4, indy4) = pareto_pts(allrmss4, allrmsy4)
    #(pfdatax4, indx4) = pareto_pts(allrmss4, allrmsx4)

    plot_stuff(plottitle, xtitle,ytitle)
    #label = label.split('/')[0]
    mmyrms = np.asarray(allrmsy1[ind])*10**3

    mmxrms = np.asarray(pfdatasx['x'])*10**3
    mmzrms = np.asarray(pfdatasx['y'])*10**3
    plt.plot(mmzrms, mmyrms, '-o', label='yrms')
    plt.plot(mmzrms, mmxrms, '-o', label='xrms')

    #mmxrms = np.asarray(pfdatase['x'])*10**3
    #de1    = np.asarray(pfdatase['y'])    
    #plt.plot(de1, mmyrms, '-o', label='yrms')
    #plt.plot(de1, mmxrms, '-o', label='xrms')


    #plt.show()

    #print('indx4', indx4)
    #Printing design variables that 
    #correspond to pareto front points
    print(fn)
#    print('px', allrmspx[ind])
#    print('py', allrmspy[ind])



    if z1==True:
      print('dE1', allde1[ind])
      print('yrms1', allrmsy1[ind])
      print('xrms1', allrmsx1[ind])
      print('zrms1', allrmss1[ind], '\n')
 
#      print(pfdatasx['x'])
#      print(pfdatasx['y'])
         
    
    if z3==True:  
        print('dE', allde2[ind])
        print('yrms', allrmsy2[ind])
        print('xrms', allrmsx2[ind])
        print('zrms', allrmss1[ind])

    print('GPHASE', allphs[ind])
    print('P1', allp1[ind]) 
    print('P2', allp2[ind]) 
    print('P3', allp3[ind]) 
    print('P4', allp4[ind]) 
    print('P5', allp5[ind]) 
    print('P6', allp6[ind]) 

    print('FWHM', allfwhm[ind])
    print('IM', allim[ind])
    print('BF', allib[ind])
    try:
        print('Q1', allq1[ind])
        print('Q2', allq2[ind])
        print('Q3', allq3[ind])
        print('Q4', allq4[ind])
    except:
        pass

    try:
        print('Q5', allq5[ind])
        print('Q6', allq6[ind])
    #    print('Q7', allq7[ind])
    #    print('Q8', allq8[ind])
    #    print('Q9', allq9[ind])
    #
    except:
        pass
    #print('xrms1', allrmsx1[ind1])
    #print('xrms2', pfdata4['x'])
    #print('rmss2', pfdata3['x'])
    
    #gens = ds.getLabel(data)
    #ds = dsets[0]
    #plot_parallel_coordinates(dsets[0], 1)
#plt.plot([0,5], [3,3], 'k-')
plt.grid()
plt.legend()
plt.savefig(savefile, dpi=1000, bbox_inches='tight')
