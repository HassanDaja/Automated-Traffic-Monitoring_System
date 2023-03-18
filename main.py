from flask import Flask
from flask_restful import Api
from DataBase import db_init
from test123.First_cam import First_cam
from Sec_Cam import Sec_cam
app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Databases/car_info.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db_init(app)

#Main

api.add_resource(First_cam,"/First_cam/")
api.add_resource(Sec_cam,"/Second_cam/")

if __name__=="__main__":
    app.run(debug=True)
