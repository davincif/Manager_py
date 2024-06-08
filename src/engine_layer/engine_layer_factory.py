from engine_layer.interfaces.camera_frame_interface import CameraFrameInterface
from engine_layer.interfaces.engine_layer_interface import EngineLayerInterface
from engine_layer.interfaces.engine_types import PointType
from engine_layer.text_engine.camera_frame_text import CameraFrameText
from engine_layer.text_engine.engine_layer_text import EngineLayerText
from engine_layer.text_engine.surface_text import SurfaceText


def factory_engine_layer() -> EngineLayerInterface:
    return EngineLayerText()


def factory_surface(size: tuple[int, int]) -> EngineLayerInterface:
    return SurfaceText(size)


def factory_camera_frame(
    upper_left: PointType, size: PointType
) -> CameraFrameInterface:
    return CameraFrameText(upper_left, size)
