tokens = ['NOP', 'PUSH', 'POP', 'JUMP_IF_FALSE', 'JUMP','EXTERN', 'JUMP_INDIRECT', 'COPY']

code = ('''
def _onMouseDown():
    this_renda = Renderer(this_gameObj.GetComponent('Renderer'))
    this_renda.get_material().set_color(red_color)
''')

from UdonPie_ import ASTExplorer
import ast


source_code = """
import udon_types

a = udon_types.udon_types["Material"]
b = 'sdf'

def sum():
    return a + b
"""

#find functions
tree = ast.parse(source_code)

for node in ast.walk(tree):
    print(node._fields)


x = [x.name for x in ast.walk(tree) if isinstance(x, ast.FunctionDef)]

print(f'functions: {x}')

explorer = ASTExplorer.ASTExplorer(source_code)
for result in explorer.getVariables():
    print(f"Found variable '{result.var}' with a value of '{result.expression}' (type: '{result.vType.__name__}')")

print(tree)

variables = []

def make_code_seg(self) -> str:
    ret_code: str = f'.code_start\n\n'

    for variable in variables:
        ret_code += '.export '+variable+'\n'
    ret_code += '\n'
    ret_code += f'.code_end\n'
    return ret_code



tokens = ('NOP', 'PUSH', 'POP', 'JUMP_IF_FALSE', 'JUMP','EXTERN', 'JUMP_INDIRECT', 'COPY')

