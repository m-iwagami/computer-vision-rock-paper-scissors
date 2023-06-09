import cv2 #the module import name for opencv-python
from keras.models import load_model #keras model is to make prediction
import numpy as np  # library 

#Save the model to make prediction
model = load_model('keras_model.h5')
#To capture an image
cap = cv2.VideoCapture(0)
#An array object represents a multidimensional, homogeneous array of fixed-size items.
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

while True: 
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)
    cv2.imshow('frame', frame)
    # Press q to close the window
    print(prediction)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
            
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()
