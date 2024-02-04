from abc import ABC, abstractmethod

from .singleton import Singleton


class Factory(ABC, Singleton):
    @abstractmethod
    def create(self, **kwargs):
        pass
