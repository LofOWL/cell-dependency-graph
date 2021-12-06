import ast
from ast import *
import inspect

def Assign(node):
    producers = [value.id for target in node.targets for value in ast.walk(target) if isinstance(value,ast.Name)]
    consumer = [value.id for value in ast.walk(node.value) if isinstance(value,ast.Name)]
    return producers,consumer

def AugAssign(node):
    consumer1 = [node.target.id] if isinstance(node.target,ast.Name) else []
    consumer2 = [node.value.id] if isinstance(node.value,ast.Name) else []
    return consumer1 + consumer2

def Import(node):
    producers = [name.name for name in node.names]
    return producers

def ImportFrom(node):
    producers = [name.name for name in node.names]
    return producers

def Call(node):
    consumers = [arg.id for arg in node.args if isinstance(arg,ast.Name)]
    return consumers

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
        
        # remove the duplicate values
        self.producers = list(set(self.producers))
        self.consumers = list(set(self.consumers))

def f():
    import random
    from random import randint
    a = 20
    b = randint(1,20)
    a = a + b + 10
    c,d = 10,10

if __name__ == "__main__":

    astp = ASTProvider()
    astp.build('print(a,b)')

    print(astp.producers)
    print(astp.consumers)



