from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

"""
Useful documentation
https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/
https://docs.sqlalchemy.org/en/14/core/type_basics.html#sqlalchemy.types.Text
"""


## Tables

class SportObjects(db.Model):
    __tablename__ = 'sportobjects'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    object_id = db.Column(db.Integer)# id Объекта
    object_name = db.Column(db.String)# Объект
    address = db.Column(db.String)# Адрес
    ved_org_id = db.Column(db.Integer)# id Ведомственной Организации
    ved_org_name = db.Column(db.String) # Ведомственная Организация
    sportzone_id = db.Column(db.Integer) # id Спортзоны
    sportzone_name = db.Column(db.String) # Спортзонаs
    sportzone_type = db.Column(db.String)# Тип спортзоны
    availability_id = db.Column(db.Integer)# Доступность id
    availability_name = db.Column(db.String) # Доступность
    sport_type = db.Column(db.String)# Вид спорта
    latitude = db.Column(db.Float) # Широта(Latitude)
    longitude = db.Column(db.Float) # Долгота(Longitude)
    square = db.Column(db.Float) # Площадь спортзоны

