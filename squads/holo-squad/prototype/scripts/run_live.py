import argparse
import time

import cv2

from pipeline.tracking import HandTracker, ObjectTracker
from pipeline.mapping import map_hand_signal, map_object_signal
from pipeline.render import render_hologram, render_hologram_object
from pipeline.metrics import MetricsOverlay
from pipeline.kalman import Kalman2D


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--camera", type=int, default=0)
    parser.add_argument("--mode", choices=["hand", "object", "both"], default="hand")
    parser.add_argument("--preset", choices=["amber", "cyan", "magenta", "blue", "green", "red"], default="amber")
    parser.add_argument("--glow", type=float, default=0.35)
    parser.add_argument("--scanlines", type=int, default=6)
    parser.add_argument("--metrics", action="store_true")
    parser.add_argument("--record", default=None, help="Salvar saida em arquivo mp4")
    parser.add_argument("--kalman", action="store_true")
    parser.add_argument("--k-process", type=float, default=1e-3)
    parser.add_argument("--k-measure", type=float, default=1e-2)
    parser.add_argument("--k-preset", choices=["stable", "responsive"], default=None)
    args = parser.parse_args()

    cap = cv2.VideoCapture(args.camera)
    if not cap.isOpened():
        raise SystemExit("Erro ao abrir camera")

    hand_tracker = HandTracker()
    obj_tracker = ObjectTracker()
    metrics = MetricsOverlay()
    if args.k_preset == "stable":
        args.k_process = 5e-4
        args.k_measure = 3e-2
    elif args.k_preset == "responsive":
        args.k_process = 2e-3
        args.k_measure = 8e-3

    kalman_hand = Kalman2D(process_noise=args.k_process, measurement_noise=args.k_measure)
    kalman_obj = Kalman2D(process_noise=args.k_process, measurement_noise=args.k_measure)
    smooth_x = None
    smooth_y = None
    alpha = 0.35

    if args.mode in ("object", "both"):
        ok, first = cap.read()
        if not ok:
            raise SystemExit("Erro ao ler frame inicial")
        bbox = cv2.selectROI("select object", first, False, False)
        cv2.destroyWindow("select object")
        obj_tracker.init(first, bbox)
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    writer = None
    if args.record:
        w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = cap.get(cv2.CAP_PROP_FPS) or 30
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        writer = cv2.VideoWriter(args.record, fourcc, fps, (w, h))

    while True:
        frame_start = time.perf_counter()
        ok, frame = cap.read()
        if not ok:
            break

        h, w = frame.shape[:2]
        if args.mode in ("hand", "both"):
            signal = hand_tracker.detect(frame)
            if signal.visible:
                control = map_hand_signal(signal.x, signal.y)
                smooth_x = control.x if smooth_x is None else (alpha * control.x + (1 - alpha) * smooth_x)
                smooth_y = control.y if smooth_y is None else (alpha * control.y + (1 - alpha) * smooth_y)
                hx, hy = (smooth_x, smooth_y)
                if args.kalman:
                    hx, hy = kalman_hand.apply(hx, hy)
                render_hologram(frame, (hx, hy), args.preset, args.glow, args.scanlines)

        if args.mode in ("object", "both") and obj_tracker.has_tracker():
            center, ok = obj_tracker.update(frame)
            if ok and center:
                control = map_object_signal(center[0], center[1], w, h)
                ox, oy = (control.x, control.y)
                if args.kalman:
                    ox, oy = kalman_obj.apply(ox, oy)
                render_hologram_object(frame, (ox, oy), args.preset, args.glow, args.scanlines)

        if args.metrics:
            m = metrics.tick(frame_start)
            metrics.draw(frame, m)

        if writer is not None:
            writer.write(frame)

        cv2.imshow("holo-live", frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("1"):
            args.mode = "hand"
        elif key == ord("2"):
            args.mode = "object"
            if not obj_tracker.has_tracker():
                ok, first = cap.read()
                if ok:
                    bbox = cv2.selectROI("select object", first, False, False)
                    cv2.destroyWindow("select object")
                    obj_tracker.init(first, bbox)
                    cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        elif key == ord("3"):
            args.mode = "both"
        elif key == 27:
            break

    cap.release()
    if writer is not None:
        writer.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
