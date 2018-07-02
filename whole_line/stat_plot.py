from opal.visualization.plots import *
from opal.opal import load_dataset


#myfile = '3gens_large_xrms_at_triplet.stat'
myfile = '3gens_small_xrms_at_triplet.stat'
#myfile = 'gens3_min_de.stat'
#myfile = 'larger_goodLinac.stat'
myfile = 'smaller_goodLinac.stat'

try:
    dsets = load_dataset('../half_run', fname=myfile)#fname='optLinac-40nC.stat')            
    ds = dsets[0]
except Exception as e:
        print ( e )

#plt = plot_profile1D(ds, 's', 'rms_x', xsci=True, ulabel='$\sigma_x$')
#plt = plot_profile1D(ds, 's', 'rms_y', xsci=True, ulabel='$\sigma_y$')
#
#
##plt.plot([18.5,18.5], [0,0.015], label='Septum')
##plt.plot([19.4,19.4], [0,0.015], label='Extra Quads')
##plt.plot([20.5,20.5], [0,0.015], label='Dipole')
##plt.plot([21.2,21.2], [0,0.015], label='Triplet')
##plt.plot([21.8, 21.8], [0,0.015], 'k-')#label='Structure')
#
#z = np.array([16.5,  17.5,  18.5,   18.7,   20.5,  20.7])
#y = np.array([0.006, 0.006, 0.0041, 0.0041, 0.0083,0.0083 ])
#
#plt.plot([19.4, 21.2], [0.0083,0.0083], 'g^', label='quads')
#plt.plot([21.8, 22.5], [0.003, 0.003], 'yD', label='PETS')
#plt.plot(z,y, 'ko', label = 'bending elements')
#plt.plot([0, 25], [0.0083, 0.0083], 'k-')#label = '1/6 of 2 inch pipe')
#plt.plot([0, 25], [0.0041, 0.0041], 'k-')#label = '1/6 of 1 inch pipe')
#plt.plot([0, 25], [0.003, 0.003], 'k-')#label = '1/6 of PETS')
#plt.legend(loc='upper left')
#plt.ylabel('$\sigma_{x,y}$')
#plt.grid()
##plt.show()
#savefile = myfile.split('.')[0]
#plt.savefig(savefile+'.pdf', dpi=1000, bbox_inches='tight')

plt.title('Bunch Length', size=20)
plt.ylabel('$\sigma_{z}$', size=20) 
plt.xlabel('Distance [m]')
plt = plot_profile1D(ds, 's', 'rms_s', xsci=True, ulabel='dE')
#plt.show()
plt.savefig('rms_z.pdf', dpi=1000, bbox_inches='tight')
