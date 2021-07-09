# Import necessary libraries
from flask import Flask, render_template, Response
import cv2
#from singlemotiondetector import SingleMotionDetector
from imutils.video import VideoStream
#import threading
#import datetime
import imutils
#import time

# initialize the output frame and a lock used to ensure thread-safe
# exchanges of the output frames (useful when multiple browsers/tabs
# are viewing the stream
#outputFrame = None
#lock = threading.Lock()

# Initialize the Flask app
app = Flask(__name__)

#camera = cv2.VideoCapture('../video.ts')
#time.sleep(2.0)

#def detect_motion(frameCount):
    # grab global references to the video stream, out

def gen_frames():  
    camera = cv2.VideoCapture('../video.ts')

    # grab global refereces to the video stream, output frame, and
    # lock variables
    #global camera, outputFrame, lock

    # initialize the motion detector and the total number of frames
    # read thus far
    #md = SingleMotionDetector(accumWeight=0.1)
    #total = 0

    # initialize the first frame in the video stream
    firstFrame = None

    while True:
        # read the next frame from the video stream, resize it,
        # convert the frame to grayscale and blur it
        success, frame = camera.read()  # read the camera frame
        if not success:
            camera = cv2.VideoCapture('../video.ts')
            continue
            break
        else:
            #frame = imutils.resize(frame, width=400)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            gray = cv2.GaussianBlur(gray, (21, 21), 0)

            # if the first frame is None, initialize it
            if firstFrame is None:
                firstFrame = gray
                continue

            # compute the absolute difference between the current frame 
            # and first frame
            frameDelta = cv2.absdiff(firstFrame, gray)
            thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]

            # dialate the thresholded image to fill in holes, then find contours
            # on thresholded image
            thresh = cv2.dilate(thresh, None, iterations=2)
            cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                    cv2.CHAIN_APPROX_SIMPLE)
            cnts = imutils.grab_contours(cnts)

            # loop over the contours
            for c in cnts:
                # if the contour is too small, ignore it
                if cv2.contourArea(c) < 50:
                    continue

                # compute the bounding box for the contour, draw it on the frame
                (x, y, w, h) = cv2.boundingRect(c)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)


            # grab the current timestamp and draw it on the frame
            #timestamp = datetime.datetime.now()
            #cv2.putText(frame, timestamp.strftime(
            #    "%A %d %B % Y %I:%M:%S%p"), (10, frame.shape[0] - 10),
            #       cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)

            # if the total number of frames has reached a sufficient
            # number to construct a reasonable background model
            # continue to process the frame
            #if total > frameCount:
                # detectMotion in the image
            #    motion = md.detect(gray)

                # check to see if motion was found in the frame
            #    if motion is not None:
                    # unpack the tuple and draw the box surrounding the
                    # "motion area" on the output frame
            #        (thresh, (minX, minY, maxX, maxY)) = motion
            #        cv2.rectangle(frame, (minX, minY), (maxX, maxY),
            #            (0, 0, 255), 2)

            # update the background model and increment the total number
            # of frames read thus far
            #md.update(gray)
            #total += 1

            #acquire the lock, set the outputfram, and release the
            # lock
            #with lock:
            #    outputFrame = frame.copy()

            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    # start a thread that will perform motion detection
#    t = threading.Thread(target=detect_motion, args=(32))
    app.run(host='0.0.0.0', port=3000, debug=True)

#camera.stop()
