import sys, os
import numpy as np
import pickle as pick
import matplotlib.pyplot as plt
from db import mldb

def doscale(vals):
    smax = np.max(vals)
    smin = np.min(vals)
    scaled_vals = (vals - smin)/smax
    return (scaled_vals)    

def pareto(x, y):
    #Making holders for my pareto fronts            
    pareto_y = []
    pareto_x = [] 
    pdvars   = [] 
    w  = np.arange(0,1.001, 0.001)
    sx = doscale(x)
    sy = doscale(y)
    #Finding best point with respect to all weights (w)
    for i in range(0, len(w)):
        fobj     = sy * w[i] + sx *(1-w[i])
        wmins    = np.where(fobj==min(fobj))[0][0]
        pareto_y = np.append(pareto_y, y[wmins])
        pareto_x = np.append(pareto_x, x[wmins])
        pdvars   = np.append(pdvars, dvars[wmins, :])
    return(pareto_x, pareto_y)#, pdvars)

#def getx(pareto, allx, ally):
#    return(xvals)
    

root = './databases/'
baseFN = ['ex-1-bounded', 'ex-2-bounded','ex-3-bounded','ex-4-bounded']
style  = ['k--', 'y.-', 'b-.','m.-'] 
alpha  = [1.0, 0.7, 0.7, 0.7]
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

for i, fn in enumerate(baseFN):   
    nn = root+fn+'.pk' 
    #Read database and loop through generations:
    dbr       = mldb.mldb()
    dbr.load(nn)
    #dvars = dbr.getXNames()
    ovals = dbr.getYNames()
    print(ovals)
    gens  = dbr.getNumberOfSamples()
    #Read all data at once:
    with open(nn, 'rb') as f:
        dbr = pick.load(f, encoding='latin1')

    allx = dbr[gens+1]['allDvarValues']
    ally = dbr[gens+1]['allObjValues']
    print(np.shape(allx), np.shape(ally))
    emitx1  = np.array(ally[:,0])
    emitx2  = np.array(ally[:,1])
    rmss1   = np.array(ally[:,2])
    rmss2   = np.array(ally[:,3])

    #emittance vs rmss
    dvars = np.array(allx)
    (prmss1, pemitx1) = pareto(rmss1, emitx1)
    (prmss2, pemitx2) = pareto(rmss2, emitx2)
    
    print(np.shape(prmss1)) #, np.shape(pdvars1))
    ex = fn.split('-')[1]
    #Plotting
    plot =1 
    if plot == 0:
        plt.plot(prmss1*10**3, pemitx1*10**6, style[i], alpha=alpha[i], label='ex-'+ex)
    else:
        plt.plot(prmss2*10**3, pemitx2*10**6, style[i], label='ex-'+ex)

plt.xlabel('Bunch Length [mm]', size=14)
plt.ylabel('Emittance [$\mu$m]', size=14)
#title = 'Pareto Front and Random Samples'
#plt.axis([0.9, 2.0, 0, 300])
#plt.set_major_formatter(mtick.FormatStrFormatter('%.1f'))
#plt.title(title, size=16)
plt.xticks(fontsize = 12)
plt.yticks(fontsize = 12)
plt.grid(True)
plt.legend(loc='upper right', numpoints=1)
if plot ==0: 
    plt.savefig('ex-pareto1.pdf',bbox_inches='tight',dpi=900)
else:
    plt.savefig('ex-pareto2.pdf',bbox_inches='tight',dpi=900)

