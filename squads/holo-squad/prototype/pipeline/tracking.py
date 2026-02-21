"""Tracking modules for hands and object."""

from dataclasses import dataclass
from typing import Optional, Tuple

import cv2
import mediapipe as mp
import numpy as np


@dataclass
class HandSignal:
    x: float
    y: float
    z: float
    visible: bool


class HandTracker:
    def __init__(self, max_num_hands: int = 1, detection_conf: float = 0.5, track_conf: float = 0.5):
        self._mp_hands = mp.solutions.hands
        self._hands = self._mp_hands.Hands(
            max_num_hands=max_num_hands,
            min_detection_confidence=detection_conf,
            min_tracking_confidence=track_conf,
        )

    def detect(self, frame_bgr: np.ndarray) -> HandSignal:
        frame_rgb = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2RGB)
        result = self._hands.process(frame_rgb)
        if not result.multi_hand_landmarks:
            return HandSignal(0.0, 0.0, 0.0, False)

        # Use wrist (landmark 0) as control point
        wrist = result.multi_hand_landmarks[0].landmark[0]
        return HandSignal(wrist.x, wrist.y, wrist.z, True)


class ObjectTracker:
    def __init__(self):
        self._tracker = None
        self._bbox = None

    def init(self, frame_bgr: np.ndarray, bbox: Tuple[int, int, int, int]):
        self._tracker = cv2.TrackerCSRT_create()
        self._bbox = bbox
        self._tracker.init(frame_bgr, bbox)

    def update(self, frame_bgr: np.ndarray) -> Tuple[Optional[Tuple[float, float]], bool]:
        if self._tracker is None:
            return None, False
        ok, bbox = self._tracker.update(frame_bgr)
        if not ok:
            return None, False

        x, y, w, h = bbox
        cx = x + w / 2.0
        cy = y + h / 2.0
        return (cx, cy), True

    def has_tracker(self) -> bool:
        return self._tracker is not None
