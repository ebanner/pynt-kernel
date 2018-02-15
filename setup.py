from distutils.core import setup

with open('README.rst') as f:
    readme = f.read()

setup(
    name='pynt_kernel',
    version='0.1',
    packages=['pynt_kernel'],
    description='Simple kernel which wraps code cells in a call to BlockingKernelClient.execute_interactive()',
    long_description=readme,
    author='Edward Banner',
    author_email='edward.banner@gmail.com',
    url='https://github.com/ebanner/pynt-kernel',
    install_requires=[
        'jupyter_client', 'IPython', 'ipykernel', 'astor'
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
    ],
)
