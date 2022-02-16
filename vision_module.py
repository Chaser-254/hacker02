import argparse
import cv2

ap = argparse.Argumentparser()
ap.add_argument("-v", "--video", help="path to the video file")
args = vars(ap.parse_args())

camvideo = cv2.VideoCapture(args["video"])

while True:
    (grabbed, frame) = camvideo.read()
    ststus = "No Target in Sight"

    if not grabbed:
        break

    gray = cv2.cvtcolor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (7, 7), 0)
    edged = cv2.canny(blurred, 50, 150)

    (cnts, _) = cv2.findcontours(edged.copy(), cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE)

    for cnt in cnts:
        approx = cv2.approxpolyDP(cnt, 0.01 * cv2.arclength(cnt, True),
        True)

        if len(approx) == 5:
            cv2.imshow("Frame", frame)
            key = cv2.waitkey(1) & 
            
            if key == ord("s"):
                break

camvideo.release()
cv2.destroyAllwindows()