"""Basic hologram render overlays."""

from typing import Tuple

import cv2
import numpy as np


HoloColor = Tuple[int, int, int]

PRESETS = {
    "amber": {"glow": (255, 200, 100), "line": (180, 255, 255)},
    "cyan": {"glow": (100, 255, 255), "line": (200, 255, 255)},
    "magenta": {"glow": (255, 120, 220), "line": (255, 200, 255)},
    "blue": {"glow": (255, 160, 80), "line": (255, 220, 160)},
    "green": {"glow": (120, 255, 120), "line": (180, 255, 180)},
    "red": {"glow": (80, 80, 255), "line": (120, 120, 255)},
}


def draw_glow_circle(frame: np.ndarray, center: Tuple[int, int], radius: int, color: HoloColor, intensity: float):
    overlay = frame.copy()
    cv2.circle(overlay, center, radius, color, -1)
    alpha = max(0.05, min(0.8, intensity))
    cv2.addWeighted(overlay, alpha, frame, 1.0 - alpha, 0, frame)


def draw_scanlines(frame: np.ndarray, spacing: int = 6, color: HoloColor = (180, 255, 255)):
    h, w = frame.shape[:2]
    for y in range(0, h, spacing):
        cv2.line(frame, (0, y), (w, y), color, 1)


def render_hologram(frame: np.ndarray, norm_xy: Tuple[float, float], preset: str, glow: float, scanlines: int):
    h, w = frame.shape[:2]
    cx = int(norm_xy[0] * w)
    cy = int(norm_xy[1] * h)

    colors = PRESETS.get(preset, PRESETS["amber"])
    draw_glow_circle(frame, (cx, cy), 40, colors["glow"], glow)
    if scanlines > 0:
        draw_scanlines(frame, spacing=scanlines, color=colors["line"])
    cv2.circle(frame, (cx, cy), 60, (255, 255, 255), 2)


def render_hologram_object(frame: np.ndarray, norm_xy: Tuple[float, float], preset: str, glow: float, scanlines: int):
    h, w = frame.shape[:2]
    cx = int(norm_xy[0] * w)
    cy = int(norm_xy[1] * h)

    # Simple 2.5D "object" wireframe
    size = 50
    colors = PRESETS.get(preset, PRESETS["amber"])
    color = colors["glow"]
    cv2.rectangle(frame, (cx - size, cy - size), (cx + size, cy + size), color, 2)
    cv2.line(frame, (cx - size, cy - size), (cx - size + 12, cy - size - 12), color, 1)
    cv2.line(frame, (cx + size, cy - size), (cx + size + 12, cy - size - 12), color, 1)
    cv2.line(frame, (cx + size, cy + size), (cx + size + 12, cy + size - 12), color, 1)
    cv2.line(frame, (cx - size, cy + size), (cx - size + 12, cy + size - 12), color, 1)
    if scanlines > 0:
        draw_scanlines(frame, spacing=scanlines, color=colors["line"])
