import ast
from ast import *
import inspect
try:
    build_in_functions = [name for name, function in sorted(__builtins__.items()) if inspect.isbuiltin(function) or inspect.isfunction(function)]
except:
    build_in_functions = [name for name, function in sorted(vars(__builtins__).items()) if inspect.isbuiltin(function) or inspect.isfunction(function)]

def removeBIF(list):
    return [i for i in list if i not in build_in_functions]

def Assign(node):
    producers = [value.id for target in node.targets for value in ast.walk(target) if isinstance(value,ast.Name)]
    consumer = [value.id for value in ast.walk(node.value) if isinstance(value,ast.Name)]
    return producers,removeBIF(consumer)

def AugAssign(node):
    consumer1 = [node.target.id] if isinstance(node.target,ast.Name) else []
    consumer2 = [node.value.id] if isinstance(node.value,ast.Name) else []
    return removeBIF(consumer1) + removeBIF(consumer2)

def Import(node):
    producers = [name.name if 'asname' not in name.__dict__ else name.asname for name in node.names]
    return producers

def ImportFrom(node):
    producers = [name.name for name in node.names]
    return producers

def Call(node):
    consumers = [arg.id for arg in node.args if isinstance(arg,ast.Name)]
    return removeBIF(consumers)

def For(node):
    producers = [value.id for value in ast.walk(node.target) if isinstance(value,ast.Name)]
    return producers

class ASTProvider:

    def __init__(self):
        self.producers = list()
        self.consumers = list()

    def reset(self):
        self.producers = list()
        self.consumers = list()

    def build(self,cell_script):
        ast_nodes = ast.parse(cell_script)
        for node in ast.walk(ast_nodes):
            if isinstance(node,ast.Assign):
                pro,con = Assign(node)
                self.producers += pro
                self.consumers += con
            if isinstance(node,ast.AugAssign):
                con = AugAssign(node)
                self.consumers += con
            if isinstance(node,ast.Import):
                self.producers += Import(node)
            if isinstance(node,ast.ImportFrom):
                self.producers += ImportFrom(node)
            if isinstance(node,ast.Call):
                con = Call(node)
                self.consumers += con
            if isinstance(node,ast.For):
                pro = For(node)
                self.producers += pro

        
        # remove the duplicate values
        self.producers = list(set(self.producers))
        self.consumers = list(set(self.consumers))

def foo():
    for i,j in zip([1,2,3],[1,2,3]):
        print(str(i))

if __name__ == "__main__":

    astp = ASTProvider()
    astp.build(inspect.getsource(foo))

    print(astp.producers)
    print(astp.consumers)



