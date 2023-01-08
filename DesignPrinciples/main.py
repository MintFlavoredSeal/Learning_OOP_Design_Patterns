from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any
from collections.abc import Iterable


class Stage:
    def __init__(self, title : str = "untitled") -> None:
        self._title = title
        self._aims = []
        
    @property
    def title(self) -> str:
        return self._title
    
    @title.setter
    def title(self, other : str) -> None:
        if not isinstance(other, str):
            raise TypeError("The title can't be other types than str.")
        
        self._title = other
        
    def add(self, aim : Aim) -> None:
        self._aims.append(aim)
        
    def save(self, path : str):
        print(bytes(self.title, "utf-8"))

    
class Aim(ABC):
    def __init__(self, params : Any) -> None:
        self.context = params


class SingleAim(Aim):
    def __init__(self, params : str) -> None:
        if not isinstance(params, str):
            raise TypeError("An invalid Type of object is given.")
        
        self.context = params


class MultiAim(Aim):
    def __init__(self, params : Iterable[str]) -> None:
        if not isinstance(params, Iterable[str]):
            raise TypeError("An invalid Type of object is given.")
        
        self.context = params
        

def load() -> None:
    pass


if __name__ == "__main__":
    stage_1 = Stage("Clean Code")
    
    word_list = ["Be consistent",
                 "Prefer meaningful names over comments",
                 "Indentation and style",
                 "Keep methods, classes, files small",
                 "Pure functions",
                 "Refactor switch statement to classes",
                 "Don't pass booleans",
                 "Use the correct constructs",
                 "Don't pass null",
                 "Command Query Separation",
                 "Organize code by the actor it belongs to",
                 "Keep framework code distant",
                 "Tests should be fast, independent and repeatable",
                 "Refactor often",
                 "Use meaningful name"]
    
    for word in word_list:
        stage_1.add(SingleAim(word))
        
    stage_1.save("")