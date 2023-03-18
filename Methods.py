import cv2
import base64
from PIL import Image
import io
import datetime
import numpy as np
def image_convert(data):
    img = Image.open(io.BytesIO(base64.b64decode(data.encode())))
    img_arr = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    return img_arr

def calculate_expectetime(distance, speed_limit):
    new_speed = speed_limit * (5/18)  # convert speed_limit from km/h to m/s
    new_distance = distance * 1000  # convert distance from km to m
    sec = new_distance // new_speed
    return sec

def least_time(distance, speed_limit):
    expected = calculate_expectetime(distance, speed_limit)
    time_change = datetime.timedelta(seconds=expected)
    new_time = datetime.datetime.now() + time_change
    return new_time

def image_to_bytes(img):
    img = Image.open(io.BytesIO(base64.b64decode(img.encode())))
    buffer = io.BytesIO()
    img.save(buffer, format='PNG')
    encoded = base64.b64encode(buffer.getvalue())
    return encoded
