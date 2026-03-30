import cv2
from detector import ObjectDetector
from speaker import Speaker

class App:
    def __init__(self):
        self.detector = ObjectDetector()
        self.speaker = Speaker()
        self.cap = cv2.VideoCapture(0)

    def run(self):
        while True:
            ret, frame = self.cap.read()

            if not ret:
                break

            labels = self.detector.detect(frame)

            if labels:
                unique_label = labels[0]   # take first detected object
                sentence = f"This is a {unique_label}"
                self.speaker.speak(sentence)

            cv2.imshow("AI Vision", frame)

            if cv2.waitKey(1) & 0xFF == 27:
                break

        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    app = App()
    app.run()