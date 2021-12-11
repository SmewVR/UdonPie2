import ast
class ASTExplorer:
    def __init__(self, source):
        self.tree = ast.parse(source, mode="exec")
        self.result = list()

    class ASTResult:
        def __init__(self, var, expr, vType):
            self.var = var
            self.expression = expr
            self.vType = vType

    def _getLineAssignment(self, lineno):
        return next((node for node in ast.walk(self.tree) if isinstance(node, ast.Name) and node.lineno == lineno), None)

    def getVariables(self):
        for node in ast.walk(self.tree):
            if not isinstance(node, ast.Assign):
                continue
            nodeValue = node.value
            nodeVariable = self._getLineAssignment(node.lineno).id
            if(isinstance(nodeValue, ast.Constant)):
                nodeExpression = node.value.value
                self.result.append(self.ASTResult(nodeVariable, nodeExpression, type(nodeExpression)))
                continue
            elif(isinstance(nodeValue, ast.Call)):
                callFunc = nodeValue.func.id
                callArgs = "(" + (", ".join([str(x.value) for x in nodeValue.args])) + ")"
                self.result.append(self.ASTResult(nodeVariable, f"{callFunc}{callArgs}", ast.Call))
            #elif... other type handling
        return self.result