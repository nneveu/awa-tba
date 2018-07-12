from opal.visualization.plots import *
from opal.opal import load_dataset


#myfile = '3gens_large_xrms_at_triplet.stat'
#myfile = '3gens_small_xrms_at_triplet.stat'
#myfile = 'gens3_min_de.stat'
####myfile = 'larger_goodLinac.stat'
#myfile = 'smaller_goodLinac.stat'

zstop= 20 

# zero was bad.... files= ['optLinac-40nC_GPHASE=0.stat', 'optLinac-40nC_GPHASE=-10.stat', 'optLinac-40nC_GPHASE=-8.stat', 
files = ['zrms_newobj.stat'] #'optLinac-40nC_KQ3=3.2_IM=250.stat']

for myfile in files:
    try:
        dsets = load_dataset('../run_opt_params', fname=myfile)#fname='optLinac-40nC.stat')            
        ds = dsets[0]
    except Exception as e:
            print ( e )
    
    pltxy  = plot_profile1D(ds, 's', 'rms_x', xsci=True, label='$\sigma_x$')
    pltxy  = plot_profile1D(ds, 's', 'rms_y', xsci=True, label='$\sigma_y$')
    
    z = np.array([ 18.5,   18.7,   20.5,  20.7])
    y = np.array([0.0041, 0.0041, 0.0083,0.0083 ]) 

#    #2 inch pipe
#    plt.plot([10, 16.5],   [0.0083, 0.0083], 'k-', label = '1/6 of 2 inch pipe')
#    plt.plot([16.5, 16.5], [0.0083, 0.006], 'k-')
#    plt.plot([17.6, 18.5], [0.0041, 0.0041], 'k-')
#    plt.plot([18.7, 21.8], [0.0083, 0.0083], 'k-') #label = '1/6 of 2 inch pipe')
#    plt.plot([21.8, 21.8], [0.0083, 0.003], 'k-')
#    plt.plot([18.7, 18.7], [0.0083, 0.0041], 'k-')
#    plt.plot([22.5, 22.5], [0.003, 0.0083], 'k-')
#    plt.plot([22.5, 25], [0.0083, 0.0083], 'k-')

#    #1 inch pipe
#    plt.plot([17.6, 17.6], [0.006, 0.0041], 'k-')#label = '1/6 of 1 inch pipe')
#    plt.plot([21.8, 22.5], [0.003, 0.003], 'k-')#label = '1/6 of PETS')

#    #Colored elements
#    plt.plot([16.5,17.6],[0.006,0.006], 'b-o', label='kicker')
#    plt.plot([13.6, 19.4, 21.2], [0.0083, 0.0083,0.0083], 'g^', label='quads')
#    plt.plot([21.8, 22.5], [0.003, 0.003], 'yD', label='PETS', markersize=2)
#    plt.plot(z,y, 'ko', label = 'bending elements')

    plt.plot([19.4,19.4],[0,0.015], '-g', label='$s_3$')
    plt.axis([0,zstop,0,0.015])
    plt.legend(loc='lower left')
    plt.ylabel('Beam sizes: $\sigma_{x,y}$', size=20)
    plt.grid()
    #plt.show()
    savefile = myfile.split('.stat')[0]
    plt.savefig('xyrms-'+savefile+'.pdf', dpi=1000, bbox_inches='tight')


    fig2 = plt.figure(2)
    pltde = plot_profile1D(ds, 's', 'dE', xsci=True, label='dE [MeV]')
    plt.ylabel('Energy Spread [MeV]')
    plt.axis([0,zstop,0,1.5])
    plt.grid()
    plt.savefig('dE-'+savefile+'.pdf', dpi=1000, bbox_inches='tight')

    fig3 = plt.figure(3)
    pltde = plot_profile1D(ds, 's', 'rms_s', xsci=True, label='$sigma_z$ [mm]')
    plt.ylabel('Bunch Length, $\sigma_{z}$')
    plt.axis([0,zstop,0,0.0026])
    plt.grid()
    plt.savefig('zrms-'+savefile+'.pdf', dpi=1000, bbox_inches='tight')

    fig4 = plt.figure(4)
    pltde = plot_profile1D(ds, 's', 'Dx', xsci=True) #, label='$sigma_z$ [mm]')
    plt.ylabel('Dispersion in x') #, $\sigma_{z}$')
    #plt.axis([0,zstop,0,0.004])
    plt.grid()
    plt.savefig('Dx-'+savefile+'.pdf', dpi=1000, bbox_inches='tight')


    fig5 = plt.figure(5)
    pltem = plot_profile1D(ds, 's', 'emit_x', xsci=True, label='$\epsilon_x$ [mm]')
    pltem = plot_profile1D(ds, 's', 'emit_y', xsci=True, label='$\epsilon_y$ [mm]')
    plt.ylabel('Emittance $\epsilon_{nx,ny}$') #, $\sigma_{z}$')
    plt.axis([0,zstop,0,0.0008])
    plt.grid()
    plt.savefig('emit-'+savefile+'.pdf', dpi=1000, bbox_inches='tight')

    fig6 = plt.figure(6)
    pltenergy = plot_profile1D(ds, 's', 'energy', xsci=True)
    plt.ylabel('Energy') #, $\sigma_{z}$')
    #plt.axis([0,25,0,0.0007])
    plt.grid()
    plt.savefig('energy-'+savefile+'.pdf', dpi=1000, bbox_inches='tight')

    fig7 = plt.figure(7)
    pltmax = plot_profile1D(ds, 's', 'max_x', xsci=True, label='max x')
    pltmax = plot_profile1D(ds, 's', 'max_y', xsci=True, label='max y')

    #2 inch pipe
    plt.plot([10, 16.5],   [0.05, 0.05], 'k-', label = 'Beam pipe aperture')
    plt.plot([16.5, 16.5], [0.05, 0.04], 'k-') #Down from kicker to septum
    plt.plot([17.6, 18.6],[0.025,0.025], 'k-') #1 inch, dipole
    plt.plot([18.7, 18.7], [0.025, 0.05], 'k-') #label = '1/6 of 2 inch pipe')
    plt.plot([18.7,21.8], [0.05, 0.05], 'k-')
    plt.plot([21.8, 21.8], [0.05, 0.018], 'k-')
    plt.plot([22.5, 22.5], [0.018, 0.05], 'k-')
    plt.plot([22.5, 25], [0.05, 0.05], 'k-')

    #1 inch pipe
    plt.plot([17.6, 17.6], [0.04, 0.025], 'k-')#label = '1/6 of 1 inch pipe')
    plt.plot([21.8, 22.5], [0.018, 0.018], 'k-')#label = '1/6 of PETS')

    #Colored elements
    plt.plot([19.4,19.4],[0,0.05], '-g', label='$s_3$')
    plt.plot([16.5,17.6],[0.04,0.04], 'b-o', label='kicker')
    plt.plot([13.6, 19.4, 21.2], [0.05, 0.05,0.05], 'g^', label='quads')
    plt.plot(z,y*6, 'ko', label = 'dipole')

    plt.ylabel('Max Beam Sizes', size=20) #, $\sigma_{z}$')
    plt.axis([0,zstop,0,0.055])
    plt.legend(loc='lower left')
    plt.grid()
    plt.savefig('xy-max-min-'+savefile+'.pdf', dpi=1000, bbox_inches='tight')


