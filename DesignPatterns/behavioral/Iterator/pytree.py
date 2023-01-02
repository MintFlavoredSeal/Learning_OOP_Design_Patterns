from collections.abc import Iterable, Iterator
from typing import Any
from abc import abstractmethod

class Vertex:
    def __init__(self, key: Any = None) -> None:
        self._key = key
        self.children = []
        
    @property
    def key(self) -> Any:
        return self._key
    
    @key.setter
    def key(self, key: Any = None) -> None:
        self._key = key
        
class TreeIterator(Iterator):
    @abstractmethod
    def __init__(self, root: Vertex) -> None:
        pass
    
    @abstractmethod
    def __next__(self) -> Any:
        pass
    
class TreeIteratorDFS(TreeIterator):
    def __init__(self, root: Vertex) -> None:
        self.stack = [root]
        
    def __next__(self) -> Any:
        try:
            top = self.stack.pop()
            
            for child in top.children[::-1]:
                self.stack.append(child)
        except IndexError:
            raise StopIteration()
        
        return top.key
        
        
class TreeIteratorBFS(TreeIterator):
    def __init__(self, root: Vertex) -> None:
        self.queue = [root]
        
    def __next__(self) -> Any:
        try:
            front = self.queue.pop(0)
            
            for child in front.children:
                self.queue.append(child)
        except IndexError:
            raise StopIteration()
        
        return front.key
        

class Tree(Iterable):
    def __init__(self, key_root : Any = None) -> None:
        self._root = Vertex(key_root)
        self._accessor = dict[Any, Vertex]()
        self.mode = "DFS"
        
        if key_root != None:
            self._accessor[key_root] = self._root
        
    def __contains__(self, key: Any = None) -> bool:
        return key in self._accessor.keys()
        
    @property
    def root(self) -> Vertex:
        return self._root
    
    @root.setter
    def root(self, key: Any = None) -> None:
        if self._root.key == None:
            self._root = Vertex(key)
        else:
            self._accessor.pop(self._root.key)
            self._root.key = key
        
        self._accessor[key] = self._root
        
    def make_child(self, key: Any = None, parent: Any = None) -> None:
        if key in self or parent not in self:
            raise NotImplementedError("FUCK YOU")
        
        self._accessor[key] = Vertex(key)
        self._accessor[parent].children.append(self._accessor[key])
        
    def setTraversalMode(self, mode : str) -> None:
        self.mode = mode
    
    def __iter__(self) -> TreeIterator:
        if self.mode == "DFS":
            return TreeIteratorDFS(self.root)
        elif self.mode == "BFS":
            return TreeIteratorBFS(self.root)
        else:
            raise ValueError(f"Can't identify how to travel the tree: {self.mode}")
    
    
if __name__ == "__main__":
    tree = Tree(1)
    tree.make_child(2, 1)
    tree.make_child(3, 1)
    tree.make_child(4, 2)
    tree.make_child(5, 2)
    tree.make_child(6, 3)
    tree.make_child(7, 3)
    
    print("DFS:"," ".join([str(e) for e in tree]))
    
    tree.setTraversalMode("BFS")
    
    print("BFS:"," ".join([str(e) for e in tree]))