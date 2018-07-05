from opal.visualization.plots import *
from opal.opal import load_dataset


#myfile = '3gens_large_xrms_at_triplet.stat'
#myfile = '3gens_small_xrms_at_triplet.stat'
#myfile = 'gens3_min_de.stat'
####myfile = 'larger_goodLinac.stat'
#myfile = 'smaller_goodLinac.stat'

# zero was bad.... files= ['optLinac-40nC_GPHASE=0.stat', 'optLinac-40nC_GPHASE=-10.stat', 'optLinac-40nC_GPHASE=-8.stat', 
files = ['csr_fields.stat']

for myfile in files:
    try:
        dsets = load_dataset('../run_opt_params', fname=myfile)#fname='optLinac-40nC.stat')            
        ds = dsets[0]
    except Exception as e:
            print ( e )
    
    pltxy  = plot_profile1D(ds, 's', 'rms_x', xsci=True, ulabel='$\sigma_x$')
    pltxy  = plot_profile1D(ds, 's', 'rms_y', xsci=True, ulabel='$\sigma_y$')
    
    #plt.plot([18.5,18.5], [0,0.015], label='Septum')
    #plt.plot([19.4,19.4], [0,0.015], label='Extra Quads')
    #plt.plot([20.5,20.5], [0,0.015], label='Dipole')
    #plt.plot([21.2,21.2], [0,0.015], label='Triplet')
    #plt.plot([21.8, 21.8], [0,0.015], 'k-')#label='Structure')
    
    z = np.array([ 18.5,   18.7,   20.5,  20.7])
    y = np.array([0.0041, 0.0041, 0.0083,0.0083 ]) 

    #2 inch pipe
    plt.plot([10, 16.5],   [0.0083, 0.0083], 'k-')   #label = '1/6 of 2 inch pipe')
    plt.plot([16.5, 16.5], [0.0083, 0.006], 'k-')
    plt.plot([17.6, 18.5], [0.0041, 0.0041], 'k-')
    plt.plot([18.7, 21.8], [0.0083, 0.0083], 'k-') #label = '1/6 of 2 inch pipe')
    plt.plot([21.8, 21.8], [0.0083, 0.003], 'k-')
    plt.plot([18.7, 18.7], [0.0083, 0.0041], 'k-')
    plt.plot([22.5, 22.5], [0.003, 0.0083], 'k-')
    plt.plot([22.5, 25], [0.0083, 0.0083], 'k-')

    #1 inch pipe
    plt.plot([17.6, 17.6], [0.006, 0.0041], 'k-')#label = '1/6 of 1 inch pipe')
    plt.plot([21.8, 22.5], [0.003, 0.003], 'k-')#label = '1/6 of PETS')
    plt.axis([0,25,0,0.013])

    #Colored elements
    plt.plot([16.5,17.6],[0.006,0.006], 'b-o', label='kicker')
    plt.plot([13.6, 19.4, 21.2], [0.0083, 0.0083,0.0083], 'g^', label='quads')
    plt.plot([21.8, 22.5], [0.003, 0.003], 'yD', label='PETS', markersize=2)
    plt.plot(z,y, 'ko', label = 'bending elements')

    plt.legend(loc='upper left')
    plt.ylabel('$\sigma_{x,y}$')
    plt.grid()
    #plt.show()
    savefile = myfile.split('.stat')[0]
    plt.savefig('xyrms-'+savefile+'.pdf', dpi=1000, bbox_inches='tight')


    fig2 = plt.figure(2)
    pltde = plot_profile1D(ds, 's', 'dE', xsci=True, ulabel='dE [MeV]')
    plt.ylabel('Energy Spread [MeV]')
    plt.axis([0,25,0,1.5])
    plt.grid()
    plt.savefig('dE-'+savefile+'.pdf', dpi=1000, bbox_inches='tight')

    fig3 = plt.figure(3)
    pltde = plot_profile1D(ds, 's', 'rms_s', xsci=True, ulabel='$sigma_z$ [mm]')
    plt.ylabel('Bunch Length, $\sigma_{z}$')
    plt.axis([0,25,0,0.0026])
    plt.grid()
    plt.savefig('zrms-'+savefile+'.pdf', dpi=1000, bbox_inches='tight')

    fig3 = plt.figure(4)
    pltde = plot_profile1D(ds, 's', 'Dx', xsci=True) #, ulabel='$sigma_z$ [mm]')
    plt.ylabel('Dispersion in x') #, $\sigma_{z}$')
    #plt.axis([0,25,0,0.004])
    plt.grid()
    plt.savefig('Dx-'+savefile+'.pdf', dpi=1000, bbox_inches='tight')


    fig3 = plt.figure(5)
    pltde = plot_profile1D(ds, 's', 'emit_x', xsci=True, ulabel='$\epsilon_x$ [mm]')
    pltde = plot_profile1D(ds, 's', 'emit_y', xsci=True, ulabel='$\epsilon_y$ [mm]')
    plt.ylabel('Emittance $\epsilon_{nx,ny}$') #, $\sigma_{z}$')
    plt.axis([0,25,0,0.0007])
    plt.grid()
    plt.savefig('emit-'+savefile+'.pdf', dpi=1000, bbox_inches='tight')



    fig3 = plt.figure(6)
    pltde = plot_profile1D(ds, 's', 'energy', xsci=True)
    plt.ylabel('Energy') #, $\sigma_{z}$')
    #plt.axis([0,25,0,0.0007])
    plt.grid()
    plt.savefig('energy-'+savefile+'.pdf', dpi=1000, bbox_inches='tight')
#plt.title('Bunch Length', size=20)
#plt.ylabel('$\sigma_{z}$', size=20) 
#plt.xlabel('Distance [m]')
#plt = plot_profile1D(ds, 's', 'rms_s', xsci=True, ulabel='dE')
#plt.show()
#plt.savefig('rms_z.pdf', dpi=1000, bbox_inches='tight')
