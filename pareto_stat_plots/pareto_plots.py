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

def plot_stuff(xname, yname, xyrange=False):
    #plt.title(title, size=25)
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
z1=False; z2=False; z3=True; z4=False; z5=False;
gun     = True
lphase  = False 
quads   = True 
doublet = False
triplet = False 
baseFN  = ['../phases/quads1-4_newobj/zrms']

x=False
y=False
bunch=True
if x==True:
    savefile = 'x_vs_px_pareto_front_quads_before_Q5'
    #plottitle = 'Pareto Front After Kicker and Septum \n $\sigma_{x}$ vs. $\sigma_{px}$'
    #xtitle = "Energy Spread [MeV]"
    #xtitle = 'Bunch Length: $\sigma_z$ [mm]'
    xtitle =  'Momentum: $\sigma_{px}$ [$\gamma$ ]'
    ytitle =  'Beam Size: $\sigma_{x}$ [mm]'

if y==True:
    savefile = 'y_vs_py_pareto_front_quads_before_Q5'
    #plottitle = 'Pareto Front After Quads \n $\sigma_{y}$ vs. $\sigma_{py}$'
    #xtitle = "Energy Spread [MeV]"
    #xtitle = 'Bunch Length: $\sigma_z$ [mm]'
    xtitle =  'Momentum: $\sigma_{py}$ [$\gamma$ ]'
    ytitle =  'Beam Size: $\sigma_{y}$ [mm]'

if y==True and x==True:
    savefile = 'xy_vs_pxy_pareto_front_quads_before_Q5'
    #plottitle = 'Pareto Front After Quads \n $\sigma_{x,y}$ vs. $\sigma_{px}$'
    #xtitle = "Energy Spread [MeV]"
    #xtitle = 'Bunch Length: $\sigma_z$ [mm]'
    xtitle =  r'Momentum: rms$_{px,py}$ ($\gamma$ $\beta$)'
    ytitle =  'Beam Size: rms$_{x,y}$ (mm)'

if bunch==True:
    savefile = 'dE_vs_zrms_pareto_front_quads_before_Q5_zoomout'
    xtitle = 'Bunch Length: rms$_s$ (mm)'
    ytitle = 'Energy Spread: dE (MeV)'

