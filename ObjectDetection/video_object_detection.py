import numpy as np
import cv2
import datetime

video_cap = cv2.VideoCapture("images/cars.mp4")

# grab the width and the height of the video stream
frame_width = int(video_cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(video_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(video_cap.get(cv2.CAP_PROP_FPS))
# initialize the FourCC and a video writer object
fourcc = cv2.VideoWriter_fourcc(*"XVID")
writer = cv2.VideoWriter("images/output.mp4", fourcc, fps, (frame_width, frame_height))

# path to the weights and model files
weights = "frozen_inference_graph.pb"
model = "ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt"
# load the MobileNet SSD model trained  on the COCO dataset
net = cv2.dnn.readNetFromTensorflow(weights, model)

# load the class labels the model was trained on
class_names = []
with open("labels.txt", "r") as f:
    class_names = f.read().strip().split("\n")
    
# create a list of random colors to represent each class
np.random.seed(42)
colors = np.random.randint(0, 255, size=(len(class_names), 3))

# loop over the frames
while True:
    # starter time to computer the fps
    start = datetime.datetime.now()
    success, frame = video_cap.read()
    h = frame.shape[0]
    w = frame.shape[1]

    # create a blob from the frame
    blob = cv2.dnn.blobFromImage(
        frame, 1.0/127.5, (320, 320), [127.5, 127.5, 127.5])
    # pass the blog through our network and get the output predictions
    net.setInput(blob)
    output = net.forward() # shape: (1, 1, 100, 7)

       # end time to compute the fps
    end = datetime.datetime.now()
    # calculate the frame per second and draw it on the frame
    fps = f"FPS: {1 / (end - start).total_seconds():.2f}"
    cv2.putText(frame, fps, (50, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 8)
    cv2.imshow("Output", frame)
    # write the frame to disk
    writer.write(frame)
    if cv2.waitKey(10) == ord("q"):
        break

# release the video capture, video writer, and close all windows
video_cap.release()
writer.release()
cv2.destroyAllWindows()