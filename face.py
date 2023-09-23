import cv2
import face_recognition

# Load a sample image containing the face you want to store
image = face_recognition.load_image_file("path_to_image.jpg")

# Find face locations
face_locations = face_recognition.face_locations(image)

if len(face_locations) == 0:
    print("No face found in the image.")
else:
    # Encode the first found face
    face_encoding = face_recognition.face_encodings(image, known_face_locations=face_locations)[0]

    # Convert the face encoding to a string (you can use libraries like base64)
    face_encoding_str = str(face_encoding.tolist())

    # Store the face encoding in the database along with a name or identifier
    # Use MySQL Connector/Python to insert the data into the database
