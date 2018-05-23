import numpy as np
from db import mldb
import matplotlib.pyplot as plt

#Functions from pyOPALTools
#https://gitlab.psi.ch/OPAL/pyOPALTools
from opal.analysis.pareto_fronts import *
plt.rc('text', usetex=True)
plt.rc('font', family='serif') 

root = './databases/'
baseFN = ['ex-1-bounded', 'ex-2-bounded', 'ex-4-bounded'] #'ex-3-bounded',
#baseFN = ['paper-run-ex4']
#dbpath = root+baseFN[0]+'.pk'

#Read db and save data to file
#data = get_all_data_db(dbpath)
#np.save('data.npy', data)

# Load db dict from file
#data = np.load('dict_paper-run-ex4.npy').item()
#(pfdata1, ind1) = pareto_pts(data['RMSS1'], data['EMITX1'])
#(pfdata2, ind2) = pareto_pts(data['RMSS2'], data['EMITX2'])

for fn in baseFN:
    dbpath = root+fn+'.pk'
    #data = get_all_data_db(dbpath)
    #np.save(fn+'.npy', data)
    data = np.load(fn+'.npy').item()

    (pfdata1, ind1) = pareto_pts(data['RMSS1'], data['EMITX1'])
    (pfdata2, ind2) = pareto_pts(data['RMSS2'], data['EMITX2'])

    print(ind1, ind2)
    #print(np.shape(data['KQ1']))
    #print(data['KQ1'][ind1])
    #print(data['KQ1'][ind2])
    
    #plt.plot(pfdata['x'], pfdata['y'], '-.')
    #plt.show()

    for key in data: 
        z1 = data[key][ind1]
        z2 = data[key][ind2]

    


#df = pand.read_csv("https://raw.githubusercontent.com/bcdunbar/datasets/master/parcoords_data.csv")
#layout = go.Layout(font = dict(family='Droid Serif', size=20), 
#                        plot_bgcolor = '#E5E5E5',
#                        paper_bgcolor = '#E5E5E5') #, color='#7f7f7f')
#
#
#l1 = np.arange(1.5, 10.5, 0.5)
#l2 = np.arange(-30, 5, 5)
#l3 = np.arange(200, 550, 50)
#l4 = np.arange(170, 270, 15)
#l5 = np.arange(-8, 9, 2)
#l6 = np.arange(1.0, 1.8, 0.25)
#l7 = np.arange(50, 1450, 50)
#
#alldata = {}
#for i, fn in enumerate(baseFN):
#    nn  = root+fn+'.pk'
#    dbr = mldb.mldb()
#    dbr.load(nn)
#    dvars  = dbr.getXNames()
#    onames = dbr.getYNames()
#    gens   = dbr.getNumberOfSamples()
#    #dbr.printOverview()
#
#    with open(nn, 'rb') as f: 
#        dbr = pick.load(f, encoding='latin1')   
#
#    allx  = dbr[gens+1]['allDvarValues'] 
#    ally  = dbr[gens+1]['allObjValues'] 
#    emitx1  = np.array(ally[:,0])
#    emitx2  = np.array(ally[:,1])
#    rmss1   = np.array(ally[:,2])
#    rmss2   = np.array(ally[:,3])
#
#    (px, py, pd)    = pareto(rmss1, emitx1, allx)
#    (px2, py2, pd2) = pareto(rmss2, emitx2, allx)
#    tosave = {'px':px, 'py':py, 'pd':pd}
#    alldata = np.append(alldata, tosave)
#    print(len(px), len(px2))
#    #print(pd)
#    #plt.plot(px, py)
#    #plt.show()
#    print(np.shape(alldata))#np.shape(px), np.shape(py), np.shape(pd))
#
#    #for i in range(0,7):
#    #    print('min ', np.max(pd[:,i]))
#    #    print('max ', np.min(pd[:,i]))
#    #for i in range(0,8):
#    #    print('min ', np.min(px))
#    #    print('max ', np.max(px))
#    #    print('min ', np.min(py))
#    #    print('max ', np.max(py))
#
#    pardata = [go.Parcoords(
#                    #line = dict(color = [-300, 0, 1, 100, 500]),
#                    #line = dict(color = ['blue', 'green']), 
#                    line = dict(color = [-3000, -700, -1500, -1800, -2700, -3000, -4000],
#                       colorscale = 'Jet',
#                       #showscale = True,
#                       #reversescale = True,
#                       cmin = -4000,
#                       cmax = 0),
#                    #width = 1,
#                    dimensions = list([
#                    
#                    dict(range = [-30,0],
#                        tickvals = l2,
#                         label = dvars[1]+ ' [deg]', values = pd[:,1]),
#                    
#                    dict(range = [200,500],
#                         tickvals = l3, #[1.5,3,4.5],
#                         label = dvars[2]+ ' [A]', values = pd[:,2]),
#    
#                    dict(range = [170,260],
#                         tickvals = l4, #[1,2,4,5],
#                         label = dvars[3]+ ' [A]', values = pd[:,3]),
#                         #ticktext = ['text 1', 'text 2', 'text 3', 'text 4']),
#    
#                    dict(range = [-8,8],
#                         tickvals = l5, 
#                         label = dvars[4]+' [A]', values = pd[:,4]),
#                    
#                    dict(range = [-8,8], tickvals = l5,
#                        label = dvars[5]+' [A]', values = pd[:,5]),
#                    
#                    dict(range = [-8,8],
#                         #tickvals = [1.5,3,4.5],
#                          tickvals = l5,label = dvars[6]+' [A]', values = pd[:,6]),
#    
#                    dict(range = [-8,8],
#                         #tickvals = [1,2,4,5],
#                          tickvals = l5,label = dvars[7]+' [A]', values = pd[:,7]),
#                         #ticktext = ['text 1', 'text 2', 'text 3', 'text 4']),
#    
#                    dict(range = [1.5,10],
#                         tickvals = l1, #[1.5,5.0,10.0],
#                         label = dvars[0]+' [ps]', values = pd[:,0]),
#                   
#                    dict(range = [1.0, 1.75],
#                          tickvals = l6,label = onames[2]+' [mm]', values = px*10**3),
#                        
#                    #dict(range = [1.0,1.75],
#                    #      tickvals = l6, label = onames[2]+ '[mm]', values = px2*10**3),
#    
#                    dict(range = [50.0,1350],
#                         tickvals = l7, label = onames[0]+' [mm-mr]', values = py*10**6),
#                    
#                    #dict(range = [50,1350],
#                    #      tickvals = l7, label = onames[0]+ '[mm-mr]', values = py2*10**6),
#        
#                ]))]
#    fig = go.Figure(data=pardata, layout=layout)
#    offline.plot(fig, filename = fn+'.html')

#def with_jax(fig, filename):
#
#    plot_div = offline.plot(fig, output_type = 'div')
#
#    template = """
#    <head>
#    <script type="text/javascript" async
#      src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-MML-AM_SVG">
#    </script>
#    </head>
#    <body>
#    {plot_div:s}
#    </body>""".format(plot_div = plot_div)
#    with open(filename, 'w') as fp:
#        fp.write(template)
#    #os.startfile(filename)
#    subprocess.call(['xdg-open', filename])
#with_jax(fig, 'cube.html')



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

