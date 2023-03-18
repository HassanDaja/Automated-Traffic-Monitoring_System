import json
import io
import requests
from PIL import Image
import os
import base64
import time

def input_data(img_path):
    full_info=os.path.basename(img_path).split('.')
    name=full_info[0]
    im=Image.open(img_path)
    buffered = io.BytesIO()
    im.save(buffered, format='JPEG')
    img_byte = buffered.getvalue() # bytes
    img_base64 = base64.b64encode(img_byte)
    img_str = img_base64.decode('utf-8')
    format=im.get_format_mimetype()
    return img_str,name,format
def first_send_request(url,img):
    respond=requests.post(url,json=json.dumps({'img':img,'distance':10,'speed_limit':100}))
    print(respond.json())
def sec_send_request(url,img):
    respond=requests.post(url,json={'img':img})
    print(respond.json())

imge=r'Images/ford1.jpg'
url1='http://127.0.0.1:5000/First_cam/'
url2='http://127.0.0.1:5000/Second_cam/'
img,file_name,file_format=input_data(imge)
start=time.time()
first_send_request(url1,img)
sec_send_request(url2,img)
end=time.time()
print(end-start)


