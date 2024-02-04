from abc import ABC, abstractmethod

from utils import Singleton


class EngineLayerInterface(ABC, Singleton):

    @abstractmethod
    def initialize(self):
        pass

    @abstractmethod
    def finish(self):
        pass

    @abstractmethod
    def configLoader(self, addr: str):
        pass
