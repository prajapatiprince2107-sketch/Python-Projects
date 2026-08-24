import cv2
import mediapipe as mp

from mediapipe.tasks import python
from mediapipe.tasks.python import vision


# ==============================
# HAND MODEL
# ==============================

hand_options = vision.HandLandmarkerOptions(
    base_options=python.BaseOptions(
        model_asset_path="hand_landmarker.task"
    ),
    running_mode=vision.RunningMode.VIDEO,
    num_hands=2,
    min_hand_detection_confidence=0.5,
    min_hand_presence_confidence=0.5,
    min_tracking_confidence=0.5
)

hand_detector = vision.HandLandmarker.create_from_options(
    hand_options
)


# ==============================
# FACE MODEL
# ==============================

face_options = vision.FaceLandmarkerOptions(
    base_options=python.BaseOptions(
        model_asset_path="face_landmarker.task"
    ),
    running_mode=vision.RunningMode.VIDEO,
    num_faces=1,
    min_face_detection_confidence=0.5,
    min_face_presence_confidence=0.5,
    min_tracking_confidence=0.5
)

face_detector = vision.FaceLandmarker.create_from_options(
    face_options
)


# ==============================
# CAMERA
# ==============================

camera = cv2.VideoCapture(0)

timestamp = 0


while True:

    success, frame = camera.read()

    if not success:
        print("Camera not found!")
        break

    # Mirror
    frame = cv2.flip(frame, 1)

    height, width, _ = frame.shape

    # OpenCV BGR → RGB
    rgb = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2RGB
    )

    mp_image = mp.Image(
        image_format=mp.ImageFormat.SRGB,
        data=rgb
    )

    timestamp += 1


    # ==============================
    # HAND DETECTION
    # ==============================

    hand_result = hand_detector.detect_for_video(
        mp_image,
        timestamp
    )

    for hand in hand_result.hand_landmarks:

        # Draw hand points
        for landmark in hand:

            x = int(landmark.x * width)
            y = int(landmark.y * height)

            if 0 <= x < width and 0 <= y < height:

                cv2.circle(
                    frame,
                    (x, y),
                    5,
                    (0, 255, 0),
                    -1
                )

        # Hand connections
        connections = [
            (0, 1), (1, 2), (2, 3), (3, 4),
            (0, 5), (5, 6), (6, 7), (7, 8),
            (0, 9), (9, 10), (10, 11), (11, 12),
            (0, 13), (13, 14), (14, 15), (15, 16),
            (0, 17), (17, 18), (18, 19), (19, 20),
            (5, 9),
            (9, 13),
            (13, 17)
        ]

        for start, end in connections:

            x1 = int(hand[start].x * width)
            y1 = int(hand[start].y * height)

            x2 = int(hand[end].x * width)
            y2 = int(hand[end].y * height)

            cv2.line(
                frame,
                (x1, y1),
                (x2, y2),
                (0, 255, 0),
                2
            )


    # ==============================
    # FACE + MOUTH DETECTION
    # ==============================

    face_result = face_detector.detect_for_video(
        mp_image,
        timestamp
    )

    if face_result.face_landmarks:

        face = face_result.face_landmarks[0]

        # Face points
        for landmark in face:

            x = int(landmark.x * width)
            y = int(landmark.y * height)

            if 0 <= x < width and 0 <= y < height:

                cv2.circle(
                    frame,
                    (x, y),
                    1,
                    (255, 255, 0),
                    -1
                )


        # ==========================
        # MOUTH POINTS
        # ==========================

        mouth_points = [
            61, 146, 91, 181,
            84, 17, 314, 405,
            321, 375, 291,
            13, 14
        ]

        for point in mouth_points:

            x = int(face[point].x * width)
            y = int(face[point].y * height)

            cv2.circle(
                frame,
                (x, y),
                5,
                (0, 0, 255),
                -1
            )


        # Mouth center
        mouth_x = int(
            (
                face[13].x +
                face[14].x
            ) / 2 * width
        )

        mouth_y = int(
            (
                face[13].y +
                face[14].y
            ) / 2 * height
        )

        cv2.putText(
            frame,
            "MOUTH",
            (mouth_x + 10, mouth_y),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 0, 255),
            2
        )


    # ==============================
    # STATUS
    # ==============================

    cv2.putText(
        frame,
        "HAND + MOUTH TRACKING",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 0),
        2
    )

    cv2.putText(
        frame,
        f"Hands: {len(hand_result.hand_landmarks)}",
        (20, 75),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 255, 255),
        2
    )

    cv2.putText(
        frame,
        f"Face: {len(face_result.face_landmarks)}",
        (20, 110),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 255, 255),
        2
    )


    # Show
    cv2.imshow(
        "HAND + MOUTH MOTION CAPTURE",
        frame
    )


    # Q = quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


camera.release()

hand_detector.close()
face_detector.close()

cv2.destroyAllWindows()