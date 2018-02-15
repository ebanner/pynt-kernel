PYNT Kernel
===========

PYNT KERNEL is a simple kernel which wraps code cells in a call to
`BlockingKernelClient.execute_interactive()`.

http://jupyter-client.readthedocs.io/en/latest/wrapperkernels.html

Installation
------------
To install ``pynt_kernel`` locally::

```shell
pip install pynt_kernel
python -m pynt_kernel.install
```

Using the PYNT Kernel
---------------------
**Notebook**: The *New* menu in the notebook should show an option for an PYNT notebook.

**Console frontends**: To use it with the console frontends, add ``--kernel pynt`` to
their command line arguments.

Usage
-----

The special thing about the PYNT kernel is that is allows all code to be sent to a kernel with a specified ID. The use case is to launch a kernel outside of jupyter via `IPython.embed_kernel()`. This will produce a message like the following.

    To connect another client to this kernel, use:
        --existing kernel-55995.json
        
In order to communicate with this kernel evaluate a code cell with the following contents.

    ***55995***
    
Now the code in all subsequent code cells will go to this kernel.

Caveats
-------

Because there is a layer of indirection between the user and the remote kernel, certain notebook features are not available. For example `var?` and `var??` seem to get swallowed up.
