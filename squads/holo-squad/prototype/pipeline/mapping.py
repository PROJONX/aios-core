"""Signal mapping utilities."""

from dataclasses import dataclass


@dataclass
class HoloControl:
    x: float
    y: float
    scale: float


def clamp(value: float, min_v: float = 0.0, max_v: float = 1.0) -> float:
    return max(min_v, min(max_v, value))


def map_hand_signal(x: float, y: float, scale: float = 1.0) -> HoloControl:
    return HoloControl(clamp(x), clamp(y), max(0.2, min(2.0, scale)))


def map_object_signal(x: float, y: float, frame_w: int, frame_h: int, scale: float = 1.0) -> HoloControl:
    nx = x / max(1.0, float(frame_w))
    ny = y / max(1.0, float(frame_h))
    return HoloControl(clamp(nx), clamp(ny), max(0.2, min(2.0, scale)))
