import cv2
import numpy as np
from PIL import ImageGrab

def screenRec():

    fourcc = cv2.VideoWriter_fourcc(*'XVID')

    fps = 8.0

    out = cv2.VideoWriter('output.avi',fourcc,fps,(1366,768))

    while(True):

        img = ImageGrab.grab()

        img_np = np.array(img)

        frame = cv2.cvtColor(img_np,cv2.COLOR_BGR2RGB)

        win_title = "Screen Recorder"
        cv2.imshow(win_title, frame)

        out.write(frame)

        if(cv2.waitkey(1) & 0XFF == ord('q')):
            break
    
    out.release()

    cv2.destroyAllWindows()

screenRec()

