import cv2
from detector import ObjectDetector
from speaker import Speaker

class App:
    def __init__(self):
        self.detector = ObjectDetector()
        self.speaker = Speaker()
        self.cap = cv2.VideoCapture(0)

        self.frame_count = 0
        self.process_every = 5   # 🔥 process 1 frame every 5 frames

    def run(self):
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break

            # 🔥 Resize frame (reduces lag a lot)
            frame = cv2.resize(frame, (640, 480))

            self.frame_count += 1

            detections = []

            # 🔥 Run detection only on some frames
            if self.frame_count % self.process_every == 0:
                detections = self.detector.detect(frame)

            spoken = False

            for det in detections[:2]:  # 🔥 limit to max 2 objects
                label = det["label"]
                if label != "person":
                    x1, y1, x2, y2 = det["box"]

                    # 🔲 Draw bounding box
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

                    # 🏷️ Label
                    cv2.putText(frame, label, (x1, y1 - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

                    # 🔊 Speak only once
                    if not spoken:
                        sentence = f"I detected a {label} in front of you"
                        self.speaker.speak(sentence)
                        spoken = True

            cv2.imshow("AI Vision", frame)

            # ESC key exit
            if cv2.waitKey(1) & 0xFF == 27:
                break

            # Window close fix
            if cv2.getWindowProperty("AI Vision", cv2.WND_PROP_VISIBLE) < 1:
                break

        self.cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    app = App()
    app.run()