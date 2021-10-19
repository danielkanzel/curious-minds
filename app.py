from flask import Flask, request, render_template
from flask_migrate import Migrate
import pandas as pd
import os
import io
import json

from src.db_model import db, SportObjects

app = Flask(__name__)
app.config.from_object(os.environ.get("CURIOUS_MINDS_SETTINGS") or "config.DevelopmentConfig")

db.init_app(app)
migrate = Migrate(app, db)

validator = {
     'id Объекта': 'object_id',
     'Объект': 'object_name',
     'Адрес': 'address',
     'id Ведомственной Организации': 'ved_org_id',
     'Ведомственная Организация': 'ved_org_name',
     'id Спортзоны': 'sportzone_id',
     'Спортзона': 'sportzone_name',
     'Тип спортзоны': 'sportzone_type',
     'Доступность': 'availability_id',
     'Доступность.1': 'availability_name',
     'Вид спорта': 'sport_type',
     'Широта (Latitude)': 'latitude',
     'Долгота (Longitude)': 'longitude',
     'Площадь спортзоны': 'square'
}


@app.route("/sportobjects", methods=["GET"])
def sportobjects():
    req = json.loads(request.get_data())

    resp = SportObjects.query.filter_by()
    return resp


@app.route('/population', methods=["GET"])
def population():
    return ...


@app.route('/f_objects', methods=["GET"])
def f_objects():
    return json.dumps(dict(
        SportObjects.query.with_entities(
            SportObjects.object_id,
            SportObjects.object_name
        ).group_by(
            SportObjects.object_id,
            SportObjects.object_name
        ).all()))


@app.route('/f_ved_org', methods=["GET"])
def f_ved_org():
    return json.dumps(dict(
        SportObjects.query.with_entities(
            SportObjects.ved_org_id,
            SportObjects.ved_org_name
        ).group_by(
            SportObjects.ved_org_id,
            SportObjects.ved_org_name
        ).all()))


@app.route('/f_sportzones', methods=["GET"])
def f_sportzones():
    return json.dumps(dict(
        SportObjects.query.with_entities(
            SportObjects.sportzone_id,
            SportObjects.sportzone_name,
            SportObjects.sportzone_type
        ).group_by(
            SportObjects.sportzone_id,
            SportObjects.sportzone_name,
            SportObjects.sportzone_type
        ).all()))


@app.route('/f_availability', methods=["GET"])
def f_availability():
    return json.dumps(dict(
        SportObjects.query.with_entities(
            SportObjects.availability_id,
            SportObjects.availability_name
        ).group_by(
            SportObjects.availability_id,
            SportObjects.availability_name
        ).all()))


@app.route("/uploadfile", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        f = request.files['data_file']
        if not f:
            return "No file"
        stream = io.StringIO(f.stream.read().decode("UTF8"), newline=None)
        stream.seek(0)
        data = pd.read_csv(stream, sep=";")
        data = data[validator.keys()]
        data = data.rename(columns=validator)
        data.to_sql(name="sportobjects", con=db.engine, index=False, if_exists='replace')
        return 'file uploaded successfully '
    if request.method == "GET":
        return render_template("upload_file.html")


if __name__ == "__main__":
    app.run()
