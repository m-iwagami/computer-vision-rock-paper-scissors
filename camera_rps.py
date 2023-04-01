import cv2
from keras.models import load_model
import numpy as np
import time

model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
            
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()

#count down time
timer = 3
start_time = time.time()
elapsed_time = int(time.time() - start_time)
for x in range(elapsed_time):
    print(timer - elapsed_time)


def get_prediction():
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

        key = cv2.waitkey(1)
        if key == ord('s'):
            start_game = True
            initial_time = time.time()
        

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
       
        
        if start_game: 
            result = np.argmax(prediction) 
            if result == [0]:
                result = "Rock"
            elif result == [1]:
                result = "Paper"
            elif result == [2]:
                result = "Scissors"
            else:
                result = "Nothing"
            print(f"you choose {result}")
