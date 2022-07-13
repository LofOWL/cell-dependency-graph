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
    return removeBIF(consumer1),removeBIF(consumer1) + removeBIF(consumer2)

def Import(node):
    producers = [name.name if name.asname == None else name.asname for name in node.names]
    return producers

def ImportFrom(node):
    producers = [name.name for name in node.names]
    return producers

def Call(node):
    consumers = [arg.id for arg in node.args if isinstance(arg,ast.Name)]
    return removeBIF(consumers)

def For(node):
    producers = [value.id for value in ast.walk(node.target) if isinstance(value,ast.Name)]
    consumers = [value.id for value in ast.walk(node.iter) if isinstance(value,ast.Name)]
    return producers,consumers

class ASTProvider:

    def __init__(self):
        self.producers = list()
        self.consumers = list()

    def reset(self):
        self.producers = list()
        self.consumers = list()

    def add(self,producers,consumers):
        for consumer in consumers:
            if consumer not in self.producers:
                self.consumers.append(consumer)
        self.producers += producers

    def build(self,cell_script):
        ast_nodes = ast.parse(cell_script)
        lines = 0
        for node in ast.walk(ast_nodes):
            if isinstance(node,ast.Assign):
                pro,con = Assign(node)
                self.add(pro,con)
            if isinstance(node,ast.AugAssign):
                pro,con = AugAssign(node)
                self.add(pro,con)
            if isinstance(node,ast.Import):
                self.add(Import(node),[])
            if isinstance(node,ast.ImportFrom):
                self.add(ImportFrom(node),[])
            if isinstance(node,ast.Call):
                self.add([],Call(node))
            if isinstance(node,ast.For):
                pro,con = For(node)
                self.add(pro,con)
            lines += 1
        
        # remove the duplicate values
        self.producers = list(set(self.producers))
        self.consumers = list(set(self.consumers))

def foo():
    a += b

if __name__ == "__main__":

    astp = ASTProvider()
    astp.build(inspect.getsource(foo))

    print(astp.producers)
    print(astp.consumers)



