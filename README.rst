PYNT Kernel
===========

PYNT KERNEL is a simple kernel which wraps code cells in a call to
`BlockingKernelClient.execute_interactive()`.

http://jupyter-client.readthedocs.io/en/latest/wrapperkernels.html

Installation
------------
To install ``pynt_kernel`` from PyPI::

```shell
pip install pynt_kernel
python -m pynt_kernel.install
```

Using the PYNT Kernel
---------------------
**Notebook**: The *New* menu in the notebook should show an option for an PYNT notebook.

**Console frontends**: To use it with the console frontends, add ``--kernel pynt`` to
their command line arguments.
