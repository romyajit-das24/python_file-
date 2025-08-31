import cv2

# Load the face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Open the webcam
cam = cv2.VideoCapture(0)

while True:
    # Read frame from the webcam
    ret, frame = cam.read()
    if not ret:
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray)

    # Draw rectangles around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Show the frame
    cv2.imshow("Face Detection", frame)

    # Break loop if 'q' is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# Release resources
cam.release()
cv2.destroyAllWindows()
