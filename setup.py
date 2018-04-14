from setuptools import setup

long_description = "A Graphical User Interface for generating ChemKED files."

install_requires = ['pyked>=0.4.0',
                    'PyQt5>=5.10.1']

python_requires = '>=3.5'

setup(
    name='chemkedGui',
    version='0.1.1',
    url='https://github.com/mdbernard/ChemKED-gui',
    license='BSD 3-Clause',
    install_requires=install_requires,
    python_requires=python_requires,
    long_description=long_description,
    packages=['chemkedGui'],
    package_dir={'chemkedGui': 'chemkedGui'},
    keywords=['chemical kinetics'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Topic :: Scientific/Engineering :: Chemistry',
    ],

)