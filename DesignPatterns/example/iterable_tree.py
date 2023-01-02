from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Any
from abc import ABC, abstractmethod

"""
This example shows an usage of 3 design patterns: Iterator, Strategy, Factory.

The goal of this example is to make a general tree class which supports a variety of tree traversals.
"""

class Factory:
    """
    Did you make another iterator for your custom container and it wouldn't work? All you have to consider are here!
    """
    
    @classmethod
    def make_iterator(cls, mode: str, root: TreeVertex = None) -> TreeIterator:
        if mode == "DFS" and root != None:
            return TreeIteratorDFS(root)
        elif mode == "BFS" and root != None:
            return TreeIteratorBFS(root)
        else:
            raise ValueError(f"invalid traversal mode: {mode}")


class TreeVertex:
    """
    This is a simple class representing nodes for class Tree.
    
    You can re-write this class with the Abstract Factory Pattern
    so that you can easily define the vertex for Graph, BST, list, and so on.
    """
    
    def __init__(self, key: Any = None) -> None:
        self.key = key
        self.children = []
        
        
class TreeIterator(Iterator):
    """
    You can add a your own traversal strategy by inheriting this interface and editing Factory.
    
    You don't need to concern about other classes since the Factory pattern has been implemented.
    """
    @abstractmethod
    def __init__(self, root: TreeVertex) -> None:
        pass
    
    @abstractmethod
    def __next__(self) -> Any:
        pass
    
    
class TreeIteratorDFS(TreeIterator):
    def __init__(self, root: TreeVertex) -> None:
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
    def __init__(self, root: TreeVertex) -> None:
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
    """
    Tree() -> new empty tree
    
    Tree(key) -> new tree whose root is initialized with a given key
    
    Tree(key, mode) -> new tree whose root is initialized with a given key and traversal mode is specified
    
    default traversal mode: "DFS"
    """
    
    def __init__(self, key_root : Any = None, mode_select : str = "DFS") -> None:
        self._root = None
        self._accessor = dict[Any, TreeVertex]()
        self._mode = mode_select
        
        if key_root != None:
            self._root = TreeVertex(key_root)
            self._accessor[key_root] = self._root
        
    def __contains__(self, key: Any = None) -> bool:
        return key in self._accessor.keys()
        
    @property
    def root(self) -> TreeVertex:
        return self._root
    
    @root.setter
    def root(self, key: Any = None) -> None:
        if self._root == None:
            self._root = TreeVertex(key)
        else:
            self._accessor.pop(self._root.key)
            self._root.key = key
        
        self._accessor[key] = self._root
        
    @property
    def mode(self) -> str:
        return self._mode
    
    @mode.setter
    def mode(self, alt: str) -> None:
        self._mode = alt
        
    def make_child(self, key: Any = None, parent: Any = None) -> None:
        if key in self:
            raise ValueError("This object don't allow multiple keys")
        
        if parent not in self:
            raise ValueError("The parent don't exist.")
        
        self._accessor[key] = TreeVertex(key)
        self._accessor[parent].children.append(self._accessor[key])
    
    def __iter__(self) -> TreeIterator:
        return Factory.make_iterator(self.mode, self.root)
    
    
if __name__ == "__main__":
    tree = Tree()
    tree.root = 1
    tree.make_child(2, 1)
    tree.make_child(3, 1)
    tree.make_child(4, 2)
    tree.make_child(5, 2)
    tree.make_child(6, 3)
    tree.make_child(7, 3)
    tree.make_child(8, 5)
    tree.make_child(9, 5)
    
    """
            1
           /  \
          2    3
         / \  / \
        4  5  6  7
          / \
         8   9
    """
    
    show = lambda : print(f"{tree.mode}:"," ".join([str(e) for e in tree]))
    
    show()
    
    tree.mode = "BFS"
    show()