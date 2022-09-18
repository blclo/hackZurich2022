# Read QR code

import readQR
import json
import requests
import getMeetingLocation

readQR.json_to_qrcode('info.json', 'MyQRCode1.png')
print(readQR.read_qr_code('MyQRCode1.png'))

#f = open('info.json')
data = readQR.read_qr_code('MyQRCode1.png')
data = data.replace("\'", "\"")

data = json.loads(data)
getMeetingLocation.calendarInfo(data)
