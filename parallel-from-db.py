import numpy as np
import sys, os
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
from db import mldb
import pickle as pick
from visualize import scaleData
from visualize import pareto
import matplotlib.pyplot as plt
import pandas as pd

plt.rc('text', usetex=True)
plt.rc('font', family='serif') 

root = './databases/'
baseFN = ['ex-1-bounded', 'ex-2-bounded','ex-3-bounded','ex-4-bounded']

for i, fn in enumerate(baseFN):
    nn  = root+fn+'.pk'
    dbr = mldb.mldb()
    dbr.load(nn)
    dvars  = dbr.getXNames()
    onames = dbr.getYNames()
    gens   = dbr.getNumberOfSamples()
    #dbr.printOverview()

    with open(nn, 'rb') as f: 
        dbr = pick.load(f, encoding='latin1')   

    allx  = dbr[gens+1]['allDvarValues'] 
    ally  = dbr[gens+1]['allObjValues'] 
    emitx1  = np.array(ally[:,0])
    emitx2  = np.array(ally[:,1])
    rmss1   = np.array(ally[:,2])
    rmss2   = np.array(ally[:,3])

    (px, py, pd) = pareto(rmss1, emitx1, allx)
    #(prmss2, pemitx2, pdvars) = pareto(rmss2, emitx2, dvars)

    print(np.shape(px), np.shape(py), np.shape(pd))
    pardata = [go.Parcoords(
                line = dict(color = 'blue'),
                dimensions = list([
                    dict(#range = [1.5,10],
                         label = dvars[0], values = pd[:,0]),
                    
                    dict(#range = [-30,0],
                         label = dvars[1], values = pd[:,1]),
                    
                    dict(#range = [200,500],
                         #tickvals = [1.5,3,4.5],
                         label = dvars[2], values = pd[:,2]),

                    dict(#range = [-8,8],
                         #tickvals = [1,2,4,5],
                         label = dvars[3], values = pd[:,3]),
                         #ticktext = ['text 1', 'text 2', 'text 3', 'text 4']),

                    dict(range = [-8,8],
                         label = dvars[4], values = pd[:,4]),
                    
                    dict(range = [-8,8],
                         label = dvars[5], values = pd[:,5]),
                    
                    dict(range = [-8,8],
                         #tickvals = [1.5,3,4.5],
                         label = dvars[6], values = pd[:,6]),

                    dict(range = [-8,8],
                         #tickvals = [1,2,4,5],
                         label = dvars[7], values = pd[:,7]),
                         #ticktext = ['text 1', 'text 2', 'text 3', 'text 4']),

                    
                    dict(#range = [-8.0, 8.0],
                         label = onames[2], values = px),

                    dict(#range = [-8.0,8.0],
                         label = onames[0], values = py),

#                    dict(#range = [-8.0,8.0],
#                         label = onames[2], values = data[:,6]),
#
#                    dict(#range = [-8.0, 8.0],
#                         label = onames[3], values = data[:,7]),
        
                ]))]
    plotly.offline.plot(pardata, filename = fn+'.html')
#for gen in range(0,gens):
#    nsims = dbr.getSampleSize(i=gen)
#    print(nsims) #len(dbr[gen]['dvarValues'])
#    for x in range(0,nsims):
#        #print(x)
#        xsim = dbr.getDVarVec(gen,x)
#        ysim = dbr.getObjVec(gen,x)
#        xvals.append(xsim)
#print(np.shape(xvals))
#
#        #print('Generation #: ', gen)
#        #print('Num of individuals: ', np.size(ns))
#        #print('first check:', np.size(ns), cols)
#        data = np.zeros((np.size(ns), cols))
#        #print("individual: ", np.size(indiv)) 
#        ##print('Total num of gens: ', count)
#        dvars = optjson.getDesignVariables()
#        #print ( "Design variables: ", dvars)
#        #print ( "number of design variables", np.size(dvars))
#        objs = optjson.getObjectives()
#        #print ( "Objectives: ", objs)
#        #print ( "number of objectives", np.size(objs))
#
#        for i, simid in enumerate(ns):
#            #Load add data in 1 generation into data array
#            # The data array is N rows X M columns
#            # N = number of simulations in generation
#            # M = number of davars + objs + 1 (for ID number)
#            #print(i)
#            indiv = optjson.getIndividualWithID(simid)
#            if (-10.0 <= indiv[5] <= 0.0) & (-10.0 <= indiv[6] <= 0.0) & (60 <= indiv[0] <= 75) & (15 <= indiv[1] <= 25) & (400 <= indiv[2] <= 550) & (180 <= indiv[3] <= 280) & (0.001 <= indiv[4] <= 0.004):
#                #print('ok') 
#                goodpoints = goodpoints +1
#            else:
#                #print('good')
#                badpoints = badpoints +1
#            #print(np.shape(data), np.shape(indiv))
#            data[i,:] = indiv
#            #print(indiv)
#    else:                
#        print('Nope', gen)
#    if np.size(ns)< 656:
#        diff = diff+1
#    count = count + np.size(ns)    
#    count2 = count2 + len(data[:,0])
#

#print('less than 656:', diff)
#print('goodpoints', goodpoints)
#print('badpoints', badpoints)

