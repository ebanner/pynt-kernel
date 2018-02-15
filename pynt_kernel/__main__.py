from ipykernel.kernelapp import IPKernelApp
from . import PyntKernel

IPKernelApp.launch_instance(kernel_class=PyntKernel)
