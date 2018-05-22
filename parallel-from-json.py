import numpy as np
import sys
#import json
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import OptPilotJsonReader as optreader

#import matplotlib
#matplotlib.use("Agg")
#import matplotlib.pyplot as plt
#import matplotlib.animation as manimation

#def parallelPlot(jsondir, )

#ex1   = "/home/nicole/Documents/surrogatemodels/ga-model/results/"
#ex1    = "./ex-1/results/"
paper-run = 'paper-run-1.pk'

nobj  = 4
ndvar = 8
#cols  = nobj + ndvar + 1 #extra 1 for ID number

# 1. Find all .json files of a directory, e.g. "./"
optjson = optreader.OptPilotJsonReader(ex1)
n = optjson.getNumOfGenerations()
#print(n)
diff       = 0
count      = 0
count2     = 0
badpoints  = 0
goodpoints = 0

test     = np.zeros((1,13))
for gen in range(1,n+1):
#if True:
#    gen = n 
    if True:
        optjson.readGeneration(gen)
        #print(dir(optjson))
        dvarsall = optjson.getAllInput()
        objsall  = optjson.getAllOutput()

        ns = optjson.getIDs()
        #print(np.size(ns))
        #print('Generation #: ', gen)
        #print('Num of individuals: ', np.size(ns))
        #print('first check:', np.size(ns), cols)
        data = np.zeros((np.size(ns), cols))
        #print("individual: ", np.size(indiv)) 
        ##print('Total num of gens: ', count)
        dvars = optjson.getDesignVariables()
        #print ( "Design variables: ", dvars)
        #print ( "number of design variables", np.size(dvars))
        objs = optjson.getObjectives()
        #print ( "Objectives: ", objs)
        #print ( "number of objectives", np.size(objs))

        print('reader:', np.shape(dvarsall), np.shape(objsall))
        for i, simid in enumerate(ns):
            #Load add data in 1 generation into data array
            # The data array is N rows X M columns
            # N = number of simulations in generation
            # M = number of davars + objs + 1 (for ID number)
            #print(i)
            indiv = optjson.getIndividualWithID(simid)
            if (-10.0 <= indiv[5] <= 0.0) & (-10.0 <= indiv[6] <= 0.0) & (60 <= indiv[0] <= 75) & (15 <= indiv[1] <= 25) & (400 <= indiv[2] <= 550) & (180 <= indiv[3] <= 280) & (0.001 <= indiv[4] <= 0.004):
                #print('ok') 
                goodpoints = goodpoints +1
            else:
                #print('good')
                badpoints = badpoints +1
            #print(np.shape(data), np.shape(indiv))
            data[i,:] = indiv
            #print(indiv)
    else:                
        print('Nope', gen)
    if np.size(ns)< 656:
        diff = diff+1
    count = count + np.size(ns)    
    count2 = count2 + len(data[:,0])

pardata = [go.Parcoords(
                line = dict(color = 'blue'),
                dimensions = list([
                    dict(#range = [1.5,10],
                         label = dvars[0], values = data[:,0]),
                    
                    dict(#range = [-30,0],
                         label = dvars[1], values = data[:,1]),
                    
                    dict(#range = [200,500],
                         #tickvals = [1.5,3,4.5],
                         label = dvars[2], values = data[:,2]),

                    dict(#range = [170,260],
                         #tickvals = [1,2,4,5],
                         label = dvars[3], values = data[:,3]),
                         #ticktext = ['text 1', 'text 2', 'text 3', 'text 4']),

                    
                    dict(#range = [-8.0, 8.0],
                         label = dvars[4], values = data[:,4]),

                    dict(#range = [-8.0,8.0],
                         label = dvars[5], values = data[:,5]),

                    dict(#range = [-8.0,8.0],
                         label = dvars[6], values = data[:,6]),

                    dict(#range = [-8.0, 8.0],
                         label = objs[0], values = data[:,7]),
        
                ]))]

#print(np.shape(data))
bounds = optjson.getBounds()
#print(bounds)
print(count, count2)
print('less than 656:', diff)
print('goodpoints', goodpoints)
print('badpoints', badpoints)
#plotly.offline.plot(pardata, filename = 'parcoord-dimensions.html')
    #test = np.append(test, data, axis=0)
#print(np.shape(test), np.size(ns))
## 4a. Get only bounds of a specific design variable
#bound = optjson.getBounds(dvars[2])
#lower = bound[0]
#upper = bound[1]
#    
#print ( "dvar: " + dvars[1] + "\n"
#        " lower bound: " + str(lower) + "\n"
#        " upper bound: " + str(upper))
#
#optjson.readGeneration(1)
## 7. Get an individual
##indiv = optjson.getIndividual(1)
##print ('All data:\n',indiv )
#

