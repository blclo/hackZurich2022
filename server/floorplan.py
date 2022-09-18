import numpy as np
import cv2

def createFloorplan(room_Goal):
    room_Goal = int(room_Goal)
    floorplan_matrix = np.matrix([[11, 12, 13, 14, 15],[21, 0, 0, 0, 25],[31, 0, 33, 0, 35], [41, 0, 0, 0, 45],[51, 52, 53, 255, 50]])

    result = np.where(floorplan_matrix == room_Goal)

    x = 50 + int(result[1])*100
    y = 50 + int(result[0])*100
    img = cv2.imread('./Image.png')
    cv2.circle(img, (x,y), radius=30, color=(0, 0, 255), thickness=3)
    cv2.imwrite("./Floorplan_goal.png", img)