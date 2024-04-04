from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sensors.db'
db = SQLAlchemy(app)

class EquipSensor(db.Model):
    
    id = db.Column(db.String, primary_key=True)
    equipmentId = db.Column(db.String)
    timestamp = db.Column(db.Datetime)
    value = db.Column(db.Float)


@app.route('/')

def index(): 