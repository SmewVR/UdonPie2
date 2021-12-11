import ast

class FuncLister(ast.NodeVisitor):
    def visit_FunctionDef(self, node):
        print(node.name)
        self.generic_visit(node)

source_code = """
import udon_types

a = udon_types.udon_types["Material"]
b = 'sdf'

def sum():
    return a + b
"""

tree = ast.parse(source_code)


for node in ast.walk(tree):
    # VARIABLE NAME
    if isinstance(node, ast.Name):
        print(node.id)

    # VARIABLE VALUES
    if isinstance(node, ast.Constant):
        print(node.value)
    # FUNCTION NAMES
    if isinstance(node, ast.FunctionDef):
        print(node.name)
'''
if(isinstance(nodeValue, ast.Constant)):
    nodeExpression = node.value.value
    self.result.append(self.ASTResult(nodeVariable, nodeExpression, type(nodeExpression)))
    continue
'''