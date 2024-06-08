from .engine_layer_interface import CameraFrameInterface, EngineLayerInterface, Point
from .engine_layer_text import CameraFrameText, EngineLayerText, SurfaceText


def factory_engine_layer() -> EngineLayerInterface:
    return EngineLayerText()


def factory_surface(size: tuple[int, int]) -> EngineLayerInterface:
    return SurfaceText(size)


def factory_camera_frame(upper_left: Point, size: Point) -> CameraFrameInterface:
    return CameraFrameText(upper_left, size)
