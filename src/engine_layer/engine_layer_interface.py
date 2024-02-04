from abc import ABC, abstractmethod


class EngineLayerInterface(ABC):

    @abstractmethod
    def initialize_engine(self):
        pass

    @abstractmethod
    def finish_engine(self):
        pass
