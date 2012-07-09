from setuptools import setup, find_packages


setup(
    name='noseenv',
    version='0.0.0',
    description='Nose plugin to add options of the form "--env ENVIRONMENT_VARIABLE=VALUE"',
    long_description=open('README.md').read(),
    author='Marc Abramowitz',
    author_email='marc@marc-abramowitz.com',
    license='GPL',
    packages=find_packages(exclude=['ez_setup']),
    install_requires=['Nose>=0.11.0'],
    url='http://github.com/msabramo/python-noseenv',
    include_package_data=True,
    entry_points="""
        [nose.plugins.0.10]
        noseenv = noseenv:NoseEnvPlugin
        """,
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Testing'
        ],
)
