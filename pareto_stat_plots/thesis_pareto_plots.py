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

def calc_xemit(sigmax, sigmapx):
    sigmaxpx = np.sqrt(  (sigmax*sigmapx)2 -    )
    delta = sigmaxpx / (sigmax*sigmapx)
    ex = np.sqrt(   (sigmax**2)*(sigmapx**2) - (sigmax*sigmapx)**2   )
    #print(ex)

plt.rc('text', usetex=True)
plt.rc('font', family='serif') 
plt.rc('axes', labelsize=18)

#baseFN = ['./noquads']#['optLinac_40nC']
#baseFN = ['./noquads/corrected/']
#baseFN = ['./extquads', './noquads']
#baseFN = ['to_q7-9']
fn  = '../phases/quads1-4_newobj/zrms'

allim   = []
allib   = []
allq1   = []
allq2   = [] 
allq3   = []
allq4   = []
allrmss3 = []
allrmsx3 = []
allrmsy3 = []
allrmspx3 = []
allrmspy3 = []
allde3   = [] 
allxemit    = []
ngen  = len(glob.glob(fn+'/results/*.json'))
dsets = load_dataset(fn+'/results/', ftype=FileType.OPTIMIZER)
ds    = dsets[0]

for i in range(1,ngen+1):

    #Loading all data in the i-th generation
    #in array that holds data for every generation
    allrmsx3  = np.append(ds.getData('RMSX3', gen=i), allrmsx3)
    allrmsy3  = np.append(ds.getData('RMSY3', gen=i), allrmsy3)
    allrmss3  = np.append(ds.getData('RMSS3', gen=i), allrmss3)
    allde3    = np.append(ds.getData('DE3', gen=i), allde3)
    allrmspx3 = np.append(ds.getData('RMSPX3', gen=i), allrmspx3)
    allrmspy3 = np.append(ds.getData('RMSPY3', gen=i), allrmspy3)

    allim   = np.append(ds.getData('IM', gen=i), allim)
    allib   = np.append(ds.getData('IBF', gen=i), allib)
    
    allq1  = np.append(ds.getData('KQ1', gen=i), allq1)
    allq2  = np.append(ds.getData('KQ2', gen=i), allq2)
    allq3  = np.append(ds.getData('KQ3', gen=i), allq3)
    allq4  = np.append(ds.getData('KQ4', gen=i), allq4)
    
    #xemit = calc_xemit(ds.getData('RMSX3', gen=i), ds.getData('RMSPX3', gen=i))
    #allxemit = np.append(xemit, allxemit)


#X vs PX pareto
(pfdataxpx, indxpx) = pareto_pts(allrmsx3, allrmspx3)
(pfdataypy, indypy) = pareto_pts(allrmsy3, allrmspy3)
(pfdataxz, indxz) = pareto_pts(allrmss3, allrmsx3)


mmxrms  = np.asarray(pfdatapx['x'])*10**3
mmpxrms = np.asarray(pfdatapx['y'])
mmyrms = np.asarray(pfdatapy['x'])*10**3
mmpyrms = np.asarray(pfdatapy['y'])
mmyrms = np.asarray(allrmsy3[indx])*10**3
mmzrms = np.asarray(pfdataz['x'])*10**3
    
savefile = 'x_vs_px_pareto_front_quads_before_Q5'
#    #plottitle = 'Pareto Front After Kicker and Septum \n $\sigma_{x}$ vs. $\sigma_{px}$'
#    #xtitle = "Energy Spread [MeV]"
#    #xtitle = 'Bunch Length: $\sigma_z$ [mm]'
#    xtitle =  'Momentum: $\sigma_{px}$ [$\gamma$ ]'
#    ytitle =  'Beam Size: $\sigma_{x}$ [mm]'
#
#if y==True:
#    savefile = 'y_vs_py_pareto_front_quads_before_Q5'
#    #plottitle = 'Pareto Front After Quads \n $\sigma_{y}$ vs. $\sigma_{py}$'
#    #xtitle = "Energy Spread [MeV]"
#    #xtitle = 'Bunch Length: $\sigma_z$ [mm]'
#    xtitle =  'Momentum: $\sigma_{py}$ [$\gamma$ ]'
#    ytitle =  'Beam Size: $\sigma_{y}$ [mm]'
#
#if y==True and x==True:
#    savefile = 'xy_vs_pxy_pareto_front_quads_before_Q5'
#    #plottitle = 'Pareto Front After Quads \n $\sigma_{x,y}$ vs. $\sigma_{px}$'
#    #xtitle = "Energy Spread [MeV]"
#    #xtitle = 'Bunch Length: $\sigma_z$ [mm]'
#    xtitle =  r'Momentum: $\sigma_{px}$ [$\gamma$ $\beta$]'
#    ytitle =  'Beam Size: $\sigma_{x,y}$ [mm]'
#
#if bunch==True:
#    savefile = 'dE_vs_zrms_pareto_front_quads_before_Q5'
#    xtitle = 'Bunch Length: $\sigma_s$ [mm]'
#    ytitle = 'Energy Spread: dE [MeV]'
#    plot_stuff(xtitle,ytitle)
#    plt.grid()
#    plt.legend(fontsize=20)
#    plt.savefig(savefile+'.pdf', dpi=1000, bbox_inches='tight')

plt.plot(mmpxrms, mmxrms, '-o', label='$\sigma_{x}$')

#Printing design variables that 
#correspond to pareto front points
print(fn)

print('dE', allde3[indy])
print('yrms', allrmsy3[indy])
print('xrms', allrmsx3[indy])
print('zrms', allrmss3[indy])

print('IM', allim[ind])
print('BF', allib[ind])
print('Q1', allq1[ind])
print('Q2', allq2[ind])
print('Q3', allq3[ind])
print('Q4', allq4[ind])


