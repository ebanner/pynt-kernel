import ast

import astor
from ipykernel.ipkernel import IPythonKernel


class PyntKernel(IPythonKernel):
    def do_execute(self, code, silent, store_history=True, user_expressions=None, allow_stdin=False):
        """Execute `code`

        If a code cell is of the form ***N*** then do not send it the kernel.
        Rather establish a connection to the kernel with a file kernel-N.json.

        Otherwise take code and wrap it in a call to
        `client.execute_interactive()`. For example the code

            'x = 5'

        would become

            'client.execute_interactive("x = 5")'

        In order to get the syntax right use AST + ASTOR to make the macro
        change.

        >>> from kernel import PyntKernel
        >>> self = PyntKernel()
        >>> code = 'x = 5'
        >>> silent = False

        """
        if code.startswith('***'):
            star, kernel_id, star = code.split('***')
            return super().do_execute(f"""

from jupyter_client import BlockingKernelClient

client = BlockingKernelClient()
client.load_connection_file('/Users/ebanner/Library/Jupyter/runtime/kernel-{kernel_id}.json')
client.start_channels()

""",
                silent,
                store_history,
                user_expressions,
                allow_stdin
            )
        else:
            call = ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(
                        value=ast.Name(id='client', ctx=ast.Load()),
                        attr='execute_interactive', ctx=ast.Load()
                    ),
                    args=[ast.Str(s=code)],
                    keywords=[]
                )
            )

            return super().do_execute(
                astor.to_source(call).strip() + ';',
                silent,
                store_history,
                user_expressions,
                allow_stdin
            )
