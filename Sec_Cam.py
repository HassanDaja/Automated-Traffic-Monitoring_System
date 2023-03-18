from flask_restful import Resource
from Methods import image_convert
from Find_plate import Number_plate
from DataBase import get_time,delete_data
import datetime
from flask import request
class Sec_cam(Resource):
    def post(self):
        img=request.json['img']
        arr_Time=datetime.datetime.now()
        img=image_convert(img)
        car_id=Number_plate(img)[0][0]
        expected_time=get_time(car_id)
        delete_data(car_id)
        if not expected_time:
            return {'status': 404}
        status=False
        if arr_Time<expected_time:
            status=True
        return {'status':status,'Plate_nums':car_id}



