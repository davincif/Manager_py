from .engine_layer_interface import EngineLayerInterface
from .engine_layer_text import EngineLayerText
from utils import Factory


class __EngineLayerFactory(Factory):
    def create(self, **kwargs) -> EngineLayerInterface:
        return EngineLayerText()


EngineLayerFactory = __EngineLayerFactory()

__all__ = ["EngineLayerFactory"]
