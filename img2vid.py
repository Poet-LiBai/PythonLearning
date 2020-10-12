import cv2
import os

video = cv2.VideoCapture('F:/AI-testvideo/testdata/university.mp4')
fps = video.get(cv2.CAP_PROP_FPS)
frameCount = video.get(cv2.CAP_PROP_FRAME_COUNT)
size = (int(video.get(cv2.CAP_PROP_FRAME_WIDTH)), int(video.get(cv2.CAP_PROP_FRAME_HEIGHT)))

videowriter = cv2.VideoWriter('F:/AI-testvideo/result.avi', cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
frame = 0
while True:
    image = cv2.imread('F:/AI-testvideo/frame/%05d.jpg' % frame)
    # cv2.imshow("video", image)
    cv2.waitKey(int(1000 / int(fps)))
    # cv2.waitKey(int(1000 / int(fps)))
    videowriter.write(image)
    frame += 1
    if frame == frameCount - 1:
        break

video.release()
videowriter.release()
# cv2.destroyAllWindows()
