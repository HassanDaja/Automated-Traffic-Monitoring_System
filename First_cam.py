from flask_restful import Resource
from Methods import least_time, image_convert
from DataBase import insert_data
from Find_plate import Number_plate
import json
from flask import request


class First_cam(Resource):
    def post(self):
        json_data = request.get_json()
        try:
            dict_data = json.loads(json_data)
        except ValueError:
            return {'error': 'Invalid JSON data'}, 400

        img = dict_data.get('img')
        if not img:
            return {'error': 'Missing image data'}, 400

        converted_img = image_convert(img)
        car_id = Number_plate(converted_img)[0]
        if car_id:
            Distance = dict_data.get('distance', 0)
            Speed_limit = dict_data.get('speed_limit', 0)
            least_expected_time = least_time(Distance, Speed_limit)
            insert_data(car_id[0], dict_data['img'], least_expected_time)
            return {'Plate_nums': car_id}
        else:
            return {'Plate_nums': None}
