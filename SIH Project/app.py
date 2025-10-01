import cv2

camera = cv2.VideoCapture(0)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

def capture_frame():
    ret, frame = camera.read()
    if not ret:
        print("Failed to capture image")
        return None
    cv2.imshow("Camera Preview", frame)
    cv2.imwrite("scanned_image.jpg", frame)
    return frame

while True:
    ret, frame = camera.read()
    if not ret:
        print("Failed to read from camera")
        break
    cv2.imshow("Camera Scanning", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('s'):
        capture_frame()
        print("Image captured successfully!")
    elif key == ord('q'):
        print("Exiting the scanning session.")
        break

camera.release()
cv2.destroyAllWindows()