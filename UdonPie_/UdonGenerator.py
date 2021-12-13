
import ast

source_code = """
import udon_types

a = udon_types.udon_types["Material"]
b = 'sdf'

def sum():
    return a + b
"""


variables = []
functions = []

tree = ast.parse(source_code)

for node in ast.walk(tree):
    # VARIABLE NAME
    if isinstance(node, ast.Name):
        variables.append(node.id)
        print(node.id)

    # VARIABLE VALUES
    if isinstance(node, ast.Constant):
        print(node.value)
    # FUNCTION NAMES
    if isinstance(node, ast.FunctionDef):
        functions.append(node.name)
        print(node.name)

print(variables)
print(functions)

def make_code_seg(self) -> str:
    ret_code: str = f'.data_start\n\n'

    for variable in variables:
        ret_code += '.export '+variable+'\n'

    ret_code += '.data_end ' + variable + '\n'
    ret_code += '.code_start ' + variable + '\n'
    for function in functions:
        ret_code += '.export ' + variable + '\n'



    ret_code += '\n'

    ret_code += f'.code_end\n'
    return ret_code
