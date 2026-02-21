"""Simple 2D Kalman filter for normalized coordinates."""

from typing import Optional, Tuple

import cv2
import numpy as np


class Kalman2D:
    def __init__(self, dt: float = 1.0, process_noise: float = 1e-3, measurement_noise: float = 1e-2):
        self._kf = cv2.KalmanFilter(4, 2)
        self._kf.transitionMatrix = np.array(
            [
                [1, 0, dt, 0],
                [0, 1, 0, dt],
                [0, 0, 1, 0],
                [0, 0, 0, 1],
            ],
            dtype=np.float32,
        )
        self._kf.measurementMatrix = np.array(
            [
                [1, 0, 0, 0],
                [0, 1, 0, 0],
            ],
            dtype=np.float32,
        )
        self._kf.processNoiseCov = np.eye(4, dtype=np.float32) * float(process_noise)
        self._kf.measurementNoiseCov = np.eye(2, dtype=np.float32) * float(measurement_noise)
        self._kf.errorCovPost = np.eye(4, dtype=np.float32)
        self._initialized = False

    def apply(self, x: float, y: float) -> Tuple[float, float]:
        measurement = np.array([[np.float32(x)], [np.float32(y)]])
        if not self._initialized:
            self._kf.statePost = np.array([[x], [y], [0.0], [0.0]], dtype=np.float32)
            self._initialized = True
            return x, y

        self._kf.predict()
        estimate = self._kf.correct(measurement)
        return float(estimate[0]), float(estimate[1])
