from distutils.core import setup, Extension

setup(  name        = 'fenics_mpm',
        version     = '1.0',
        description = 'MPM with FEniCS',
        author      = 'Evan M. Cummings',
        url         = 'https://github.com/pf4d/fenics_mpm',
        packages    = ['fenics_mpm'],
        package_dir = {'fenics_mpm' : 'fenics_mpm'},
        ext_modules = [Extension('fenics_mpm', ['fenics_mpm/cpp/MPMElasticMaterial.h',
                                                'fenics_mpm/cpp/MPMImpenetrableMaterial.h',
                                                'fenics_mpm/cpp/MPMMaterial.h',
                                                'fenics_mpm/cpp/MPMModel.h'])]
     )



