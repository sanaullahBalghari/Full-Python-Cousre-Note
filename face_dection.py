import face_recognition;
import cv2
# Load the known images and encode the faces
image_of_person1 = face_recognition.load_image_file("person1.jpg")
person1_face_encoding = face_recognition.face_encodings(image_of_person1)[0]

image_of_person2 = face_recognition.load_image_file("person2.jpg")
person2_face_encoding = face_recognition.face_encodings(image_of_person2)[0]

# Create an array of known face encodings and their corresponding names
known_face_encodings = [person1_face_encoding, person2_face_encoding]
known_face_names = ["person1", "person2"]

# Load the video feed from your webcam
video_capture = cv2.VideoCapture(0)

while True:
    # Capture each frame from the video feed
    ret, frame = video_capture.read()

    # Find all face locations and face encodings in the current frame
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    # Loop through each face found in the frame
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Check if the face matches any known face
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        name = "Unknown"

        # If a match is found, use the name of the known face
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

        # Draw a rectangle and label around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

    # Display the resulting frame
    cv2.imshow("Video", frame)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video feed and close all windows
video_capture.release()
cv2.destroyAllWindows()