for fn in baseFN:
    
    if gun == True:
        #allphs  = []
        #allfwhm = []
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

    if z5==True:
        allrmss5 = []
        allrmsx5 = []
        allrmsy5 = []
        allrmspx5 = []
        allrmspy5 = []
        #allde5   = [] 
 

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
            rmspx1 = ds.getData('RMSPX1', gen=i)
            rmspy1 = ds.getData('RMSPY1', gen=i)

            #Saving i-th generation data to an array
            #that holds data for every generation
            #allemx1  = np.append(emx1, allemx1)
            #allrmss1 = np.append(rmss1, allrmss1)
            allrmsx1 = np.append(rmsx1, allrmsx1)
            allrmsy1 = np.append(rmsy1, allrmsy1)
            allrmspx1 = np.append(rmspx1, allrmspx1)
            allrmspy1 = np.append(rmspy1, allrmspy1)
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
            rmspx3 = ds.getData('RMSPX3', gen=i)
            rmspy3 = ds.getData('RMSPY3', gen=i)

            #Saving i-th generation data to an array
            #that holds data for every generation
            allrmsx3 = np.append(rmsx3, allrmsx3)
            allrmsy3 = np.append(rmsy3, allrmsy3)
            allrmss3 = np.append(rmss3, allrmss3)
            allde3 = np.append(de3, allde3)
            allrmspx3 = np.append(rmspx3, allrmspx3)
            allrmspy3 = np.append(rmspy3, allrmspy3)


        if z5==True:
            #Loadig all data in the i-th generation
            rmss5 = ds.getData('RMSS5', gen=i)
            rmsx5 = ds.getData('RMSX5', gen=i)
            rmsy5 = ds.getData('RMSY5', gen=i)

            #Saving i-th generation data to an array
            #that holds data for every generation
            #allemx1  = np.append(emx1, allemx1)
            allrmss5 = np.append(rmss5, allrmss5)
            allrmsx5 = np.append(rmsx5, allrmsx5)
            allrmsy5 = np.append(rmsy5, allrmsy5)


        if gun == True:
            #gphs = ds.getData('GPHASE', gen=i)
            #fwhm = ds.getData('FWHM', gen=i)
            im = ds.getData('IM', gen=i)
            ib = ds.getData('IBF', gen=i)

            #allphs  = np.append(gphs, allphs)
            #allfwhm = np.append(fwhm, allfwhm) 
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
            allq5  = np.append(q5, allq5)
            allq6  = np.append(q6, allq6)

        if triplet==True:
            q7 = ds.getData('KQ7', gen=i)
            q8 = ds.getData('KQ8', gen=i)
            q9 = ds.getData('KQ9', gen=i)
            allq7  = np.append(q7, allq7)
            allq8  = np.append(q8, allq8)
            allq9  = np.append(q9, allq9)



    #After data for all generations is saved, 
    #Make a pareto front using all data from opt run.
    #(pfdata1, ind1) = pareto_pts(allrmss1, allemx1)
    #(pfdata2, ind) = pareto_pts(allrmss2, allrmsx2)
    #(pfdata2, ind) = pareto_pts(allrmss2, allrmsx2)
    #(pfdatasx, ind) = pareto_pts(allrmsx1, allrmss1)
    #(pfdatasx, ind) = pareto_pts(allrmss3, allrmsx3)
    #(pfdatase, ind) = pareto_pts(allrmsx1, allde1)
    #(pfdatay4, indy4) = pareto_pts(allrmss4, allrmsy4)
    #(pfdatasx, ind) = pareto_pts(allrmss5, allrmsx5)

    if x==True:
        (pfdatapx, indx) = pareto_pts(allrmsx3, allrmspx3)
        print('ind', indx)
        mmxrms  = np.asarray(pfdatapx['x'])*10**3
        mmpxrms = np.asarray(pfdatapx['y'])
        plt.plot(mmpxrms, mmxrms, '-o', label='rms$_{x,px}$')

    if y==True:
        (pfdatapy, indy) = pareto_pts(allrmsy3, allrmspy3)
        mmyrms = np.asarray(pfdatapy['x'])*10**3
        mmpyrms = np.asarray(pfdatapy['y'])
        plt.plot(mmpyrms, mmyrms, '-o', label='rms$_{y,py}$')
        plt.legend()
#    if x==True and y==True:
#        mmyrms = np.asarray(allrmsy1[ind])*10**3
#        plt.plot(mmpxrms, mmxrms, '-o', label='xrms')
#        plt.plot(mmpxrms, mmyrms, '-o', label='yrms')


    if bunch==True:
        (pfdataz, ind) = pareto_pts(allrmss3, allde3)
        mmzrms = np.asarray(pfdataz['x'])*10**3
        #plt.axis([1.38,1.5,0.45,0.75])
        plt.plot(mmzrms, pfdataz['y'], '-o')
    
    plot_stuff(xtitle,ytitle)
    plt.grid()
    plt.savefig(savefile+'.pdf', dpi=1000, bbox_inches='tight')


    #Printing design variables that 
    #correspond to pareto front points
    print(fn)

    if z1==True:
        print('dE1', allde1[ind])
        print('yrms1', allrmsy1[ind])
        #print('xrms1', allrmsx1[ind])
        #print('zrms1', allrmss1[ind], '\n')
 
    
    if z3==True:  
        print('dE', allde3[ind])
        print('yrms', allrmsy3[ind])
        print('xrms', allrmsx3[ind])
        print('zrms', allrmss3[ind])

    ##print('GPHASE', allphs[ind])
    #print('P1', allp1[ind]) 
    #print('P2', allp2[ind]) 
    #print('P3', allp3[ind]) 
    #print('P4', allp4[ind]) 
    #print('P5', allp5[ind]) 
    #print('P6', allp6[ind]) 

    if gun==True:
        #print('FWHM', allfwhm[ind])
        #print('testIM', allim[211])
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
        #print('Q5', allq5[ind])
        #print('Q6', allq6[ind])
        print('Q7', allq7[ind])
        print('Q8', allq8[ind])
        print('Q9', allq9[ind])
    #
    except:
        pass
    

