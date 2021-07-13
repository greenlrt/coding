# Import necessary libraries
from flask import Flask, render_template, Response
import cv2
import m3u8
import requests
#from singlemotiondetector import SingleMotionDetector
from imutils.video import VideoStream
#import threading
#import datetime
import imutils

url = 'http://s52.ipcamlive.com/streams/34qg1rhjs0f7kxe5b/'

# Initialize the Flask app
app = Flask(__name__)

def gen_frames():  
    while True:
        r = requests.get(url + 'stream.m3u8')

        m3u8_master = m3u8.loads(r.text)

        for segment in m3u8_master.data['segments']:
            camera = cv2.VideoCapture(url + segment['uri']) 
    
            # initialize the first frame in the video stream
            #firstFrame = None

            while True:
                # read the next frame from the video stream, resize it,
                # convert the frame to grayscale and blur it
                success, frame = camera.read()  # read the camera frame
                if not success:
                    break
                else:
                    #frame = imutils.resize(frame, width=400)
                    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    #gray = cv2.GaussianBlur(gray, (21, 21), 0)
    
                    # if the first frame is None, initialize it
                    #if firstFrame is None:
                        #firstFrame = gray
                        #continue

                    # compute the absolute difference between the current frame 
                    # and first frame
                    #frameDelta = cv2.absdiff(firstFrame, gray)
                    #thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]

                    # dialate the thresholded image to fill in holes, then find contours
                    # on thresholded image
                    #thresh = cv2.dilate(thresh, None, iterations=2)
                    #cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                        #cv2.CHAIN_APPROX_SIMPLE)
                    #cnts = imutils.grab_contours(cnts)

                    # loop over the contours
                    #for c in cnts:
                        # if the contour is too small, ignore it
                        #if cv2.contourArea(c) < 50:
                            #continue

                    # compute the bounding box for the contour, draw it on the frame
                    #(x, y, w, h) = cv2.boundingRect(c)
                    #cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)


                    # grab the current timestamp and draw it on the frame
                    #timestamp = datetime.datetime.now()
                    #cv2.putText(frame, timestamp.strftime(
                    #    "%A %d %B % Y %I:%M:%S%p"), (10, frame.shape[0] - 10),
                    #       cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)


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
