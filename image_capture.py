import cv2

LEFT_PATH = "C:/Users/example/camera_capture/LEFT/{:03d}.jpg"
RIGHT_PATH = "C:/Users/example/camera_capture/RIGHT/{:03d}.jpg"

left = cv2.VideoCapture(0)
right = cv2.VideoCapture(2)

frame_count = 1

while(frame_count <= 25):

    if not left.grab() or not right.grab():
        print("Frames not grabbed")
        break

    grabbed, left_frame = left.retrieve()
    grabbed, right_frame = right.retrieve()

    cv2.imwrite(LEFT_PATH.format(frame_count), left_frame)
    cv2.imwrite(RIGHT_PATH.format(frame_count), right_frame)

    cv2.imshow('left', left_frame)
    cv2.imshow('right', right_frame)
    frame_count += 1

    # Press escape to quit
    if cv2.waitKey(33) == 27:
        break

left.release()
right.release()
cv2.destroyAllWindows()