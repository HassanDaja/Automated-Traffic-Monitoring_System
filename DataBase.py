from flask_sqlalchemy import SQLAlchemy
import pandas as pd
from sqlalchemy import create_engine
db = SQLAlchemy()
# Function that initializes the db and creates the tables
def db_init(app):
    db.init_app(app)
    # Creates the logs tables if the db doesnt already exist
    with app.app_context():
        db.create_all()
#DataBase table
class Car_info(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    img = db.Column(db.Text, unique=True, nullable=False)
    expected_time = db.Column(db.DateTime, nullable=False)

#printing Table
def print_DB(path):
    #connecting engine with db file
    engine = create_engine(f'sqlite:///{path}', echo=False)
    #getting info out of the table
    user_table = pd.read_sql_table(table_name="car_info", con=engine)
    print(user_table.iloc[:,0])

#inserting data into the table
def insert_data(ID,Image,time):
    #making img object
    img = Car_info(id=ID,img=Image,expected_time=time)
    #inserting object into the DataBase
    db.session.add(img)
    db.session.commit()

#Deleting Car info by ID after returning ticket status
def delete_data(ID):
    #checking if ID exist in the DataBase
    if db.session.query(Car_info).filter_by(id=ID).count() > 0:
        #Deleting info from the DataBase
        db.session.query(Car_info).filter_by(id=ID).delete()
        db.session.commit()

#Getting the expected time by ID
def get_time(car_id):
    if Car_info.query.filter_by(id=car_id).count()>0:
        data = Car_info.query.filter_by(id=car_id).first()
        return data.expected_time
    else:
        return False


