import glob
import cv2
#import pandas as pd
import pathlib
import json
import qrcode



def json_to_qrcode(jsonFilePath2, imageFilePath):
    with open(jsonFilePath2, 'r') as jsonf:
        jsonReader = json.load(jsonf)

        qr = qrcode.QRCode(version=1, box_size=15, border=5)
        data = jsonReader
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')
        img.save(imageFilePath)

def read_qr_code(filename):
    """Read an image and read the QR code.

    Args:
        filename (string): Path to file

    Returns:
        qr (string): Value from QR code
    """

    try:
        img = cv2.imread(filename)
        detect = cv2.QRCodeDetector()
        value, points, straight_qrcode = detect.detectAndDecode(img)
        return value
    except:
        print("error")
        return

def goMeeting(data, Meetfloor):
    data["options"]["destination"]["destinationFloor"] = Meetfloor
    data["options"]["destination"]["destinationZone"] = "floor "+str(Meetfloor)

    return data
