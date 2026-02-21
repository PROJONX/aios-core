"""Simple FPS and latency overlay."""

import time
from dataclasses import dataclass
from typing import Optional

import cv2
import numpy as np


@dataclass
class Metrics:
    fps: float = 0.0
    ms: float = 0.0


class MetricsOverlay:
    def __init__(self, smoothing: float = 0.9):
        self._smoothing = smoothing
        self._last_ts: Optional[float] = None
        self._fps: float = 0.0

    def tick(self, frame_start: float) -> Metrics:
        now = time.perf_counter()
        if self._last_ts is None:
            self._last_ts = now
            return Metrics(0.0, 0.0)

        dt = now - self._last_ts
        inst_fps = 1.0 / dt if dt > 0 else 0.0
        self._fps = self._fps * self._smoothing + inst_fps * (1 - self._smoothing)
        self._last_ts = now

        ms = (now - frame_start) * 1000.0
        return Metrics(self._fps, ms)

    def draw(self, frame: np.ndarray, metrics: Metrics):
        text = f"FPS: {metrics.fps:.1f} | Latency: {metrics.ms:.1f} ms"
        cv2.putText(frame, text, (12, 28), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 3)
        cv2.putText(frame, text, (12, 28), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 1)
