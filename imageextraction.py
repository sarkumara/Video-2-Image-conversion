import cv2
import numpy as np
import os

video_path = '/content/drive/My Drive/CNN/FacialEmotion/ImageExtraction/Input/test.avi' #input video Path

skipCount = 4 #frame to be skipped
currentFrame = 0 # Current Frame

cap = cv2.VideoCapture(video_path)

length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print( length )

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    
    if currentFrame % skipCount == 0:
      # Saves image of the current frame in jpg file
       name = '/content/drive/My Drive/CNN/FacialEmotion/ImageExtraction/Output/' + str(currentFrame) + '.jpg' #output image path
       print ('Creating...' + name)
       cv2.imwrite(name, frame)

    # To stop duplicate images
    currentFrame += 1
    
    if currentFrame == length :
     break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()